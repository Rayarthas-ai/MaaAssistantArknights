# Hope Budget Policy

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

## Budget Model

```text
Hope Budget
|-- Core Reserve
|-- Survival Budget
`-- Optional Budget
```

## Core Reserve

- `望` not owned: reserve Hope for core recruitment.
- `望` E1: reserve Hope for key promotion.
- `望` E2: core reserve can decrease.

## Survival Budget

May be spent on healing, ground stability, leak prevention, and necessary economy.

## Optional Budget

Used for second Carry, high-value utility, or tactical enhancement after core and survival needs are protected.

## Zero Hope Logic

Zero Hope must be linked to `MissingFunctionNeed`. Forbidden rule:

```text
HopeCost == 0 -> unconditional recruit
```

The prototype grants ZeroHopeBonus only when the candidate covers missing or weak functional roles.
