# 杀戮尖塔2 卡牌抓取统计工具

一个用于分析杀戮尖塔2（Slay The Spire 2）游戏存档中卡牌抓取统计数据的 Python 工具。

## 功能特性

- **卡牌抓取统计**：按游戏阶段（第1、2、3幕）统计卡牌抓取数和抓取率
- **卡组构成分析**：追踪卡组构成，包括总数量、诅咒、初始牌、攻击牌、技能牌、能力牌和消耗牌
- **净数量计算**：计算卡组的"净数量"，即扣除消耗牌和能力牌后的有效牌数
- **特殊情况处理**：处理幽灵种子、佩尔之翼、净化等特殊游戏机制
- **版本对比**：比较不同游戏版本之间的卡牌抓取率差异
- **多角色支持**：支持分析任意角色（静默猎手、铁甲战士、故障机器人等）
- **Excel 输出**：生成格式化的 Excel 报告，按卡池和稀有度分表显示

## 环境要求

- Python 3.7+
- openpyxl

```bash
pip install openpyxl
```

## 使用方法

### 生成卡牌抓取统计

```bash
python card_pick_stats.py 1 50 --history "存档历史记录路径" --card-info card_rarity.json --output card_stats_output
```

**参数说明：**
- `n`：起始局数（从后往前数，1 = 最近一局）
- `m`：结束局数（m >= n）
- `--history, -i`：包含 `.run` 文件的存档历史目录路径
- `--card-info, -c`：卡牌信息 JSON 文件路径
- `--output, -o`：输出目录（默认：card_stats_output）
- `--localization, -l`：本地化文件路径（可选，用于显示中文卡牌名）
- `--style, -s`：表头颜色风格（blue, green, orange, yellow, purple, gray, pink, red, cyan）
- `--character`：要分析的角色（默认：SILENT）

**示例：**
```bash
python card_pick_stats.py 1 27 --history "C:\Users\用户名\AppData\Roaming\SlayTheSpire2\steam\123456789\saves\history" --card-info card_rarity.json --style green
```

### 对比不同版本的统计数据

```bash
python compare_stats.py 文件1.xlsx 文件2.xlsx --output 对比结果.xlsx
```

**参数说明：**
- `file1`：第一个 Excel 文件（作为基准）
- `file2`：第二个 Excel 文件
- `--output, -o`：输出文件路径（可选）

## 输出格式

生成的 Excel 文件包含多个表单：

1. **卡组构成**：显示每局游戏的卡组构成
   - 总数量、诅咒、打击、防御、攻击牌、技能牌、能力牌、消耗牌
   - 净数量计算
   - 特殊情况备注

2. **按卡池和稀有度分类的卡牌统计**：多个表单，按以下方式组织：
   - 卡池（静默猎手、无色、铁甲战士等）
   - 稀有度（普通、罕见、稀有、远古等）
   
   每个表单显示：
   - 卡牌 ID 和名称
   - 每幕的抓取数、出现数和抓取率
   - 总体抓取统计

## 特殊情况处理

工具会处理以下特殊游戏机制：

- **幽灵种子**：初始打击和防御视为消耗牌
- **佩尔之翼**：初始防御视为消耗牌
- **净化**：根据是否升级，从净数量中减去 3（未升级）或 5（已升级）
- **虚无**：带有虚无属性的牌视为消耗牌
- **灵魂之力**：附魔会移除卡牌的消耗属性

## 卡牌信息文件

`card_rarity.json` 文件包含：
- 卡牌 ID
- 稀有度（普通、罕见、稀有、远古等）
- 类型（攻击、技能、能力等）
- 卡池（静默猎手、无色、铁甲战士等）
- 是否消耗
- 是否虚无

## 存档文件位置

默认存档文件位置：
- **Windows**: `%APPDATA%\SlayTheSpire2\steam\[steam_id]\saves\history`
- **Linux**: `~/.config/SlayTheSpire2/steam/[steam_id]/saves/history`
- **macOS**: `~/Library/Application Support/SlayTheSpire2/steam/[steam_id]/saves/history`

## 许可证

MIT License

## 贡献

欢迎贡献代码！请随时提交 Pull Request。
