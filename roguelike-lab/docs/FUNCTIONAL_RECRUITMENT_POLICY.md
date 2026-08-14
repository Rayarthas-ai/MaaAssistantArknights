# Functional Recruitment Policy

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

## Goal

Move recruitment research from fixed profession/star thinking toward an explainable functional model around the first Carry `望`. This document is a lab policy design only; it does not change MaaCore or official resources.

## Functional Roles

- `main_carry`
- `ground`
- `block`
- `healing`
- `sustain`
- `economy`
- `ranged`
- `anti_air`
- `burst`
- `control`
- `fast_redeploy`
- `bait`
- `summon`
- `utility`
- `emergency`

An operator may carry multiple functional tags. Profession is input evidence, not the final team-completeness model. For example, `古米` is represented as ground, block, healing, and sustain because current MAA groups include `重装`, `地面阻挡`, and `奶盾`.

## Current MAA Support

Current JSON can directly support coarse score changes through priority fields and group-based offsets. It cannot fully compute current Hope budget, exact missing functional roles, multi-role value, or duplicate functional saturation.

## Lab-Only Model

`FunctionalRoleEvaluator` takes a `TeamState` plus `operator_function_profiles.json` and outputs coverage, missing roles, weak roles, and saturated roles. Thresholds are configurable and intentionally not tied to fixed profession templates.

`CandidateScorer` explains scores with Wang policy, missing function bonus, multi-role bonus, zero/low Hope efficiency, promotion value, duplicate penalties, and Hope reserve pressure. The prototype does not claim final numeric balance.

## Decision Types

- `RECRUIT`: currently supported by recruitment scoring.
- `PROMOTE`: currently approximated by promote priority.
- `SKIP`: needs Core decision support.
- `RESERVE`: needs Core/Hope-aware state support.
