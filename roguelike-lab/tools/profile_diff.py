#!/usr/bin/env python3
"""Diff formal and candidate operator function profiles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_profiles(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "profiles" in data and isinstance(data["profiles"], dict):
        return data["profiles"]
    return data


def diff_profiles(base: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "operators_added": sorted(set(candidate) - set(base)),
        "operators_removed": sorted(set(base) - set(candidate)),
        "function_changes": [],
        "strategy_tier_changes": [],
        "evidence_added": [],
        "confidence_changes": [],
    }
    for name in sorted(set(base) & set(candidate)):
        b = base[name]
        c = candidate[name]
        bfunc = b.get("functions", {})
        cfunc = c.get("functions", {})
        for fn in sorted(set(bfunc) | set(cfunc)):
            if bfunc.get(fn) != cfunc.get(fn):
                result["function_changes"].append(
                    {"operator": name, "function": fn, "baseline": bfunc.get(fn), "candidate": cfunc.get(fn)}
                )
        if b.get("strategy_tier") != c.get("strategy_tier"):
            result["strategy_tier_changes"].append(
                {"operator": name, "baseline": b.get("strategy_tier"), "candidate": c.get("strategy_tier")}
            )
        if b.get("confidence") != c.get("confidence"):
            result["confidence_changes"].append(
                {"operator": name, "baseline": b.get("confidence"), "candidate": c.get("confidence")}
            )
        if len(c.get("evidence", [])) > len(b.get("evidence", [])):
            result["evidence_added"].append(
                {"operator": name, "added": c.get("evidence", [])[len(b.get("evidence", [])) :]}
            )
    return result


def markdown(diff: dict[str, Any], baseline: Path, candidate: Path) -> str:
    lines = [
        "# Operator Function Profile Diff",
        "",
        f"Baseline: `{baseline}`",
        f"Candidate: `{candidate}`",
        "",
    ]
    for key, title in [
        ("operators_added", "Operators Added"),
        ("operators_removed", "Operators Removed"),
        ("function_changes", "Function Weight/Tag Changes"),
        ("strategy_tier_changes", "Strategy Tier Changes"),
        ("evidence_added", "Evidence Added"),
        ("confidence_changes", "Confidence Changes"),
    ]:
        lines += [f"## {title}", ""]
        rows = diff[key]
        if not rows:
            lines += ["No changes.", ""]
        else:
            lines += [f"- `{json.dumps(row, ensure_ascii=False, sort_keys=True)}`" for row in rows]
            lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--md-out", type=Path)
    args = parser.parse_args()
    diff = diff_profiles(load_profiles(args.baseline), load_profiles(args.candidate))
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(diff, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(diff, ensure_ascii=False, indent=2))
    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(markdown(diff, args.baseline, args.candidate), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
