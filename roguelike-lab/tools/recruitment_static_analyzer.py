#!/usr/bin/env python3
"""Static analyzer for MAA roguelike recruitment.json files."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_PRIORITY_EXTREME = 1000
DEFAULT_OFFSET_EXTREME = 500


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def is_number(value: Any) -> bool:
    return isinstance(value, int | float) and not isinstance(value, bool)


def operator_effective(oper: dict[str, Any]) -> dict[str, Any]:
    recruit = oper.get("recruit_priority", 0)
    promote = oper.get("promote_priority", 0)
    return {
        "name": oper.get("name", ""),
        "recruit_priority": recruit,
        "promote_priority": promote,
        "recruit_priority_when_team_full": oper.get("recruit_priority_when_team_full", recruit - 100),
        "promote_priority_when_team_full": oper.get("promote_priority_when_team_full", promote + 300),
        "is_start": bool(oper.get("is_start", False)),
        "is_key": bool(oper.get("is_key", False)),
        "is_alternate": bool(oper.get("is_alternate", False)),
        "skill": oper.get("skill"),
        "alternate_skill": oper.get("alternate_skill"),
        "auto_retreat": oper.get("auto_retreat", 0),
        "recruit_priority_offsets": oper.get("recruit_priority_offsets", []),
        "collection_priority_offsets": oper.get("collection_priority_offsets", []),
        "raw": oper,
    }


def index_strategy(data: dict[str, Any]) -> dict[str, Any]:
    groups: dict[str, list[str]] = {}
    operators: dict[str, list[dict[str, Any]]] = defaultdict(list)
    group_docs: dict[str, str] = {}
    for group in data.get("priority", []):
        group_name = group.get("name", "")
        groups.setdefault(group_name, [])
        group_docs[group_name] = group.get("doc", "")
        for oper in group.get("opers", []):
            name = oper.get("name", "")
            groups[group_name].append(name)
            operators[name].append({**operator_effective(oper), "group": group_name})
    return {
        "theme": data.get("theme"),
        "groups": groups,
        "group_docs": group_docs,
        "operators": operators,
        "team_complete_condition": data.get("team_complete_condition", []),
    }


def add_issue(issues: list[dict[str, Any]], severity: str, code: str, message: str, **details: Any) -> None:
    issues.append({"severity": severity, "code": code, "message": message, **details})


def check_schema(data: dict[str, Any], issues: list[dict[str, Any]]) -> None:
    if data.get("theme") is None:
        add_issue(issues, "error", "missing_theme", "Missing top-level theme.")
    if not isinstance(data.get("priority"), list):
        add_issue(issues, "error", "missing_priority", "Top-level priority must be an array.")
        return
    if not isinstance(data.get("team_complete_condition"), list):
        add_issue(
            issues,
            "error",
            "missing_team_complete_condition",
            "Top-level team_complete_condition must be an array.",
        )

    for group_index, group in enumerate(data.get("priority", [])):
        if not isinstance(group, dict):
            add_issue(issues, "error", "group_not_object", "Group entry is not an object.", index=group_index)
            continue
        if not group.get("name"):
            add_issue(issues, "error", "group_missing_name", "Group is missing name.", index=group_index)
        if not isinstance(group.get("opers"), list):
            add_issue(issues, "error", "group_missing_opers", "Group opers must be an array.", group=group.get("name"))
            continue
        for oper_index, oper in enumerate(group.get("opers", [])):
            if not isinstance(oper, dict):
                add_issue(issues, "error", "operator_not_object", "Operator entry is not an object.", group=group.get("name"), index=oper_index)
                continue
            if not oper.get("name"):
                add_issue(issues, "error", "operator_missing_name", "Operator is missing name.", group=group.get("name"), index=oper_index)
            for field in ["recruit_priority", "promote_priority", "recruit_priority_when_team_full", "promote_priority_when_team_full", "skill", "alternate_skill", "auto_retreat"]:
                if field in oper and not is_number(oper[field]):
                    add_issue(issues, "error", "field_not_number", f"`{field}` should be numeric.", group=group.get("name"), operator=oper.get("name"), value=oper[field])
            for field in ["is_start", "is_key", "is_alternate"]:
                if field in oper and not isinstance(oper[field], bool):
                    add_issue(issues, "warning", "flag_not_boolean", f"`{field}` should be boolean.", group=group.get("name"), operator=oper.get("name"), value=oper[field])


def analyze(data: dict[str, Any], priority_extreme: int, offset_extreme: int) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    check_schema(data, issues)
    idx = index_strategy(data)

    groups = idx["groups"]
    operators = idx["operators"]
    all_group_names = set(groups)
    membership_count = Counter()
    for members in groups.values():
        membership_count.update(members)

    for name, count in sorted(membership_count.items()):
        if count > 1:
            definitions = operators.get(name, [])
            raw_defs = [{k: v for k, v in d.items() if k not in {"raw"}} for d in definitions]
            add_issue(
                issues,
                "info",
                "duplicate_operator",
                "Operator appears in multiple groups. This can be intentional, but check for conflicting metadata.",
                operator=name,
                count=count,
                definitions=raw_defs,
            )

    for name, definitions in operators.items():
        for info in definitions:
            for field in [
                "recruit_priority",
                "promote_priority",
                "recruit_priority_when_team_full",
                "promote_priority_when_team_full",
            ]:
                value = info.get(field, 0)
                if abs(value) >= priority_extreme:
                    add_issue(
                        issues,
                        "info",
                        "extreme_priority",
                        f"`{field}` is extreme; verify it is intentional.",
                        operator=name,
                        group=info["group"],
                        field=field,
                        value=value,
                    )
            if info["is_start"] and info["recruit_priority"] <= 0:
                add_issue(
                    issues,
                    "warning",
                    "start_with_nonpositive_priority",
                    "Start operator has non-positive recruit priority.",
                    operator=name,
                    group=info["group"],
                )
            if info["is_key"] and info["recruit_priority"] <= 0:
                add_issue(
                    issues,
                    "warning",
                    "key_with_nonpositive_priority",
                    "Key operator has non-positive recruit priority.",
                    operator=name,
                    group=info["group"],
                )

    start_count = sum(1 for defs in operators.values() for d in defs if d["is_start"])
    key_count = sum(1 for defs in operators.values() for d in defs if d["is_key"])
    if start_count < 3 or start_count > 80:
        add_issue(
            issues,
            "warning",
            "start_operator_count_anomaly",
            "Start operator count is outside the expected broad range.",
            count=start_count,
        )
    if key_count < 8 or key_count > 160:
        add_issue(
            issues,
            "warning",
            "key_operator_count_anomaly",
            "Key operator count is outside the expected broad range.",
            count=key_count,
        )

    for condition_index, condition in enumerate(idx["team_complete_condition"]):
        cond_groups = condition.get("groups", [])
        threshold = condition.get("threshold", 0)
        missing = [g for g in cond_groups if g not in all_group_names]
        if missing:
            add_issue(
                issues,
                "error",
                "team_complete_unknown_group",
                "team_complete_condition references unknown group(s).",
                condition_index=condition_index,
                missing_groups=missing,
            )
        possible_ops = set()
        for group in cond_groups:
            possible_ops.update(groups.get(group, []))
        if threshold > len(possible_ops):
            add_issue(
                issues,
                "error",
                "team_complete_impossible",
                "team_complete_condition threshold exceeds unique operators available in referenced groups.",
                condition_index=condition_index,
                threshold=threshold,
                unique_operator_count=len(possible_ops),
            )

    for name, definitions in operators.items():
        for info in definitions:
            for field in ["recruit_priority_offsets", "collection_priority_offsets"]:
                offsets = info.get(field) or []
                if not isinstance(offsets, list):
                    add_issue(issues, "error", "offset_not_array", f"`{field}` should be an array.", operator=name, group=info["group"])
                    continue
                for offset_index, offset in enumerate(offsets):
                    if not isinstance(offset, dict):
                        add_issue(issues, "error", "offset_not_object", "Offset entry should be an object.", operator=name, group=info["group"], field=field, offset_index=offset_index)
                        continue
                    if field == "recruit_priority_offsets":
                        offset_groups = offset.get("groups", [])
                        missing = [g for g in offset_groups if g not in all_group_names]
                        if missing:
                            add_issue(
                                issues,
                                "error",
                                "offset_unknown_group",
                                "Offset references unknown group(s).",
                                operator=name,
                                group=info["group"],
                                offset_index=offset_index,
                                missing_groups=missing,
                            )
                        possible_ops = set()
                        for group in offset_groups:
                            possible_ops.update(groups.get(group, []))
                        threshold = offset.get("threshold", 0)
                        is_less = bool(offset.get("is_less", False))
                        if not is_less and threshold > len(possible_ops):
                            add_issue(
                                issues,
                                "warning",
                                "offset_never_triggers",
                                "Offset threshold is greater than unique operators available in referenced groups.",
                                operator=name,
                                group=info["group"],
                                offset_index=offset_index,
                                threshold=threshold,
                                unique_operator_count=len(possible_ops),
                            )
                    value = offset.get("offset", 0)
                    if is_number(value) and abs(value) >= offset_extreme:
                        add_issue(
                            issues,
                            "info",
                            "extreme_offset",
                            "Offset is large; verify it cannot dominate unexpectedly.",
                            operator=name,
                            group=info["group"],
                            field=field,
                            offset_index=offset_index,
                            value=value,
                        )

    for name, definitions in operators.items():
        if len(definitions) <= 1:
            continue
        comparable = []
        for d in definitions:
            comparable.append(
                {
                    "group": d["group"],
                    "skill": d.get("skill"),
                    "alternate_skill": d.get("alternate_skill"),
                    "recruit_priority": d.get("recruit_priority"),
                    "promote_priority": d.get("promote_priority"),
                    "is_start": d.get("is_start"),
                    "is_key": d.get("is_key"),
                    "is_alternate": d.get("is_alternate"),
                }
            )
        if len({json.dumps(x, ensure_ascii=False, sort_keys=True) for x in comparable}) > 1:
            add_issue(
                issues,
                "warning",
                "operator_conflicting_strategy",
                "Same operator has different strategy metadata across groups.",
                operator=name,
                definitions=comparable,
            )

    summary = {
        "theme": idx["theme"],
        "group_count": len(groups),
        "operator_definition_count": sum(len(v) for v in operators.values()),
        "unique_operator_count": len(operators),
        "start_operator_count": start_count,
        "key_operator_count": key_count,
        "team_complete_condition_count": len(idx["team_complete_condition"]),
        "issue_count": len(issues),
        "issues_by_severity": dict(Counter(issue["severity"] for issue in issues)),
    }

    return {"summary": summary, "issues": issues, "index": idx}


def issue_markdown(analysis: dict[str, Any], source: Path) -> str:
    summary = analysis["summary"]
    issues = analysis["issues"]
    lines = [
        "# Recruitment Static Analysis",
        "",
        f"Source: `{source}`",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Issues", ""])
    if not issues:
        lines.append("No issues found.")
        lines.append("")
        return "\n".join(lines)

    order = {"error": 0, "warning": 1, "info": 2}
    for issue in sorted(issues, key=lambda x: (order.get(x["severity"], 9), x["code"], x.get("operator", ""))):
        details = {k: v for k, v in issue.items() if k not in {"severity", "code", "message"}}
        lines.append(f"- **{issue['severity']}** `{issue['code']}`: {issue['message']}")
        if details:
            lines.append(f"  `{json.dumps(details, ensure_ascii=False, sort_keys=True)}`")
    lines.append("")
    return "\n".join(lines)


def baseline_markdown(analysis: dict[str, Any], source: Path) -> str:
    idx = analysis["index"]
    groups = idx["groups"]
    operators = idx["operators"]
    team_complete = idx["team_complete_condition"]

    start_ops = []
    key_ops = []
    collection_offsets = []
    recruit_offsets = []
    for name, defs in operators.items():
        for d in defs:
            if d["is_start"]:
                start_ops.append((name, d["group"], d["recruit_priority"], d["promote_priority"]))
            if d["is_key"]:
                key_ops.append((name, d["group"], d["recruit_priority"], d["promote_priority"]))
            if d.get("collection_priority_offsets"):
                collection_offsets.append((name, d["group"], d["collection_priority_offsets"]))
            if d.get("recruit_priority_offsets"):
                recruit_offsets.append((name, d["group"], d["recruit_priority_offsets"]))

    def sort_score(row: tuple[Any, ...]) -> tuple[int, int, str]:
        return (-(row[2] or 0), -(row[3] or 0), row[0])

    lines = [
        "# JieGarden Recruitment Baseline",
        "",
        f"Source: `{source}`",
        f"Theme: `{idx['theme']}`",
        "",
        "## Human Strategy Summary",
        "",
        "The official JieGarden recruitment strategy is a rule-and-score table. It first protects opening operators through `is_start`, then protects team structure through `is_key` and `team_complete_condition`. Candidate operators are scored by `recruit_priority` for new recruitment and `promote_priority` for promotion. Team composition and some collectibles can adjust those scores through offsets.",
        "",
        "### Opening Core Operators",
        "",
        "Operators marked `is_start=true`, sorted by recruitment priority:",
        "",
        "| Operator | Group | Recruit | Promote |",
        "| --- | --- | ---: | ---: |",
    ]
    for name, group, recruit, promote in sorted(start_ops, key=sort_score):
        lines.append(f"| {name} | {group} | {recruit} | {promote} |")

    lines.extend([
        "",
        "### Team Core Operators",
        "",
        "Operators marked `is_key=true`, sorted by recruitment priority:",
        "",
        "| Operator | Group | Recruit | Promote |",
        "| --- | --- | ---: | ---: |",
    ])
    for name, group, recruit, promote in sorted(key_ops, key=sort_score):
        lines.append(f"| {name} | {group} | {recruit} | {promote} |")

    lines.extend(["", "### Team Complete Conditions", ""])
    for i, condition in enumerate(team_complete, start=1):
        lines.append(
            f"{i}. At least `{condition.get('threshold')}` unique operator(s) from groups: "
            + ", ".join(f"`{g}`" for g in condition.get("groups", []))
        )

    lines.extend([
        "",
        "Interpretation:",
        "",
        "- The first condition demands two high-value carry/core-output groups.",
        "- The second condition demands two ground/blocking or summon/Kal'tsit-style stabilizers.",
        "- The third condition demands at least one healing lane.",
        "- The fourth condition demands at least one DP/cost-recovery group.",
        "",
        "### Mutual Exclusion And Downranking",
        "",
        "Negative `recruit_priority_offsets` are the main JSON mechanism for avoiding over-recruiting similar roles. The most common pattern is: once a referenced group is already present, reduce the score of another operator in the same strategic lane.",
        "",
    ])
    for name, group, offsets in recruit_offsets:
        neg = [o for o in offsets if isinstance(o, dict) and (o.get("offset", 0) or 0) < 0]
        if neg:
            lines.append(f"- `{name}` in `{group}` has negative recruitment offsets: `{json.dumps(neg, ensure_ascii=False)}`")

    lines.extend([
        "",
        "### Conditional Upweighting",
        "",
        "Positive `recruit_priority_offsets` raise priority when a team need is still missing or a condition is met.",
        "",
    ])
    for name, group, offsets in recruit_offsets:
        pos = [o for o in offsets if isinstance(o, dict) and (o.get("offset", 0) or 0) > 0]
        if pos:
            lines.append(f"- `{name}` in `{group}` has positive recruitment offsets: `{json.dumps(pos, ensure_ascii=False)}`")

    lines.extend([
        "",
        "### Collectible-Driven Priority",
        "",
    ])
    if collection_offsets:
        for name, group, offsets in collection_offsets:
            lines.append(f"- `{name}` in `{group}` changes priority from collectibles: `{json.dumps(offsets, ensure_ascii=False)}`")
    else:
        lines.append("No `collection_priority_offsets` found.")

    lines.extend([
        "",
        "## Operator Groups",
        "",
    ])
    for group, members in groups.items():
        lines.append(f"### {group}")
        doc = idx["group_docs"].get(group)
        if doc:
            lines.append("")
            lines.append(doc)
        lines.extend(["", "| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |", "| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |"])
        for name in members:
            defs = [d for d in operators[name] if d["group"] == group]
            d = defs[0]
            lines.append(
                f"| {name} | {d['recruit_priority']} | {d['promote_priority']} | "
                f"{d['recruit_priority_when_team_full']} | {d['promote_priority_when_team_full']} | "
                f"{d['is_start']} | {d['is_key']} | {d['is_alternate']} | "
                f"{d.get('skill') or ''} | {d.get('alternate_skill') or ''} | {d.get('auto_retreat') or 0} | "
                f"`{json.dumps(d.get('recruit_priority_offsets') or [], ensure_ascii=False)}` | "
                f"`{json.dumps(d.get('collection_priority_offsets') or [], ensure_ascii=False)}` |"
            )
        lines.append("")

    lines.extend(["## Static Analyzer Summary", ""])
    for key, value in analysis["summary"].items():
        lines.append(f"- `{key}`: {value}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--md-out", type=Path)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--baseline-md-out", type=Path)
    parser.add_argument("--priority-extreme", type=int, default=DEFAULT_PRIORITY_EXTREME)
    parser.add_argument("--offset-extreme", type=int, default=DEFAULT_OFFSET_EXTREME)
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    data = load_json(args.input)
    analysis = analyze(data, args.priority_extreme, args.offset_extreme)
    jsonable = {
        "summary": analysis["summary"],
        "issues": analysis["issues"],
    }

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(jsonable, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(issue_markdown(analysis, args.input), encoding="utf-8")
    if args.baseline_md_out:
        args.baseline_md_out.parent.mkdir(parents=True, exist_ok=True)
        args.baseline_md_out.write_text(baseline_markdown(analysis, args.input), encoding="utf-8")
    if not args.json_out and not args.md_out and not args.baseline_md_out:
        print(json.dumps(jsonable, ensure_ascii=False, indent=2))

    if args.fail_on_error and any(issue["severity"] == "error" for issue in analysis["issues"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
