#!/usr/bin/env python3
"""Diff two MAA roguelike recruitment.json files.

The tool compares semantic strategy fields instead of dumping raw JSON. It can
write both machine-readable JSON and human-readable Markdown reports.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TRACKED_OPERATOR_FIELDS = [
    "recruit_priority",
    "promote_priority",
    "recruit_priority_when_team_full",
    "promote_priority_when_team_full",
    "is_start",
    "is_key",
    "is_alternate",
    "skill",
    "alternate_skill",
    "skill_usage",
    "skill_times",
    "alternate_skill_usage",
    "alternate_skill_times",
    "auto_retreat",
]

OFFSET_FIELDS = ["recruit_priority_offsets", "collection_priority_offsets"]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def defaulted_oper(oper: dict[str, Any], group_name: str = "", occurrence: int = 0) -> dict[str, Any]:
    data = {field: oper.get(field) for field in TRACKED_OPERATOR_FIELDS}
    if data["recruit_priority_when_team_full"] is None:
        data["recruit_priority_when_team_full"] = (oper.get("recruit_priority") or 0) - 100
    if data["promote_priority_when_team_full"] is None:
        data["promote_priority_when_team_full"] = (oper.get("promote_priority") or 0) + 300
    for flag in ["is_start", "is_key", "is_alternate"]:
        data[flag] = bool(oper.get(flag, False))
    data["name"] = oper.get("name", "")
    data["group"] = group_name
    data["definition_key"] = make_definition_key(data["name"], group_name, occurrence)
    return data


def make_definition_key(name: str, group_name: str, occurrence: int = 0) -> str:
    suffix = f"#{occurrence}" if occurrence else ""
    return f"{name} [{group_name}]{suffix}"


def normalize_offsets(offsets: Any) -> list[dict[str, Any]]:
    if not isinstance(offsets, list):
        return []
    normalized = []
    for offset in offsets:
        if not isinstance(offset, dict):
            normalized.append({"raw": offset})
            continue
        item = dict(offset)
        if "groups" in item and isinstance(item["groups"], list):
            item["groups"] = sorted(item["groups"])
        normalized.append(item)
    return sorted(normalized, key=lambda x: json.dumps(x, ensure_ascii=False, sort_keys=True))


def index_strategy(data: dict[str, Any]) -> dict[str, Any]:
    groups: dict[str, list[str]] = {}
    operators: dict[str, dict[str, Any]] = {}
    memberships: dict[str, list[str]] = {}
    offsets: dict[str, dict[str, Any]] = {}
    definition_counts: dict[tuple[str, str], int] = {}

    for group in data.get("priority", []):
        group_name = group.get("name", "")
        groups[group_name] = []
        for oper in group.get("opers", []):
            name = oper.get("name", "")
            groups[group_name].append(name)
            memberships.setdefault(name, []).append(group_name)

            pair_key = (name, group_name)
            occurrence = definition_counts.get(pair_key, 0)
            definition_counts[pair_key] = occurrence + 1
            effective = defaulted_oper(oper, group_name, occurrence)
            definition_key = effective["definition_key"]
            operators[definition_key] = effective
            offsets[definition_key] = {
                "operator": name,
                "group": group_name,
                "recruit_priority_offsets": normalize_offsets(oper.get("recruit_priority_offsets")),
                "collection_priority_offsets": normalize_offsets(oper.get("collection_priority_offsets")),
            }

    return {
        "theme": data.get("theme"),
        "groups": groups,
        "operators": operators,
        "memberships": memberships,
        "offsets": offsets,
        "team_complete_condition": data.get("team_complete_condition", []),
    }


def compare_maps(base: dict[str, Any], cand: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    base_ops = base["operators"]
    cand_ops = cand["operators"]
    base_op_names = set(base_ops)
    cand_op_names = set(cand_ops)
    result["operators_added"] = sorted(cand_op_names - base_op_names)
    result["operators_removed"] = sorted(base_op_names - cand_op_names)

    field_changes = []
    flag_changes = []
    skill_changes = []
    priority_fields = {
        "recruit_priority",
        "promote_priority",
        "recruit_priority_when_team_full",
        "promote_priority_when_team_full",
    }
    flag_fields = {"is_start", "is_key", "is_alternate"}
    skill_fields = {
        "skill",
        "alternate_skill",
        "skill_usage",
        "skill_times",
        "alternate_skill_usage",
        "alternate_skill_times",
        "auto_retreat",
    }
    for name in sorted(base_op_names & cand_op_names):
        for field in TRACKED_OPERATOR_FIELDS:
            old = base_ops[name].get(field)
            new = cand_ops[name].get(field)
            if old == new:
                continue
            change = {
                "definition": name,
                "operator": base_ops[name].get("name", name),
                "group": base_ops[name].get("group", ""),
                "field": field,
                "baseline": old,
                "candidate": new,
            }
            if field in priority_fields:
                field_changes.append(change)
            elif field in flag_fields:
                flag_changes.append(change)
            elif field in skill_fields:
                skill_changes.append(change)

    result["priority_changes"] = field_changes
    result["flag_changes"] = flag_changes
    result["skill_metadata_changes"] = skill_changes

    base_groups = base["groups"]
    cand_groups = cand["groups"]
    result["groups_added"] = sorted(set(cand_groups) - set(base_groups))
    result["groups_removed"] = sorted(set(base_groups) - set(cand_groups))
    group_changes = []
    for group in sorted(set(base_groups) & set(cand_groups)):
        old = base_groups[group]
        new = cand_groups[group]
        if old != new:
            group_changes.append(
                {
                    "group": group,
                    "members_added": sorted(set(new) - set(old)),
                    "members_removed": sorted(set(old) - set(new)),
                    "order_changed": old != new and set(old) == set(new),
                    "baseline_order": old,
                    "candidate_order": new,
                }
            )
    result["group_changes"] = group_changes

    offset_changes = []
    for name in sorted(base_op_names | cand_op_names):
        old = base["offsets"].get(name, {})
        new = cand["offsets"].get(name, {})
        if old != new:
            offset_changes.append({"operator": name, "baseline": old, "candidate": new})
    result["offset_changes"] = offset_changes

    if base["team_complete_condition"] != cand["team_complete_condition"]:
        result["team_complete_condition_changes"] = {
            "baseline": base["team_complete_condition"],
            "candidate": cand["team_complete_condition"],
        }
    else:
        result["team_complete_condition_changes"] = None

    return result


def markdown_report(diff: dict[str, Any], baseline: Path, candidate: Path) -> str:
    lines = [
        "# Recruitment Strategy Diff",
        "",
        f"Baseline: `{baseline}`",
        f"Candidate: `{candidate}`",
        "",
    ]

    def section(title: str, rows: list[Any]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not rows:
            lines.append("No changes.")
            lines.append("")
            return
        for row in rows:
            lines.append(f"- `{json.dumps(row, ensure_ascii=False, sort_keys=True)}`")
        lines.append("")

    section("Operators Added", diff["operators_added"])
    section("Operators Removed", diff["operators_removed"])
    section("Groups Added", diff["groups_added"])
    section("Groups Removed", diff["groups_removed"])
    section("Group Changes", diff["group_changes"])
    section("Priority Changes", diff["priority_changes"])
    section("Start/Key/Alternate Flag Changes", diff["flag_changes"])
    section("Skill Metadata Changes", diff["skill_metadata_changes"])
    section("Offsets Changes", diff["offset_changes"])

    lines.append("## Team Complete Condition")
    lines.append("")
    if diff["team_complete_condition_changes"]:
        lines.append("```json")
        lines.append(json.dumps(diff["team_complete_condition_changes"], ensure_ascii=False, indent=2))
        lines.append("```")
    else:
        lines.append("No changes.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--md-out", type=Path)
    args = parser.parse_args()

    baseline = index_strategy(load_json(args.baseline))
    candidate = index_strategy(load_json(args.candidate))
    diff = compare_maps(baseline, candidate)

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(diff, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(diff, ensure_ascii=False, indent=2))

    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(markdown_report(diff, args.baseline, args.candidate), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
