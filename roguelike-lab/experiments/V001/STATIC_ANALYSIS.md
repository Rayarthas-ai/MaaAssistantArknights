# JieGarden Recruitment Baseline

Source: `roguelike-lab\experiments\V001\recruitment.json`
Theme: `JieGarden`

## Human Strategy Summary

The official JieGarden recruitment strategy is a rule-and-score table. It first protects opening operators through `is_start`, then protects team structure through `is_key` and `team_complete_condition`. Candidate operators are scored by `recruit_priority` for new recruitment and `promote_priority` for promotion. Team composition and some collectibles can adjust those scores through offsets.

### Opening Core Operators

Operators marked `is_start=true`, sorted by recruitment priority:

| Operator | Group | Recruit | Promote |
| --- | --- | ---: | ---: |
| 电弧 | 电弧 | 999 | 999 |
| 予愿安洁莉娜 | 玛恩纳 | 998 | 1000 |
| 维什戴尔 | 益达 | 998 | 1000 |
| 新约能天使 | 新能 | 997 | 999 |
| 圣聆初雪 | 术师 | 900 | 950 |
| 蕾缪安 | 提丰 | 850 | 900 |
| 丰川祥子 | 近卫 | 822 | 960 |
| 怒潮凛冬 | 近卫 | 821 | 801 |
| 百炼嘉维尔 | 近卫 | 820 | 801 |
| 乌尔比安 | 近卫 | 801 | 801 |
| 斩业星熊 | 重装 | 800 | 900 |
| 佩佩 | 近卫 | 800 | 801 |
| 休谟斯 | 近卫 | 730 | 400 |
| 羽毛笔 | 近卫 | 720 | 500 |
| 仇白 | 近卫 | 705 | 840 |
| 山 | 近卫 | 700 | 610 |
| 清流 | 单奶 | 688 | 200 |
| 罗小黑 | 地面阻挡 | 688 | 200 |
| 苏苏洛 | 单奶 | 680 | 250 |
| 梅 | 速狙 | 679 | 0 |
| 跃跃 | 高台输出 | 679 | 0 |
| 流星 | 速狙 | 678 | 200 |
| 白雪 | 狙击 | 678 | 200 |
| 铅踝 | 狙击 | 678 | 200 |
| 克洛丝 | 速狙 | 678 | 0 |
| 风丸 | 近卫 | 670 | 400 |
| 海沫 | 近卫 | 650 | 500 |
| 嘉维尔 | 单奶 | 640 | 0 |
| 安赛尔 | 单奶 | 635 | 0 |
| 圣约送葬人 | 近卫 | 630 | 700 |
| 古米 | 重装 | 626 | 790 |
| 令 | 召唤 | 620 | 801 |
| 号角 | 重装 | 619 | 700 |
| 石棉 | 重装 | 615 | 400 |
| 讯使 | 挡人先锋 | 611 | 0 |
| 煌 | 近卫 | 610 | 790 |
| 帕拉斯 | 近卫 | 610 | 350 |
| 凯尔希 | 凯尔希 | 600 | 810 |
| 斑点 | 重装 | 600 | 0 |
| 锏 | 近卫 | 570 | 997 |
| 芬 | 挡人先锋 | 551 | 0 |
| 林 | 盾法 | 526 | 750 |
| 艾丽妮 | 近卫 | 520 | 655 |
| 假日威龙陈 | 水陈 | 510 | 940 |
| 银灰 | 玛恩纳 | 510 | 870 |
| 稀音 | 召唤 | 500 | 150 |
| 芳汀 | 其他地面 | 468 | 0 |
| 伊桑 | 地刺 | 405 | 405 |
| 提丰 | 提丰 | 370 | 510 |

### Team Core Operators

Operators marked `is_key=true`, sorted by recruitment priority:

| Operator | Group | Recruit | Promote |
| --- | --- | ---: | ---: |
| 电弧 | 电弧 | 999 | 999 |
| 予愿安洁莉娜 | 玛恩纳 | 998 | 1000 |
| 维什戴尔 | 益达 | 998 | 1000 |
| 新约能天使 | 新能 | 997 | 999 |
| 司霆惊蛰 | 玛恩纳 | 996 | 1000 |
| 玛恩纳 | 玛恩纳 | 995 | 999 |
| 酒神 | 元素 | 905 | 950 |
| 凛御银灰 | 伊内丝 | 900 | 950 |
| 圣聆初雪 | 术师 | 900 | 950 |
| 蕾缪安 | 提丰 | 850 | 900 |
| Touch | 单奶 | 843 | 550 |
| 丰川祥子 | 近卫 | 822 | 960 |
| 怒潮凛冬 | 近卫 | 821 | 801 |
| 百炼嘉维尔 | 近卫 | 820 | 801 |
| 伊内丝 | 伊内丝 | 819 | 930 |
| 郁金香 | 挡人先锋 | 807 | 550 |
| 乌尔比安 | 近卫 | 801 | 801 |
| 斩业星熊 | 重装 | 800 | 900 |
| 纯烬艾雅法拉 | 单奶 | 799 | 601 |
| 遥 | 群奶 | 750 | 650 |
| 凯尔希·思衡托 | 群奶 | 748 | 648 |
| 休谟斯 | 近卫 | 730 | 400 |
| 仇白 | 近卫 | 705 | 840 |
| 荒芜拉普兰德 | 术师 | 700 | 900 |
| 澄闪 | 术师 | 695 | 841 |
| 逻各斯 | 术师 | 692 | 841 |
| 清流 | 单奶 | 688 | 200 |
| 罗小黑 | 地面阻挡 | 688 | 200 |
| 艾拉 | 速狙 | 682 | 801 |
| Stormeye | 速狙 | 681 | 200 |
| 苏苏洛 | 单奶 | 680 | 250 |
| 梅 | 速狙 | 679 | 0 |
| 跃跃 | 高台输出 | 679 | 0 |
| 流星 | 速狙 | 678 | 200 |
| 白雪 | 狙击 | 678 | 200 |
| 铅踝 | 狙击 | 678 | 200 |
| 克洛丝 | 速狙 | 678 | 0 |
| 晓歌 | 情报官 | 677 | 630 |
| 蜜莓 | 单奶 | 641 | 300 |
| 艾雅法拉 | 术师 | 640 | 801 |
| 嘉维尔 | 单奶 | 640 | 0 |
| 妮芙 | 术师 | 639 | 801 |
| 安赛尔 | 单奶 | 635 | 0 |
| 芙蓉 | 单奶 | 634 | 0 |
| 黍 | 重装 | 627 | 690 |
| 古米 | 重装 | 626 | 790 |
| 塞雷娅 | 重装 | 624 | 650 |
| 蛇屠箱 | 重装 | 622 | 620 |
| 余 | 重装 | 620 | 650 |
| 珊比 | 重装 | 620 | 650 |
| 号角 | 重装 | 619 | 700 |
| 讯使 | 挡人先锋 | 611 | 0 |
| 清道夫 | 挡人先锋 | 610 | 0 |
| 泡泡 | 重装 | 605 | 400 |
| 凯尔希 | 凯尔希 | 600 | 810 |
| 卡缇 | 重装 | 600 | 0 |
| 斑点 | 重装 | 600 | 0 |
| 娜仁图亚 | 速狙 | 581 | 500 |
| 能天使 | 速狙 | 580 | 500 |
| 桃金娘 | 投锋 | 580 | 380 |
| 锏 | 近卫 | 570 | 997 |
| 米格鲁 | 重装 | 568 | 0 |
| 卡达 | 术师 | 563 | 0 |
| 史都华德 | 术师 | 562 | 0 |
| 芬 | 挡人先锋 | 551 | 0 |
| 香草 | 挡人先锋 | 550 | 0 |
| 林 | 盾法 | 526 | 750 |
| 灵知 | 辅助 | 526 | 602 |
| 假日威龙陈 | 水陈 | 510 | 940 |
| 银灰 | 玛恩纳 | 510 | 870 |
| 铃兰 | 辅助 | 486 | 612 |
| 空弦 | 速狙 | 478 | 900 |
| 石英 | 地面阻挡 | 467 | 0 |
| 月见夜 | 其他地面 | 466 | 0 |
| 泡普卡 | 其他地面 | 460 | 0 |
| 安德切尔 | 其他高台 | 455 | 0 |
| 溯光星源 | 辅助 | 450 | 600 |
| 波登可 | 群奶 | 440 | 0 |
| 深海色 | 召唤 | 424 | 0 |
| 罗比菈塔 | 地面阻挡 | 424 | 0 |
| 梓兰 | 辅助 | 423 | 0 |
| 末药 | 单奶 | 406 | 0 |
| 伊桑 | 地刺 | 405 | 405 |
| 砾 | 炮灰 | 385 | 300 |
| 提丰 | 提丰 | 370 | 510 |
| 异客 | 术师 | 359 | 780 |
| 夜刀 | 其他地面 | 310 | 0 |
| 炎熔 | 其他高台 | 206 | 0 |
| 空爆 | 其他高台 | 206 | 0 |

### Team Complete Conditions

1. At least `2` unique operator(s) from groups: `益达`, `玛恩纳`, `新能`
2. At least `2` unique operator(s) from groups: `重装`, `近卫`, `召唤`, `凯尔希`
3. At least `1` unique operator(s) from groups: `焰苇`, `单奶`, `群奶`
4. At least `1` unique operator(s) from groups: `回费`

Interpretation:

- The first condition demands two high-value carry/core-output groups.
- The second condition demands two ground/blocking or summon/Kal'tsit-style stabilizers.
- The third condition demands at least one healing lane.
- The fourth condition demands at least one DP/cost-recovery group.

### Mutual Exclusion And Downranking

Negative `recruit_priority_offsets` are the main JSON mechanism for avoiding over-recruiting similar roles. The most common pattern is: once a referenced group is already present, reduce the score of another operator in the same strategic lane.

- `酒神` in `元素` has negative recruitment offsets: `[{"groups": ["元素"], "threshold": 1, "offset": -200}]`
- `塑心` in `元素` has negative recruitment offsets: `[{"groups": ["元素"], "threshold": 1, "offset": -200}]`
- `波卜` in `元素` has negative recruitment offsets: `[{"groups": ["元素"], "threshold": 1, "offset": -200}]`
- `凛视` in `元素` has negative recruitment offsets: `[{"groups": ["元素"], "threshold": 1, "offset": -200}]`
- `凯尔希` in `凯尔希` has negative recruitment offsets: `[{"groups": ["地面阻挡", "焰苇", "玛恩纳"], "threshold": 3, "offset": -200, "doc": "地面和高台输出均完备时，凯尔希的招募优先级-200"}, {"groups": ["单奶", "群奶"], "threshold": 2, "offset": -100}]`
- `司霆惊蛰` in `玛恩纳` has negative recruitment offsets: `[{"groups": ["凯尔希", "召唤", "地面阻挡"], "is_less": true, "offset": -200, "doc": "地面阻挡<1时，司霆惊蛰的招募优先级-200"}]`
- `玛恩纳` in `玛恩纳` has negative recruitment offsets: `[{"groups": ["凯尔希", "召唤", "地面阻挡"], "is_less": true, "offset": -200, "doc": "地面阻挡<1时，玛恩纳的招募优先级-200"}]`
- `银灰` in `玛恩纳` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫"], "threshold": 2, "offset": -200}]`
- `凛御银灰` in `伊内丝` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 3, "offset": -100}]`
- `伊内丝` in `伊内丝` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 3, "offset": -100}]`
- `假日威龙陈` in `水陈` has negative recruitment offsets: `[{"groups": ["益达"], "threshold": 1, "offset": -230}]`
- `赤刃明霄陈` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `圣约送葬人` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `隐德来希` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `怒潮凛冬` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `百炼嘉维尔` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `锏` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 3, "offset": -150}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `佩佩` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `乌尔比安` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `海沫` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `丰川祥子` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `山` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -500}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `贝洛内` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -500}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `羽毛笔` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `休谟斯` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -500}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `仇白` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 3, "offset": -150}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `棘刺` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `煌` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -200}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `维娜·维多利亚` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装", "召唤", "近卫", "情报官", "挡人先锋", "其他地面"], "is_less": true, "threshold": 2, "offset": -350, "doc": "地面阻挡≤2时，维娜·维多利亚的招募优先级-350"}, {"groups": ["凯尔希", "玛恩纳"], "threshold": 1, "offset": -200, "doc": "玛恩纳或凯尔希在队伍中时，维娜·维多利亚的招募优先级-200"}]`
- `艾丽妮` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `帕拉斯` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `医生` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `风丸` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `幽灵鲨` in `近卫` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 2, "offset": -180}, {"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -300, "doc": "地面阻挡≤1时，幽灵鲨的招募优先级-300"}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]`
- `黍` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]`
- `塞雷娅` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]`
- `余` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]`
- `珊比` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]`
- `临光` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装", "近卫"], "threshold": 2, "offset": -200}]`
- `深律` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装", "近卫"], "threshold": 2, "offset": -200}]`
- `号角` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]`
- `星熊` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]`
- `年` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -200}]`
- `机械师` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]`
- `涤火杰西卡` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]`
- `信仰搅拌机` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]`
- `雷蛇` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]`
- `深巡` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]`
- `瑕光` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]`
- `蛇屠箱` in `重装` has negative recruitment offsets: `[{"groups": ["重装", "凯尔希"], "threshold": 2, "offset": -300}]`
- `泡泡` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]`
- `古米` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装", "近卫"], "threshold": 2, "offset": -300}]`
- `泥岩` in `重装` has negative recruitment offsets: `[{"groups": ["重装", "凯尔希", "近卫"], "threshold": 2, "offset": -200}]`
- `斥罪` in `重装` has negative recruitment offsets: `[{"groups": ["重装", "凯尔希", "近卫"], "threshold": 2, "offset": -200}]`
- `石棉` in `重装` has negative recruitment offsets: `[{"groups": ["重装", "凯尔希", "近卫"], "threshold": 2, "offset": -200}]`
- `卡缇` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 1, "offset": -300}]`
- `米格鲁` in `重装` has negative recruitment offsets: `[{"groups": ["重装"], "threshold": 1, "offset": -100}]`
- `预备干员-重装` in `重装` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装"], "threshold": 1, "offset": -140}]`
- `艾拉` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -200}, {"groups": ["凯尔希", "近卫", "重装"], "is_less": true, "threshold": 1, "offset": -300}]`
- `莱伊` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `娜仁图亚` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `能天使` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `灰烬` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `空弦` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `寒芒克洛丝` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `隐现` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `蓝毒` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]`
- `梅` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙"], "threshold": 1, "offset": -300}]`
- `克洛丝` in `速狙` has negative recruitment offsets: `[{"groups": ["水陈", "速狙"], "threshold": 1, "offset": -300}]`
- `令` in `召唤` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "重装", "召唤"], "threshold": 1, "offset": -300}]`
- `稀音` in `召唤` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "重装", "召唤"], "threshold": 1, "offset": -300}]`
- `梅尔` in `召唤` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "重装", "召唤"], "threshold": 1, "offset": -300}]`
- `深海色` in `召唤` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫"], "threshold": 1, "offset": -300}]`
- `纯烬艾雅法拉` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `蜜莓` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `桑葚` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `哈洛德` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `褐果` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `Touch` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -200}]`
- `流明` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `絮雨` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `赫默` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `华法琳` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `苏苏洛` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `嘉维尔` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `清流` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `安赛尔` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `芙蓉` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `预备干员-后勤` in `单奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 1, "offset": -300}]`
- `史尔特尔` in `史尔特尔` has negative recruitment offsets: `[{"groups": ["凯尔希", "重装", "召唤", "近卫", "情报官", "挡人先锋", "其他地面"], "is_less": true, "threshold": 2, "offset": -350, "doc": "地面阻挡≤2时，史尔特尔的招募优先级-350"}]`
- `缄默德克萨斯` in `处决者` has negative recruitment offsets: `[{"groups": ["处决者", "史尔特尔"], "threshold": 2, "offset": -200}]`
- `麒麟R夜刀` in `处决者` has negative recruitment offsets: `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -300}]`
- `耀骑士临光` in `处决者` has negative recruitment offsets: `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -200}, {"groups": ["凯尔希", "重装", "召唤", "近卫", "情报官", "挡人先锋", "其他地面"], "is_less": true, "threshold": 1, "offset": -350, "doc": "地面阻挡≤1时，临光的招募优先级-350"}]`
- `傀影` in `处决者` has negative recruitment offsets: `[{"groups": ["处决者", "史尔特尔"], "threshold": 2, "offset": -200}]`
- `弑君者` in `处决者` has negative recruitment offsets: `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -200}]`
- `红` in `处决者` has negative recruitment offsets: `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -200}]`
- `风笛` in `其他地面` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]`
- `历阵锐枪芬` in `其他地面` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]`
- `浊心斯卡蒂` in `浊心斯卡蒂` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -180}, {"groups": ["浊心斯卡蒂"], "threshold": 1, "offset": -580}]`
- `魔王` in `浊心斯卡蒂` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -280}, {"groups": ["浊心斯卡蒂"], "threshold": 1, "offset": -580}]`
- `遥` in `群奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `凯尔希·思衡托` in `群奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -200}]`
- `夜莺` in `群奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -200}]`
- `白面鸮` in `群奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `调香师` in `群奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `微风` in `群奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `明椒` in `群奶` has negative recruitment offsets: `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]`
- `琴柳` in `投锋` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}]`
- `极境` in `投锋` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}]`
- `万顷` in `投锋` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}]`
- `桃金娘` in `投锋` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}]`
- `忍冬` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `推进之王` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `嵯峨` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `焰尾` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `德克萨斯` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `青枳` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `讯使` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `清道夫` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]`
- `芬` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]`
- `香草` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]`
- `翎羽` in `挡人先锋` has negative recruitment offsets: `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]`
- `晓歌` in `情报官` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}]`
- `寻澜` in `情报官` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}]`
- `齐尔查克` in `情报官` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}]`
- `谜图` in `情报官` has negative recruitment offsets: `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}]`
- `荒芜拉普兰德` in `术师` has negative recruitment offsets: `[{"groups": ["术师"], "threshold": 1, "offset": -120}]`
- `澄闪` in `术师` has negative recruitment offsets: `[{"groups": ["术师"], "threshold": 1, "offset": -120}]`
- `艾雅法拉` in `术师` has negative recruitment offsets: `[{"groups": ["术师"], "threshold": 1, "offset": -120}]`
- `妮芙` in `术师` has negative recruitment offsets: `[{"groups": ["术师"], "threshold": 1, "offset": -120}]`
- `烛煌` in `术师` has negative recruitment offsets: `[{"groups": ["术师"], "threshold": 1, "offset": -120}]`
- `莫斯提马` in `术师` has negative recruitment offsets: `[{"groups": ["术师"], "threshold": 2, "offset": -120}]`
- `林` in `盾法` has negative recruitment offsets: `[{"groups": ["术师"], "threshold": 1, "offset": -130}]`
- `蕾缪安` in `提丰` has negative recruitment offsets: `[{"groups": ["益达"], "threshold": 1, "offset": -200}]`
- `提丰` in `提丰` has negative recruitment offsets: `[{"groups": ["益达"], "threshold": 1, "offset": -230}]`
- `铅踝` in `狙击` has negative recruitment offsets: `[{"groups": ["益达"], "threshold": 1, "offset": -10}]`
- `白雪` in `狙击` has negative recruitment offsets: `[{"groups": ["狙击", "水陈"], "threshold": 1, "offset": -200}]`
- `跃跃` in `高台输出` has negative recruitment offsets: `[{"groups": ["水陈", "速狙"], "threshold": 1, "offset": -300}]`
- `归溟幽灵鲨` in `地刺` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 2, "offset": -350}, {"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -600, "doc": "地面阻挡≤1时，招募优先级-500"}]`
- `阿` in `其他高台` has negative recruitment offsets: `[{"groups": ["奶"], "is_less": true, "threshold": 1, "offset": -300}]`
- `阿斯卡纶` in `地刺` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -500}]`
- `水月` in `地刺` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -600}]`
- `狮蝎` in `地刺` has negative recruitment offsets: `[{"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -600}]`
- `孑` in `其他地面` has negative recruitment offsets: `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]`
- `琳琅诗怀雅` in `其他地面` has negative recruitment offsets: `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]`
- `老鲤` in `其他地面` has negative recruitment offsets: `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]`
- `乌有` in `其他地面` has negative recruitment offsets: `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]`
- `焰狐龙梓兰` in `其他高台` has negative recruitment offsets: `[{"groups": ["狙击", "水陈"], "threshold": 1, "offset": -200}]`
- `松果` in `其他高台` has negative recruitment offsets: `[{"groups": ["狙击", "水陈"], "threshold": 1, "offset": -200}]`

### Conditional Upweighting

Positive `recruit_priority_offsets` raise priority when a team need is still missing or a condition is met.

- `凯尔希` in `凯尔希` has positive recruitment offsets: `[{"groups": ["地面阻挡", "召唤"], "is_less": true, "threshold": 1, "offset": 100, "doc": "地面阻挡输出位≤1时，凯尔希的招募优先级+100"}, {"groups": ["单奶", "群奶"], "is_less": true, "threshold": 1, "offset": 105, "doc": "治疗位≤1时，凯尔希的招募优先级+105"}]`
- `黍` in `重装` has positive recruitment offsets: `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}]`
- `塞雷娅` in `重装` has positive recruitment offsets: `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}]`
- `临光` in `重装` has positive recruitment offsets: `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}]`
- `深律` in `重装` has positive recruitment offsets: `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}]`
- `古米` in `重装` has positive recruitment offsets: `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}]`
- `斑点` in `重装` has positive recruitment offsets: `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}]`
- `流星` in `速狙` has positive recruitment offsets: `[{"groups": ["益达"], "threshold": 1, "offset": 10}]`
- `白面鸮` in `群奶` has positive recruitment offsets: `[{"groups": ["益达"], "threshold": 1, "offset": 250}]`
- `夏栎` in `群奶` has positive recruitment offsets: `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 500}]`
- `波登可` in `群奶` has positive recruitment offsets: `[{"groups": ["单奶", "群奶", "凯尔希"], "is_less": true, "offset": 100}]`
- `万顷` in `投锋` has positive recruitment offsets: `[{"groups": ["提丰", "水陈", "速狙"], "threshold": 2, "offset": 50}]`
- `晓歌` in `情报官` has positive recruitment offsets: `[{"groups": ["新能"], "threshold": 1, "offset": 150}]`
- `铃兰` in `辅助` has positive recruitment offsets: `[{"groups": ["术师"], "threshold": 2, "offset": 80}]`
- `溯光星源` in `辅助` has positive recruitment offsets: `[{"groups": ["术师"], "threshold": 2, "offset": 80}]`
- `可露希尔` in `其他高台` has positive recruitment offsets: `[{"groups": ["回费"], "is_less": true, "offset": 150, "doc": "回费干员≤0时，优先级+150"}]`
- `缪尔赛思` in `其他高台` has positive recruitment offsets: `[{"groups": ["回费"], "is_less": true, "offset": 150, "doc": "回费干员≤0时，优先级+150"}]`
- `夜半` in `其他高台` has positive recruitment offsets: `[{"groups": ["回费"], "is_less": true, "offset": 150, "doc": "回费干员≤0时，优先级+150"}]`
- `渡桥` in `其他高台` has positive recruitment offsets: `[{"groups": ["回费"], "is_less": true, "offset": 150}]`
- `豆苗` in `其他高台` has positive recruitment offsets: `[{"groups": ["回费"], "is_less": true, "offset": 150}]`

### Collectible-Driven Priority

- `银灰` in `玛恩纳` changes priority from collectibles: `[{"collection": "折戟-浴血", "offset": 120}]`
- `乌尔比安` in `近卫` changes priority from collectibles: `[{"collection": "折戟-浴血", "offset": 220}]`
- `仇白` in `近卫` changes priority from collectibles: `[{"collection": "折戟-浴血", "offset": 120}]`
- `维娜·维多利亚` in `近卫` changes priority from collectibles: `[{"collection": "“文明的存续”", "offset": 120}]`
- `荒芜拉普兰德` in `术师` changes priority from collectibles: `[{"collection": "波纹之手", "offset": 300}]`
- `澄闪` in `术师` changes priority from collectibles: `[{"collection": "波纹之手", "offset": 300}]`
- `异客` in `术师` changes priority from collectibles: `[{"collection": "波纹之手", "offset": 638}]`
- `莫斯提马` in `术师` changes priority from collectibles: `[{"collection": "波纹之手", "offset": 200}]`

## Operator Groups

### 益达

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 维什戴尔 | 998 | 1000 | 898 | 1300 | True | True | False | 3 | 2 | 0 | `[]` | `[]` |

### 新能

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 新约能天使 | 997 | 999 | 897 | 1299 | True | True | False | 2 |  | 0 | `[]` | `[]` |

### 电弧

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 电弧 | 999 | 999 | 899 | 1299 | True | True | False | 2 |  | 0 | `[]` | `[]` |

### 元素

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 酒神 | 905 | 950 | 805 | 1250 | False | True | False | 2 |  | 0 | `[{"groups": ["元素"], "threshold": 1, "offset": -200}]` | `[]` |
| 塑心 | 705 | 702 | 605 | 1002 | False | False | False | 3 | 1 | 0 | `[{"groups": ["元素"], "threshold": 1, "offset": -200}]` | `[]` |
| 波卜 | 258 | 401 | 158 | 701 | False | False | False | 1 |  | 0 | `[{"groups": ["元素"], "threshold": 1, "offset": -200}]` | `[]` |
| 凛视 | 257 | 400 | 157 | 700 | False | False | False | 2 |  | 0 | `[{"groups": ["元素"], "threshold": 1, "offset": -200}]` | `[]` |

### 凯尔希

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 凯尔希 | 600 | 810 | 500 | 1110 | True | True | False | 3 | 2 | 0 | `[{"groups": ["地面阻挡", "召唤"], "is_less": true, "threshold": 1, "offset": 100, "doc": "地面阻挡输出位≤1时，凯尔希的招募优先级+100"}, {"groups": ["单奶", "群奶"], "is_less": true, "threshold": 1, "offset": 105, "doc": "治疗位≤1时，凯尔希的招募优先级+105"}, {"groups": ["地面阻挡", "焰苇", "玛恩纳"], "threshold": 3, "offset": -200, "doc": "地面和高台输出均完备时，凯尔希的招募优先级-200"}, {"groups": ["单奶", "群奶"], "threshold": 2, "offset": -100}]` | `[]` |

### 玛恩纳

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 予愿安洁莉娜 | 998 | 1000 | 898 | 1300 | True | True | False | 3 | 2 | 0 | `[]` | `[]` |
| 司霆惊蛰 | 996 | 1000 | 896 | 1300 | False | True | False | 2 |  | 0 | `[{"groups": ["凯尔希", "召唤", "地面阻挡"], "is_less": true, "offset": -200, "doc": "地面阻挡<1时，司霆惊蛰的招募优先级-200"}]` | `[]` |
| 玛恩纳 | 995 | 999 | 895 | 1299 | False | True | False | 3 | 2 | 0 | `[{"groups": ["凯尔希", "召唤", "地面阻挡"], "is_less": true, "offset": -200, "doc": "地面阻挡<1时，玛恩纳的招募优先级-200"}]` | `[]` |
| 银灰 | 510 | 870 | 410 | 1170 | True | True | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "近卫"], "threshold": 2, "offset": -200}]` | `[{"collection": "折戟-浴血", "offset": 120}]` |
| 龙舌兰 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 聘风 | 0 | 300 | -100 | 600 | False | False | False | 2 |  | 0 | `[]` | `[]` |

### 伊内丝

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 凛御银灰 | 900 | 950 | 800 | 1250 | False | True | False | 3 | 1 | 0 | `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 3, "offset": -100}]` | `[]` |
| 伊内丝 | 819 | 930 | 719 | 1230 | False | True | False | 2 |  | 0 | `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 3, "offset": -100}]` | `[]` |

### 水陈

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 假日威龙陈 | 510 | 940 | 410 | 1240 | True | True | False | 3 | 1 | 0 | `[{"groups": ["益达"], "threshold": 1, "offset": -230}]` | `[]` |

### 近卫

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 赤刃明霄陈 | 711 | 800 | 611 | 1100 | False | False | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 圣约送葬人 | 630 | 700 | 530 | 1000 | True | False | False | 3 | 2 | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 隐德来希 | 600 | 700 | 500 | 1000 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 怒潮凛冬 | 821 | 801 | 721 | 1101 | True | True | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 百炼嘉维尔 | 820 | 801 | 720 | 1101 | True | True | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 锏 | 570 | 997 | 470 | 1297 | True | True | False | 3 | 2 | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 3, "offset": -150}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 佩佩 | 800 | 801 | 700 | 1101 | True | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 乌尔比安 | 801 | 801 | 701 | 1101 | True | True | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -210}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[{"collection": "折戟-浴血", "offset": 220}]` |
| 海沫 | 650 | 500 | 550 | 800 | True | False | False | 1 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 丰川祥子 | 822 | 960 | 722 | 1260 | True | True | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 山 | 700 | 610 | 600 | 910 | True | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -500}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 贝洛内 | 699 | 610 | 599 | 910 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -500}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 羽毛笔 | 720 | 500 | 620 | 800 | True | False | False | 1 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 休谟斯 | 730 | 400 | 630 | 700 | True | True | False | 1 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -500}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 仇白 | 705 | 840 | 605 | 1140 | True | True | False | 3 | 2 | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 3, "offset": -150}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[{"collection": "折戟-浴血", "offset": 120}]` |
| 棘刺 | 605 | 950 | 505 | 1250 | False | False | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -300}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 煌 | 610 | 790 | 510 | 1090 | True | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -200}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 维娜·维多利亚 | 600 | 750 | 500 | 1050 | False | False | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "重装", "召唤", "近卫", "情报官", "挡人先锋", "其他地面"], "is_less": true, "threshold": 2, "offset": -350, "doc": "地面阻挡≤2时，维娜·维多利亚的招募优先级-350"}, {"groups": ["凯尔希", "玛恩纳"], "threshold": 1, "offset": -200, "doc": "玛恩纳或凯尔希在队伍中时，维娜·维多利亚的招募优先级-200"}]` | `[{"collection": "“文明的存续”", "offset": 120}]` |
| 艾丽妮 | 520 | 655 | 420 | 955 | True | False | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 帕拉斯 | 610 | 350 | 510 | 650 | True | False | False | 1 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 医生 | 600 | 350 | 500 | 650 | False | False | False |  |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 风丸 | 670 | 400 | 570 | 700 | True | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤", "重装"], "threshold": 1, "offset": -400}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |
| 幽灵鲨 | 620 | 350 | 520 | 650 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 2, "offset": -180}, {"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -300, "doc": "地面阻挡≤1时，幽灵鲨的招募优先级-300"}, {"groups": ["元素奶"], "is_less": true, "threshold": 1, "offset": -80}]` | `[]` |

### 重装

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 斩业星熊 | 800 | 900 | 700 | 1200 | True | True | False | 2 |  | 0 | `[]` | `[]` |
| 黍 | 627 | 690 | 527 | 990 | False | True | False | 3 | 1 | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}, {"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]` | `[]` |
| 塞雷娅 | 624 | 650 | 524 | 950 | False | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}, {"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]` | `[]` |
| 余 | 620 | 650 | 520 | 950 | False | True | False | 2 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]` | `[]` |
| 珊比 | 620 | 650 | 520 | 950 | False | True | False | 3 | 2 | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]` | `[]` |
| 临光 | 613 | 490 | 513 | 790 | False | False | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}, {"groups": ["凯尔希", "重装", "近卫"], "threshold": 2, "offset": -200}]` | `[]` |
| 深律 | 612 | 490 | 512 | 790 | False | False | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}, {"groups": ["凯尔希", "重装", "近卫"], "threshold": 2, "offset": -200}]` | `[]` |
| 号角 | 619 | 700 | 519 | 1000 | True | True | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]` | `[]` |
| 星熊 | 611 | 650 | 511 | 950 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]` | `[]` |
| 年 | 623 | 615 | 523 | 915 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -200}]` | `[]` |
| 机械师 | 630 | 650 | 530 | 950 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]` | `[]` |
| 涤火杰西卡 | 622 | 650 | 522 | 950 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]` | `[]` |
| 信仰搅拌机 | 620 | 650 | 520 | 950 | False | False | False | 3 | 2 | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -120}]` | `[]` |
| 雷蛇 | 613 | 350 | 513 | 650 | False | False | False | 1 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]` | `[]` |
| 深巡 | 612 | 350 | 512 | 650 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]` | `[]` |
| 瑕光 | 607 | 570 | 507 | 870 | False | False | False | 1 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]` | `[]` |
| 蛇屠箱 | 622 | 620 | 522 | 920 | False | True | False | 2 |  | 0 | `[{"groups": ["重装", "凯尔希"], "threshold": 2, "offset": -300}]` | `[]` |
| 泡泡 | 605 | 400 | 505 | 700 | False | True | False | 2 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 2, "offset": -300}]` | `[]` |
| 古米 | 626 | 790 | 526 | 1090 | True | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}, {"groups": ["凯尔希", "重装", "近卫"], "threshold": 2, "offset": -300}]` | `[]` |
| 泥岩 | 560 | 590 | 460 | 890 | False | False | False | 2 |  | 0 | `[{"groups": ["重装", "凯尔希", "近卫"], "threshold": 2, "offset": -200}]` | `[]` |
| 斥罪 | 561 | 591 | 461 | 891 | False | False | False | 2 |  | 0 | `[{"groups": ["重装", "凯尔希", "近卫"], "threshold": 2, "offset": -200}]` | `[]` |
| 石棉 | 615 | 400 | 515 | 700 | True | False | False | 2 |  | 0 | `[{"groups": ["重装", "凯尔希", "近卫"], "threshold": 2, "offset": -200}]` | `[]` |
| 暮落 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 车尔尼 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 可颂 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 拜松 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 闪击 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 吽 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 暴雨 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 角峰 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 坚雷 | 0 | 350 | -100 | 650 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 斑点 | 600 | 0 | 500 | 300 | True | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 120}]` | `[]` |
| 卡缇 | 600 | 0 | 500 | 300 | False | True | False | 1 |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 1, "offset": -300}]` | `[]` |
| 米格鲁 | 568 | 0 | 468 | 300 | False | True | False | 1 |  | 0 | `[{"groups": ["重装"], "threshold": 1, "offset": -100}]` | `[]` |
| 预备干员-重装 | 460 | 0 | 360 | 300 | False | False | True |  |  | 0 | `[{"groups": ["凯尔希", "重装"], "threshold": 1, "offset": -140}]` | `[]` |

### 速狙

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 新约能天使 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 艾拉 | 682 | 801 | 582 | 1101 | False | True | False | 3 | 2 | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -200}, {"groups": ["凯尔希", "近卫", "重装"], "is_less": true, "threshold": 1, "offset": -300}]` | `[]` |
| 莱伊 | 481 | 701 | 381 | 1001 | False | False | False | 3 | 2 | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| 娜仁图亚 | 581 | 500 | 481 | 800 | False | True | False | 1 |  | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| 能天使 | 580 | 500 | 480 | 800 | False | True | False | 3 | 2 | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| Stormeye | 681 | 200 | 581 | 500 | False | True | False | 1 |  | 0 | `[]` | `[]` |
| 灰烬 | 477 | 420 | 377 | 720 | False | False | False | 2 |  | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| 空弦 | 478 | 900 | 378 | 1200 | False | True | False | 3 | 1 | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| 寒芒克洛丝 | 678 | 420 | 578 | 720 | False | False | False | 2 |  | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| 隐现 | 456 | 400 | 356 | 700 | False | False | False | 1 |  | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| 蓝毒 | 455 | 400 | 355 | 700 | False | False | False | 1 |  | 0 | `[{"groups": ["水陈", "速狙", "益达"], "threshold": 1, "offset": -300}]` | `[]` |
| 四月 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 13 | `[]` | `[]` |
| 灰喉 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 梅 | 679 | 0 | 579 | 300 | True | True | False | 1 |  | 0 | `[{"groups": ["水陈", "速狙"], "threshold": 1, "offset": -300}]` | `[]` |
| 流星 | 678 | 200 | 578 | 500 | True | True | False |  |  | 0 | `[{"groups": ["益达"], "threshold": 1, "offset": 10}]` | `[]` |
| 克洛丝 | 678 | 0 | 578 | 300 | True | True | False | 1 |  | 0 | `[{"groups": ["水陈", "速狙"], "threshold": 1, "offset": -300}]` | `[]` |
| 预备干员-狙击 | 205 | 0 | 0 | 300 | False | False | True |  |  | 0 | `[]` | `[]` |

### 召唤

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 电弧 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 令 | 620 | 801 | 520 | 1101 | True | False | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "近卫", "重装", "召唤"], "threshold": 1, "offset": -300}]` | `[]` |
| 稀音 | 500 | 150 | 400 | 450 | True | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "重装", "召唤"], "threshold": 1, "offset": -300}]` | `[]` |
| 梅尔 | 440 | 150 | 340 | 450 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "重装", "召唤"], "threshold": 1, "offset": -300}]` | `[]` |
| 深海色 | 424 | 0 | 324 | 300 | False | True | False | 1 |  | 0 | `[{"groups": ["凯尔希", "近卫"], "threshold": 1, "offset": -300}]` | `[]` |

### 元素奶

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 纯烬艾雅法拉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蜜莓 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 桑葚 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 哈洛德 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 褐果 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 单奶

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 纯烬艾雅法拉 | 799 | 601 | 699 | 901 | False | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 蜜莓 | 641 | 300 | 541 | 600 | False | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 桑葚 | 640 | 290 | 540 | 590 | False | False | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 哈洛德 | 639 | 290 | 539 | 590 | False | False | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| Touch | 843 | 550 | 743 | 850 | False | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -200}]` | `[]` |
| 流明 | 690 | 625 | 590 | 925 | False | False | False | 3 | 1 | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 絮雨 | 622 | 410 | 522 | 710 | False | False | False | 2 | 1 | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 闪灵 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 赫默 | 732 | 250 | 632 | 550 | False | False | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 华法琳 | 715 | 350 | 615 | 650 | False | False | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 图耶 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 亚叶 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 苏苏洛 | 680 | 250 | 580 | 550 | True | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 末药 | 406 | 0 | 306 | 300 | False | True | False |  |  | 0 | `[]` | `[]` |
| 嘉维尔 | 640 | 0 | 540 | 300 | True | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 褐果 | 687 | 200 | 587 | 500 | False | False | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 清流 | 688 | 200 | 588 | 500 | True | True | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 安赛尔 | 635 | 0 | 535 | 300 | True | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 芙蓉 | 634 | 0 | 534 | 300 | False | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 锡兰 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 预备干员-后勤 | 405 | 0 | 305 | 300 | False | False | True |  |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 1, "offset": -300}]` | `[]` |
| Lancet-2 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 史尔特尔

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 史尔特尔 | 670 | 910 | 570 | 1210 | False | False | False | 3 | 1 | 0 | `[{"groups": ["凯尔希", "重装", "召唤", "近卫", "情报官", "挡人先锋", "其他地面"], "is_less": true, "threshold": 2, "offset": -350, "doc": "地面阻挡≤2时，史尔特尔的招募优先级-350"}]` | `[]` |

### 处决者

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 本能的召唤 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 缄默德克萨斯 | 650 | 821 | 550 | 1121 | False | False | False | 3 | 2 | 8 | `[{"groups": ["处决者", "史尔特尔"], "threshold": 2, "offset": -200}]` | `[]` |
| 麒麟R夜刀 | 611 | 815 | 511 | 1115 | False | False | False | 2 |  | 6 | `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -300}]` | `[]` |
| 史尔特尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 耀骑士临光 | 570 | 720 | 470 | 1020 | False | False | False | 2 |  | 0 | `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -200}, {"groups": ["凯尔希", "重装", "召唤", "近卫", "情报官", "挡人先锋", "其他地面"], "is_less": true, "threshold": 1, "offset": -350, "doc": "地面阻挡≤1时，临光的招募优先级-350"}]` | `[]` |
| 傀影 | 501 | 555 | 401 | 855 | False | False | False | 2 |  | 15 | `[{"groups": ["处决者", "史尔特尔"], "threshold": 2, "offset": -200}]` | `[]` |
| 弑君者 | 500 | 550 | 400 | 850 | False | False | False | 3 | 2 | 16 | `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -200}]` | `[]` |
| 红 | 500 | 302 | 400 | 602 | False | False | False | 1 |  | 7 | `[{"groups": ["处决者", "史尔特尔"], "threshold": 1, "offset": -200}]` | `[]` |
| 斯卡蒂 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 15 | `[]` | `[]` |
| 宴 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 8 | `[]` | `[]` |
| 慕斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 15 | `[]` | `[]` |
| 摩根 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 9 | `[]` | `[]` |
| 止颂 | -800 | 0 | -900 | 300 | False | False | False | 2 |  | 12 | `[]` | `[]` |
| 风笛 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 历阵锐枪芬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 镜中虚影 | 0 | 0 | -100 | 300 | False | False | False |  |  | 8 | `[]` | `[]` |
| Mon3tr | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芙兰卡 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 20 | `[]` | `[]` |

### 浊心斯卡蒂

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 浊心斯卡蒂 | 727 | 740 | 627 | 1040 | False | False | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -180}, {"groups": ["浊心斯卡蒂"], "threshold": 1, "offset": -580}]` | `[]` |
| 魔王 | 630 | 690 | 530 | 990 | False | False | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -280}, {"groups": ["浊心斯卡蒂"], "threshold": 1, "offset": -580}]` | `[]` |

### 群奶

主要以攻击范围区分

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 遥 | 750 | 650 | 650 | 950 | False | True | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 凯尔希·思衡托 | 748 | 648 | 648 | 948 | False | True | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -200}]` | `[]` |
| 夜莺 | 708 | 677 | 608 | 977 | False | False | False | 3 | 2 | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 3, "offset": -200}]` | `[]` |
| 白面鸮 | 710 | 506 | 610 | 806 | False | False | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}, {"groups": ["益达"], "threshold": 1, "offset": 250}]` | `[]` |
| 调香师 | 688 | 200 | 588 | 500 | False | False | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 微风 | 687 | 200 | 587 | 500 | False | False | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 明椒 | 680 | 200 | 580 | 500 | False | False | False | 2 |  | 0 | `[{"groups": ["单奶", "群奶"], "threshold": 2, "offset": -300}]` | `[]` |
| 莎草 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 淬羽赫默 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 月禾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 九色鹿 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 夏栎 | 132 | 0 | 32 | 300 | False | False | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶"], "is_less": true, "offset": 500}]` | `[]` |
| 波登可 | 440 | 0 | 340 | 300 | False | True | False | 1 |  | 0 | `[{"groups": ["单奶", "群奶", "凯尔希"], "is_less": true, "offset": 100}]` | `[]` |
| 浊心斯卡蒂 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 魔王 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 海蒂 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 三角初华 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 空 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |

### 投锋

本次肉鸽开局压力较大,投锋优先度不高

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 琴柳 | 520 | 400 | 420 | 700 | False | False | False | 1 |  | 80 | `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}]` | `[]` |
| 极境 | 570 | 390 | 470 | 690 | False | False | False | 1 |  | 80 | `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}]` | `[]` |
| 万顷 | 569 | 390 | 469 | 690 | False | False | False | 1 |  | 80 | `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}, {"groups": ["提丰", "水陈", "速狙"], "threshold": 2, "offset": 50}]` | `[]` |
| 桃金娘 | 580 | 380 | 480 | 680 | False | True | False | 1 |  | 80 | `[{"groups": ["挡人先锋", "情报官"], "is_less": true, "threshold": 1, "offset": -400}, {"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -200}]` | `[]` |

### 挡人先锋

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 郁金香 | 807 | 550 | 707 | 850 | False | True | False | 1 |  | 0 | `[]` | `[]` |
| 忍冬 | 550 | 350 | 450 | 650 | False | False | False | 3 | 2 | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 推进之王 | 536 | 250 | 436 | 550 | False | False | False | 2 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 嵯峨 | 529 | 250 | 429 | 550 | False | False | False | 2 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 焰尾 | 528 | 250 | 428 | 550 | False | False | False | 2 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 德克萨斯 | 527 | 250 | 427 | 550 | False | False | False | 2 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 青枳 | 507 | 250 | 407 | 550 | False | False | False | 2 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 红隼 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 讯使 | 611 | 0 | 511 | 300 | True | True | False | 1 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 清道夫 | 610 | 0 | 510 | 300 | False | True | False | 1 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 2, "offset": -300}]` | `[]` |
| 贾维 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 凛冬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芬 | 551 | 0 | 451 | 300 | True | True | False | 1 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]` | `[]` |
| 香草 | 550 | 0 | 450 | 300 | False | True | False | 1 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]` | `[]` |
| 风笛 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 历阵锐枪芬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 苇草 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 野鬃 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 格拉尼 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 红豆 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 翎羽 | 310 | 0 | 210 | 300 | False | False | False | 1 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]` | `[]` |

### 情报官

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 凛御银灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 伊内丝 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 晓歌 | 677 | 630 | 577 | 930 | False | True | False | 2 |  | 80 | `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}, {"groups": ["新能"], "threshold": 1, "offset": 150}]` | `[]` |
| 寻澜 | 627 | 620 | 527 | 920 | False | False | False | 2 |  | 80 | `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}]` | `[]` |
| 齐尔查克 | 577 | 410 | 477 | 710 | False | False | False | 1 |  | 0 | `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}]` | `[]` |
| 谜图 | 551 | 400 | 451 | 700 | False | False | False | 2 |  | 0 | `[{"groups": ["挡人先锋", "情报官", "投锋"], "threshold": 2, "offset": -150}]` | `[]` |

### 术师

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 圣聆初雪 | 900 | 950 | 800 | 1250 | True | True | False | 2 |  | 0 | `[]` | `[]` |
| 荒芜拉普兰德 | 700 | 900 | 600 | 1200 | False | True | False | 3 | 2 | 0 | `[{"groups": ["术师"], "threshold": 1, "offset": -120}]` | `[{"collection": "波纹之手", "offset": 300}]` |
| 澄闪 | 695 | 841 | 595 | 1141 | False | True | False | 3 | 2 | 0 | `[{"groups": ["术师"], "threshold": 1, "offset": -120}]` | `[{"collection": "波纹之手", "offset": 300}]` |
| 逻各斯 | 692 | 841 | 592 | 1141 | False | True | False | 3 | 1 | 0 | `[]` | `[]` |
| 艾雅法拉 | 640 | 801 | 540 | 1101 | False | True | False | 2 |  | 0 | `[{"groups": ["术师"], "threshold": 1, "offset": -120}]` | `[]` |
| 妮芙 | 639 | 801 | 539 | 1101 | False | True | False | 2 |  | 0 | `[{"groups": ["术师"], "threshold": 1, "offset": -120}]` | `[]` |
| 烛煌 | 630 | 800 | 530 | 1100 | False | False | False | 3 | 2 | 0 | `[{"groups": ["术师"], "threshold": 1, "offset": -120}]` | `[]` |
| 刻俄柏 | 439 | 680 | 339 | 980 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 异客 | 359 | 780 | 259 | 1080 | False | True | False | 3 | 2 | 0 | `[]` | `[{"collection": "波纹之手", "offset": 638}]` |
| 莫斯提马 | 525 | 910 | 425 | 1210 | False | False | False | 3 | 2 | 0 | `[{"groups": ["术师"], "threshold": 2, "offset": -120}]` | `[{"collection": "波纹之手", "offset": 200}]` |
| 霍尔海雅 | 355 | 588 | 255 | 888 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| 维伊 | 360 | 560 | 260 | 860 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| 黑键 | 358 | 558 | 258 | 858 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| 雪绒 | 400 | 0 | 300 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 特米米 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 苦艾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 温米 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 卡达 | 563 | 0 | 463 | 300 | False | True | False | 2 |  | 0 | `[]` | `[]` |
| 史都华德 | 562 | 0 | 462 | 300 | False | True | False | 1 |  | 0 | `[]` | `[]` |

### 盾法

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 林 | 526 | 750 | 426 | 1050 | True | True | False | 1 |  | 0 | `[{"groups": ["术师"], "threshold": 1, "offset": -130}]` | `[]` |
| 卡涅利安 | 330 | 550 | 230 | 850 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| 薄绿 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蜜蜡 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |

### 提丰

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 维什戴尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蕾缪安 | 850 | 900 | 750 | 1200 | True | True | False | 2 |  | 0 | `[{"groups": ["益达"], "threshold": 1, "offset": -200}]` | `[]` |
| 提丰 | 370 | 510 | 270 | 810 | True | True | False | 2 |  | 0 | `[{"groups": ["益达"], "threshold": 1, "offset": -230}]` | `[]` |

### 狙击

远程狙击

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 维什戴尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 提丰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蕾缪安 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 早露 | 503 | 600 | 403 | 900 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| 迷迭香 | 800 | 2000 | 700 | 2300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 承曦格雷伊 | 781 | 500 | 681 | 800 | False | False | False | 1 |  | 0 | `[]` | `[]` |
| 菲亚梅塔 | 368 | 700 | 268 | 1000 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| W | 348 | 500 | 248 | 800 | False | False | False | 1 |  | 0 | `[]` | `[]` |
| 熔泉 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 埃拉托 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 铅踝 | 678 | 200 | 578 | 500 | True | True | False | 2 |  | 0 | `[{"groups": ["益达"], "threshold": 1, "offset": -10}]` | `[]` |
| 截云 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 慑砂 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 陨星 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 白雪 | 678 | 200 | 578 | 500 | True | True | False | 2 |  | 0 | `[{"groups": ["狙击", "水陈"], "threshold": 1, "offset": -200}]` | `[]` |
| 远牙 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 子月 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 安哲拉 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 守林人 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 安比尔 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |

### 辅助

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 酒神 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 塑心 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 铃兰 | 486 | 612 | 386 | 912 | False | True | False | 3 | 2 | 0 | `[{"groups": ["术师"], "threshold": 2, "offset": 80}]` | `[]` |
| 溯光星源 | 450 | 600 | 350 | 900 | False | True | False | 3 | 2 | 0 | `[{"groups": ["术师"], "threshold": 2, "offset": 80}]` | `[]` |
| 灵知 | 526 | 602 | 426 | 902 | False | True | False | 3 | 1 | 0 | `[]` | `[]` |
| 安洁莉娜 | 406 | 402 | 306 | 702 | False | False | False | 3 | 1 | 0 | `[]` | `[]` |
| 巫恋 | 462 | 360 | 362 | 660 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 初雪 | 353 | 255 | 253 | 555 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 波卜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 凛视 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 真理 | 256 | 400 | 156 | 700 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 海霓 | 256 | 400 | 156 | 700 | False | False | False |  |  | 0 | `[]` | `[]` |
| 但书 | 256 | 400 | 156 | 700 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 小满 | 256 | 400 | 156 | 700 | False | False | False |  |  | 0 | `[]` | `[]` |
| 格劳克斯 | 0 | 300 | -100 | 600 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 波登可 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 地灵 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 娜仁图亚 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 跃跃 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 梓兰 | 423 | 0 | 323 | 300 | False | True | False | 1 |  | 0 | `[]` | `[]` |
| 龙腾.F | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 地面阻挡

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| “弦惊” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 斩业星熊 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 黍 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 塞雷娅 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 戴乌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 余 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 珊比 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 年 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 星熊 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 机械师 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 涤火杰西卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 信仰搅拌机 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 瑕光 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 石棉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 雷蛇 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 深巡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蛇屠箱 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 号角 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 乌尔比安 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 怒潮凛冬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 百炼嘉维尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 隐德来希 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 圣约送葬人 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 赤刃明霄陈 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 予愿安洁莉娜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 锏 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 煌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 山 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 贝洛内 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| Mon3tr | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 海沫 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 羽毛笔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 休谟斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 临光 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 深律 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 吽 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 暴行 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 暴雨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 闪击 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 拜松 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 可颂 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 车尔尼 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 暮落 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 风丸 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 帕拉斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 医生 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 奥达 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 古米 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 赛柯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 泡泡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 角峰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 坚雷 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 斑点 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 丰川祥子 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 仇白 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 棘刺 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 忍冬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 推进之王 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 嵯峨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 火哨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 焰尾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 灰毫 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 卡缇 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 米格鲁 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 拉普兰德 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 艾丽妮 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 泥岩 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 斥罪 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 陈 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 白铁 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 娜斯提 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 赫德雷 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 银灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 幽灵鲨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 归溟幽灵鲨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 柏喙 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 烈夏 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 森蚺 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 洋灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 凛御银灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 伊内丝 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 郁金香 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 战车 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 艾丝黛尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 刻刀 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 晓歌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 寻澜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 齐尔查克 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 布洛卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 导火索 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 掠风 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 罗比菈塔 | 424 | 0 | 324 | 300 | False | True | False | 1 |  | 0 | `[]` | `[]` |
| 预备干员-重装 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 重岳 | 0 | 700 | -100 | 1000 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| “清平” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| Sharp | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 罗小黑 | 688 | 200 | 588 | 500 | True | True | False | 1 |  | 0 | `[]` | `[]` |
| 青枳 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 讯使 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 德克萨斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 红隼 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 清道夫 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 贾维 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 凛冬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 谜图 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 诗怀雅 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 鞭刃 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 苍苔 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 铎铃 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 极光 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 杜宾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芳汀 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 泡普卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 月见夜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 香草 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 贝娜 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 历阵锐枪芬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 风笛 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 野鬃 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 苇草 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 格拉尼 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 铸铁 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 薇薇安娜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 维娜·维多利亚 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 星极 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 燧石 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 猎蜂 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 因陀罗 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 杰克 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 炎客 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 石英 | 467 | 0 | 367 | 300 | False | True | False | 2 |  | 0 | `[]` | `[]` |
| 缠丸 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 断罪者 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 移动摄影器 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 机械水獭 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 预备干员-近战 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 触手 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| Friston-3 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 地面远程

打三及以上

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 丰川祥子 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 赛柯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 棘刺 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 号角 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 仇白 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 银灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 拉普兰德 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 烈夏 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 乌尔比安 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 凛御银灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 伊内丝 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 帕拉斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 医生 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 晓歌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 寻澜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 齐尔查克 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 火哨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 断崖 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 灰毫 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芳汀 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 霜叶 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 煌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 机械师 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 涤火杰西卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 信仰搅拌机 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 雷蛇 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 深巡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 谜图 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 诗怀雅 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 鞭刃 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 苍苔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 月见夜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 杜宾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 领主

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 丰川祥子 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 棘刺 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 仇白 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 银灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 拉普兰德 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 烈夏 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 断崖 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芳汀 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 霜叶 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 月见夜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 奶盾

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 黍 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 塞雷娅 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 临光 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 深律 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 古米 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 斑点 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 奶

所有能回复血的远程，包括单奶，群奶，辅助

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| Touch | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 夜莺 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 白面鸮 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 纯烬艾雅法拉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 遥 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 焰影苇草 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 缇缇 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蜜莓 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 桑葚 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 哈洛德 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 闪灵 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 流明 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 华法琳 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 凯尔希 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 图耶 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 亚叶 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 刺玫 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 濯尘芙蓉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 阿米娅-MEDIC | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 苏苏洛 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 赫默 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 褐果 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 浊心斯卡蒂 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 魔王 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 调香师 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 絮雨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 微风 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 末药 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 嘉维尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 安赛尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芙蓉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 淬羽赫默 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 月禾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 九色鹿 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 夏栎 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 明椒 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 莎草 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 波登可 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 锡兰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 清流 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 海蒂 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 空 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 预备干员-后勤 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 回费

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 凛御银灰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 伊内丝 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 晓歌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 寻澜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 齐尔查克 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 谜图 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 郁金香 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 焰尾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 嵯峨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 忍冬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 推进之王 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 德克萨斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 青枳 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 红隼 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 讯使 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 清道夫 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 贾维 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 凛冬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 香草 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 琴柳 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 万顷 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 极境 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 桃金娘 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 高台输出

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 新约能天使 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 维什戴尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 圣聆初雪 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 逻各斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 荒芜拉普兰德 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 澄闪 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 艾雅法拉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 焰影苇草 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 缇缇 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蕾缪安 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 艾拉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 桑特拉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 娜仁图亚 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 电弧 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 假日威龙陈 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 酒神 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 妮芙 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 烛煌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 能天使 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 空弦 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 灰烬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 林 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 异客 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 令 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 莫斯提马 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| Stormeye | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 隐现 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 寒芒克洛丝 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 莱伊 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 蓝毒 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 四月 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 灰喉 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 稀音 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 霍尔海雅 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 望 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 多萝西 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 白金 | 0 | 550 | -100 | 850 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 锡人 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 引星棘刺 | 680 | 710 | 580 | 1010 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 死芒 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 梅 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 克洛丝 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 刻俄柏 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 苦艾 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 特米米 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 刺玫 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 濯尘芙蓉 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 雪绒 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 阿米娅 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 阿米娅-MEDIC | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 至简 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 洛洛 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 卡达 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 耶拉 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 折光 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 夜魔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 阿 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 麦哲伦 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 跃跃 | 679 | 0 | 579 | 300 | True | True | False | 2 |  | 0 | `[{"groups": ["水陈", "速狙"], "threshold": 1, "offset": -300}]` | `[]` |
| 史都华德 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| “逍遥” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 鸿雪 | 0 | 0 | -100 | 300 | False | False | False | 3 | 1 | 0 | `[]` | `[]` |
| 黑 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 夕 | 0 | 320 | -100 | 620 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 天火 | 0 | 300 | -100 | 600 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 星源 | 0 | 300 | -100 | 600 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 惊蛰 | 0 | 300 | -100 | 600 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 寒檀 | 0 | 300 | -100 | 600 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 温米 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 布丁 | 0 | 200 | -100 | 500 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 梅尔 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 衡沙 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 深海色 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| Pith | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 龙腾.A | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 发条羽兽 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 地刺

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 阿斯卡纶 | 576 | 602 | 476 | 902 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -500}]` | `[]` |
| 水月 | 395 | 440 | 295 | 740 | False | False | False | 1 |  | 0 | `[{"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -600}]` | `[]` |
| 归溟幽灵鲨 | 570 | 601 | 470 | 901 | False | False | False | 2 |  | 0 | `[{"groups": ["凯尔希", "近卫", "召唤"], "threshold": 2, "offset": -350}, {"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -600, "doc": "地面阻挡≤1时，招募优先级-500"}]` | `[]` |
| 伊桑 | 405 | 405 | 305 | 705 | True | True | False | 2 |  | 0 | `[]` | `[]` |
| 狮蝎 | 385 | 400 | 285 | 700 | False | False | False | 1 |  | 0 | `[{"groups": ["凯尔希", "近卫", "重装", "情报官", "挡人先锋"], "is_less": true, "threshold": 1, "offset": -600}]` | `[]` |
| 若叶睦 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 绮良 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 双月 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 无人机

范围内回血,部署位任意

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 医疗探机 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 斯卡蒂的海嗣 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 夜灯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 炮灰

唤醒羊癫疯或者吸引炸弹

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 夜刀 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 砾 | 385 | 300 | 285 | 600 | False | True | False | 2 |  | 15 | `[]` | `[]` |
| 镜中虚影 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 孑 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 红 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 槐琥 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 卡夫卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 赛柯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| Mon3tr | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 傀影 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 麒麟R夜刀 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 缄默德克萨斯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 弑君者 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 移动摄影器 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| “清平” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 预备干员-近战 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 预备干员-重装 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 机械水獭 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 触手 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 桃金娘 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 极境 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 万顷 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 琴柳 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| “弦惊” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 幻影 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 掩体 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 归溟幽灵鲨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 幽灵鲨 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 泡普卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 月见夜 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芬 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 米格鲁 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 卡缇 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 大龙

部署逻辑是在地面阻挡前1格

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| “弦惊” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 机动盾牌 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 鱼

电弧的2技能召唤物

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 赛柯 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 障碍物

部署位地面,无朝向的召唤物

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 障碍物 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 掩体 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 幻影 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 补给站

部署位任意,有朝向的召唤物

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 便携式补给站 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 全自动造型仪 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 白铁™多功能平台 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 可靠电池 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 支援陷阱

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| “轰隆隆先生” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 失修舞台雾机 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 诅咒娃娃 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 雷鸣地雷 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 起重机

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 雪雉的安全起重机 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 风雪之眼

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 风雪之眼 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 其他地面

未出现的地面干员、特殊地面干员将默认分到该组,主要是挡1干员

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 风笛 | 410 | 350 | 310 | 650 | False | False | False | 2 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]` | `[]` |
| 历阵锐枪芬 | 390 | 250 | 290 | 550 | False | False | False | 1 |  | 0 | `[{"groups": ["投锋", "挡人先锋", "情报官"], "threshold": 1, "offset": -300}]` | `[]` |
| 歌蕾蒂娅 | -800 | 210 | -900 | 510 | False | False | False | 3 | 1 | 0 | `[]` | `[]` |
| 黑角 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 芳汀 | 468 | 0 | 368 | 300 | True | False | False | 2 |  | 0 | `[]` | `[]` |
| 断崖 | 370 | 0 | 270 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 刻刀 | 405 | 0 | 305 | 300 | False | False | False | 1 |  | 0 | `[]` | `[]` |
| 柏喙 | 405 | 0 | 305 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 铸铁 | 305 | 0 | 205 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 温蒂 | 400 | 500 | 300 | 800 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 见行者 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 食铁兽 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 阿消 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 布洛卡 | 412 | 0 | 312 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 导火索 | 412 | 0 | 312 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 薇薇安娜 | 411 | 0 | 311 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 星极 | 410 | 0 | 310 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 泡普卡 | 460 | 0 | 360 | 300 | False | True | False | 1 |  | 0 | `[]` | `[]` |
| 月见夜 | 466 | 0 | 366 | 300 | False | True | False | 1 |  | 0 | `[]` | `[]` |
| 火神 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 露托 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 拉普兰德 | 440 | 550 | 340 | 850 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 霜叶 | 318 | 0 | 218 | 300 | False | False | False | 1 |  | 0 | `[]` | `[]` |
| 铁钳号·原型机 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 槐琥 | 0 | 200 | -100 | 500 | False | False | False | 2 |  | 2 | `[]` | `[]` |
| 卡夫卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 3 | `[]` | `[]` |
| 达格达 | -800 | 0 | -900 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 维荻 | -800 | 0 | -900 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 夜刀 | 310 | 0 | 210 | 300 | False | True | False |  |  | 0 | `[]` | `[]` |
| 琳琅诗怀雅 | 260 | 350 | 160 | 650 | False | False | False | 3 | 1 | 0 | `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]` | `[]` |
| 老鲤 | 260 | 350 | 160 | 650 | False | False | False | 3 | 1 | 0 | `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]` | `[]` |
| 乌有 | 260 | 350 | 160 | 650 | False | False | False | 1 |  | 0 | `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]` | `[]` |
| 孑 | 260 | 350 | 160 | 650 | False | False | False | 2 |  | 0 | `[{"groups": ["回费"], "is_less": true, "threshold": 1, "offset": -300}]` | `[]` |
| 左乐 | -700 | 0 | -800 | 300 | False | False | False | 3 | 2 | 0 | `[]` | `[]` |
| 赫拉格 | -800 | 0 | -900 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 赤冬 | -800 | 0 | -900 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 火龙S黑角 | -800 | 0 | -900 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 玫兰莎 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 龙舌兰 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 预备干员-近战 | 208 | 0 | 108 | 300 | False | False | True |  |  | 0 | `[]` | `[]` |
| 流形 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 狼群 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 眠兽 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 樱桃三号 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 磐蟹护卫队 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 棋子 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

### 其他高台

未出现的高台干员、特殊高台干员将默认分到该组

| Operator | Recruit | Promote | Recruit Full | Promote Full | Start | Key | Alternate | Skill | Alt Skill | Auto Retreat | Offsets | Collection Offsets |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 送葬人 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 望 | 3000 | 3000 | 3000 | 3000 | False | False | False | 3 |  | 0 | `[]` | `[]` |
| 多萝西 | 596 | 466 | 496 | 766 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 死芒 | 400 | 600 | 300 | 900 | False | False | False | 3 |  | 0 | `[]` | `[]` |
| 可露希尔 | 325 | 325 | 225 | 625 | False | False | False | 3 | 2 | 0 | `[{"groups": ["回费"], "is_less": true, "offset": 150, "doc": "回费干员≤0时，优先级+150"}]` | `[]` |
| 缪尔赛思 | -800 | 140 | -900 | 440 | False | False | False | 3 | 1 | 0 | `[{"groups": ["回费"], "is_less": true, "offset": 150, "doc": "回费干员≤0时，优先级+150"}]` | `[]` |
| 夜半 | 235 | 0 | 135 | 300 | False | False | False | 2 |  | 0 | `[{"groups": ["回费"], "is_less": true, "offset": 150, "doc": "回费干员≤0时，优先级+150"}]` | `[]` |
| 渡桥 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[{"groups": ["回费"], "is_less": true, "offset": 150}]` | `[]` |
| 豆苗 | 234 | 200 | 134 | 500 | False | False | False | 2 |  | 0 | `[{"groups": ["回费"], "is_less": true, "offset": 150}]` | `[]` |
| 安德切尔 | 455 | 0 | 355 | 300 | False | True | False | 1 |  | 0 | `[]` | `[]` |
| 罗宾 | 5 | 200 | -95 | 500 | False | False | False | 1 |  | 0 | `[]` | `[]` |
| 焰狐龙梓兰 | 600 | 600 | 500 | 900 | False | False | False | 1 |  | 0 | `[{"groups": ["狙击", "水陈"], "threshold": 1, "offset": -200}]` | `[]` |
| 松果 | 550 | 200 | 450 | 500 | False | False | False | 2 |  | 0 | `[{"groups": ["狙击", "水陈"], "threshold": 1, "offset": -200}]` | `[]` |
| 玫拉 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 酸糖 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 普罗旺斯 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 和弦 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 深靛 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 爱丽丝 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 戴菲恩 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 霜华 | 0 | 0 | -100 | 300 | False | False | False | 1 |  | 0 | `[]` | `[]` |
| 红云 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 流星 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 杰西卡 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 伺夜 | -800 | 210 | -900 | 510 | False | False | False | 3 | 1 | 0 | `[]` | `[]` |
| 炎狱炎熔 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 莱恩哈特 | 0 | 250 | -100 | 550 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 格雷伊 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 远山 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 谬因 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 伊芙利特 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 蚀清 | -800 | 0 | -900 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 冰酿 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 夜烟 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 阿 | 256 | 400 | 156 | 700 | False | False | False | 1 |  | 0 | `[{"groups": ["奶"], "is_less": true, "threshold": 1, "offset": -300}]` | `[]` |
| 空构 | 0 | 0 | -100 | 300 | False | False | False | 1 |  | 0 | `[]` | `[]` |
| 奥斯塔 | 0 | 0 | -100 | 300 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| 炎熔 | 206 | 0 | 106 | 300 | False | True | False |  |  | 0 | `[]` | `[]` |
| 空爆 | 206 | 0 | 106 | 300 | False | True | False |  |  | 0 | `[]` | `[]` |
| 预备干员-术师 | 205 | 0 | 105 | 300 | False | False | True |  |  | 0 | `[]` | `[]` |
| 预备干员-狙击 | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |
| 玛露西尔 | -114514 | -800 | -114614 | -500 | False | False | False | 2 |  | 0 | `[]` | `[]` |
| “打字机” | 0 | 0 | -100 | 300 | False | False | False |  |  | 0 | `[]` | `[]` |

## Static Analyzer Summary

- `theme`: JieGarden
- `group_count`: 45
- `operator_definition_count`: 741
- `unique_operator_count`: 417
- `start_operator_count`: 49
- `key_operator_count`: 89
- `team_complete_condition_count`: 4
- `issue_count`: 530
- `issues_by_severity`: {'info': 301, 'error': 2, 'warning': 227}
