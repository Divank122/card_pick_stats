# Slay The Spire 2 Card Pick Stats

A Python tool for analyzing card pick statistics from Slay The Spire 2 game save files.

## Features

- **Card Pick Statistics**: Analyze card pick rates and counts by game act (Act 1, 2, 3)
- **Deck Composition Analysis**: Track deck composition including total cards, curses, starter cards, attacks, skills, powers, and exhaust cards
- **Net Quantity Calculation**: Calculate the "net quantity" of decks after accounting for exhaust and power cards
- **Special Case Handling**: Handle special game mechanics like Ghost Seed, Paels Wing, Purity, and Protector
- **Version Comparison**: Compare card pick rates between different game versions
- **Multi-Character Support**: Analyze runs for any character (Silent, Ironclad, Defect, etc.)
- **Excel Output**: Generate formatted Excel reports with multiple sheets organized by card pool and rarity

## Requirements

- Python 3.7+
- openpyxl

```bash
pip install openpyxl
```

## Usage

### 1. Extract Card Information (Optional)

If you have access to the game source code, you can extract card information:

```bash
python extract_rarity.py --cards-dir "path/to/game/src/Core/Models/Cards" --cardpools-dir "path/to/game/src/Core/Models/CardPools" --output card_rarity.json
```

A pre-generated `card_rarity.json` is included in this repository.

### 2. Generate Card Pick Statistics

```bash
python card_pick_stats.py 1 50 --history "path/to/saves/history" --card-info card_rarity.json --output card_stats_output
```

**Arguments:**
- `n`: Starting game number (from the end, e.g., 1 = most recent)
- `m`: Ending game number (m >= n)
- `--history, -i`: Path to the save history directory containing `.run` files
- `--card-info, -c`: Path to card info JSON file
- `--output, -o`: Output directory (default: card_stats_output)
- `--localization, -l`: Optional localization file for Chinese card names
- `--style, -s`: Header color style (blue, green, orange, yellow, purple, gray, pink, red, cyan)
- `--character`: Character to analyze (default: SILENT)

**Example:**
```bash
python card_pick_stats.py 1 27 --history "C:\Users\YourName\AppData\Roaming\SlayTheSpire2\steam\123456789\saves\history" --card-info card_rarity.json --style green
```

### 3. Compare Statistics Between Versions

```bash
python compare_stats.py file1.xlsx file2.xlsx --output comparison.xlsx
```

**Arguments:**
- `file1`: First Excel file (baseline)
- `file2`: Second Excel file
- `--output, -o`: Output file path (optional)

## Output Format

The generated Excel file contains multiple sheets:

1. **卡组构成 (Deck Composition)**: Shows deck composition for each run
   - Total cards, curses, strikes, defends, attacks, skills, powers, exhaust cards
   - Net quantity calculation
   - Special case notes

2. **Card Pick Statistics by Pool and Rarity**: Multiple sheets organized by:
   - Card pool (Silent, Colorless, Ironclad, etc.)
   - Rarity (Common, Uncommon, Rare, Ancient, etc.)
   
   Each sheet shows:
   - Card ID and name
   - Pick count, offer count, and pick rate for each act
   - Total pick statistics

## Special Cases

The tool handles several special game mechanics:

- **Ghost Seed (幽灵种子)**: Initial strikes and defends count as exhaust
- **Paels Wing (佩尔之翼)**: Initial defends count as exhaust
- **Purity (净化)**: Subtract 3 (unupgraded) or 5 (upgraded) from net quantity
- **Ethereal (虚无)**: Cards with ethereal count as exhaust
- **Soul Power (灵魂之力)**: Enchantment removes exhaust from cards

## Card Information File

The `card_rarity.json` file contains:
- Card ID
- Rarity (Common, Uncommon, Rare, Ancient, etc.)
- Type (Attack, Skill, Power, etc.)
- Pool (Silent, Colorless, Ironclad, etc.)
- Exhaust status
- Ethereal status

## Save File Location

Default save file locations:
- **Windows**: `%APPDATA%\SlayTheSpire2\steam\[steam_id]\saves\history`
- **Linux**: `~/.config/SlayTheSpire2/steam/[steam_id]/saves/history`
- **macOS**: `~/Library/Application Support/SlayTheSpire2/steam/[steam_id]/saves/history`

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
