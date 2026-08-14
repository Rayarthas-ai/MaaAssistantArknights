# Low-Hope Seed Operators

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

Facts are read from official MAA resources. Functional tags are seed hypotheses unless explicitly tied to MAA groups/resources.

## Functional Role Tags

`main_carry`, `ground`, `block`, `healing`, `sustain`, `economy`, `ranged`, `anti_air`, `burst`, `control`, `fast_redeploy`, `bait`, `summon`, `utility`, `emergency`

## 古米

### MAA Facts

- Rarity: `4`; position: `MELEE`; profession: `TANK`; subProfessionId: `guardian`

| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| `重装` | 626 | 790 | 526 | 1090 | 1 | True | True | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}, {"groups": ["凯尔希", "重装", "近卫"], "threshold": 2, "offset": -300}]` |
| `地面阻挡` | 0 | 0 | -100 | 300 |  | False | False | 0 | `[]` |
| `奶盾` | 0 | 0 | -100 | 300 |  | False | False | 0 | `[]` |

### Functional Mapping

| Functional Role | Weight | Evidence status |
| --- | ---: | --- |
| `ground` | 0.6 | seed hypothesis with recorded evidence |
| `block` | 0.8 | seed hypothesis with recorded evidence |
| `healing` | 0.6 | seed hypothesis with recorded evidence |
| `sustain` | 0.7 | seed hypothesis with recorded evidence |

### Interpretation

- Current MAA classification: `重装, 地面阻挡, 奶盾`.
- Functional profile confidence: `medium`.
- Evidence: MAA official: Groups: 重装, 地面阻挡, 奶盾; manual strategy: Ground + Block + Healing + Sustain.
- Needs community guide or game-test validation before being treated as stable.

## 伊桑

### MAA Facts

- Rarity: `4`; position: `MELEE`; profession: `SPECIAL`; subProfessionId: `stalker`

| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| `地刺` | 405 | 405 | 305 | 705 | 2 | True | True | 0 | `[]` |

### Functional Mapping

| Functional Role | Weight | Evidence status |
| --- | ---: | --- |
| `ground` | 0.4 | seed hypothesis with recorded evidence |
| `control` | 0.7 | seed hypothesis with recorded evidence |
| `utility` | 0.4 | seed hypothesis with recorded evidence |
| `emergency` | 0.3 | seed hypothesis with recorded evidence |

### Interpretation

- Current MAA classification: `地刺`.
- Functional profile confidence: `low`.
- Evidence: MAA official: Group: 地刺; SPECIAL/stalker; manual strategy: Phase 4 seed.
- Needs community guide or game-test validation before being treated as stable.

## 砾

### MAA Facts

- Rarity: `4`; position: `MELEE`; profession: `SPECIAL`; subProfessionId: `executor`

| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| `炮灰` | 385 | 300 | 285 | 600 | 2 | False | True | 15 | `[]` |

### Functional Mapping

| Functional Role | Weight | Evidence status |
| --- | ---: | --- |
| `ground` | 0.4 | seed hypothesis with recorded evidence |
| `fast_redeploy` | 0.9 | seed hypothesis with recorded evidence |
| `bait` | 0.9 | seed hypothesis with recorded evidence |
| `emergency` | 0.7 | seed hypothesis with recorded evidence |

### Interpretation

- Current MAA classification: `炮灰`.
- Functional profile confidence: `medium`.
- Evidence: MAA official: Group: 炮灰; auto_retreat=15; manual strategy: Phase 4 seed.
- Needs community guide or game-test validation before being treated as stable.

## 豆苗

### MAA Facts

- Rarity: `4`; position: `RANGED`; profession: `PIONEER`; subProfessionId: `tactician`

| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| `其他高台` | 234 | 200 | 134 | 500 | 2 | False | False | 0 | `[{"groups": ["回费"], "is_less": true, "offset": 150}]` |

### Functional Mapping

| Functional Role | Weight | Evidence status |
| --- | ---: | --- |
| `economy` | 0.7 | seed hypothesis with recorded evidence |
| `ranged` | 0.4 | seed hypothesis with recorded evidence |
| `summon` | 0.4 | seed hypothesis with recorded evidence |
| `utility` | 0.4 | seed hypothesis with recorded evidence |

### Interpretation

- Current MAA classification: `其他高台`.
- Functional profile confidence: `low`.
- Evidence: MAA official: Offset references 回费; MAA official: PIONEER/tactician; manual strategy: Phase 4 seed.
- Needs community guide or game-test validation before being treated as stable.

## 梅

### MAA Facts

- Rarity: `4`; position: `RANGED`; profession: `SNIPER`; subProfessionId: `fastshot`

| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| `速狙` | 679 | 0 | 579 | 300 | 1 | True | True | 0 | `[{"groups": ["水陈", "速狙"], "threshold": 1, "offset": -300}]` |
| `高台输出` | 0 | 0 | -100 | 300 |  | False | False | 0 | `[]` |

### Functional Mapping

| Functional Role | Weight | Evidence status |
| --- | ---: | --- |
| `ranged` | 0.7 | seed hypothesis with recorded evidence |
| `anti_air` | 0.7 | seed hypothesis with recorded evidence |
| `control` | 0.3 | seed hypothesis with recorded evidence |

### Interpretation

- Current MAA classification: `速狙, 高台输出`.
- Functional profile confidence: `medium`.
- Evidence: MAA official: Groups: 速狙, 高台输出; manual strategy: Phase 4 seed.
- Needs community guide or game-test validation before being treated as stable.

## 清流

### MAA Facts

- Rarity: `4`; position: `RANGED`; profession: `MEDIC`; subProfessionId: `healer`

| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| `单奶` | 688 | 200 | 588 | 500 | 2 | True | True | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` |
| `奶` | 0 | 0 | -100 | 300 |  | False | False | 0 | `[]` |

### Functional Mapping

| Functional Role | Weight | Evidence status |
| --- | ---: | --- |
| `healing` | 0.8 | seed hypothesis with recorded evidence |
| `sustain` | 0.6 | seed hypothesis with recorded evidence |
| `ranged` | 0.2 | seed hypothesis with recorded evidence |

### Interpretation

- Current MAA classification: `单奶, 奶`.
- Functional profile confidence: `medium`.
- Evidence: MAA official: Groups: 单奶, 奶; manual strategy: Phase 4 seed.
- Needs community guide or game-test validation before being treated as stable.

## 罗小黑

### MAA Facts

- Rarity: `4`; position: `MELEE`; profession: `WARRIOR`; subProfessionId: `lord`

| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |
| `地面阻挡` | 688 | 200 | 588 | 500 | 1 | True | True | 0 | `[]` |

### Functional Mapping

| Functional Role | Weight | Evidence status |
| --- | ---: | --- |
| `ground` | 0.7 | seed hypothesis with recorded evidence |
| `block` | 0.4 | seed hypothesis with recorded evidence |
| `utility` | 0.3 | seed hypothesis with recorded evidence |

### Interpretation

- Current MAA classification: `地面阻挡`.
- Functional profile confidence: `low`.
- Evidence: MAA official: Group: 地面阻挡; manual strategy: Phase 4 seed.
- Needs community guide or game-test validation before being treated as stable.
