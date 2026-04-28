import os
import re
import json
import argparse

def camel_to_snake(name):
    result = []
    for i, c in enumerate(name):
        if c.isupper() and i > 0:
            result.append('_')
        result.append(c)
    return ''.join(result)

def extract_card_info(cards_dir, cardpools_dir, output_file):
    card_info = {}
    
    for filename in os.listdir(cards_dir):
        if not filename.endswith('.cs'):
            continue
        
        filepath = os.path.join(cards_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        rarity_match = re.search(r':\s*base\s*\([^)]*CardRarity\.(\w+)', content)
        type_match = re.search(r':\s*base\s*\([^)]*CardType\.(\w+)', content)
        exhaust_match = re.search(r'CardKeyword\.Exhaust', content)
        ethereal_match = re.search(r'CardKeyword\.Ethereal', content)
        
        if rarity_match or type_match:
            class_name = filename.replace('.cs', '')
            card_id = camel_to_snake(class_name).upper()
            
            card_info[card_id] = {
                "rarity": rarity_match.group(1) if rarity_match else "Unknown",
                "type": type_match.group(1) if type_match else "Unknown",
                "pool": "Unknown",
                "exhaust": exhaust_match is not None,
                "ethereal": ethereal_match is not None
            }
    
    card_pools = {
        "SilentCardPool.cs": "Silent",
        "IroncladCardPool.cs": "Ironclad",
        "DefectCardPool.cs": "Defect",
        "ColorlessCardPool.cs": "Colorless",
        "CurseCardPool.cs": "Curse",
        "StatusCardPool.cs": "Status",
        "EventCardPool.cs": "Event",
        "TokenCardPool.cs": "Token",
        "QuestCardPool.cs": "Quest",
        "NecrobinderCardPool.cs": "Necrobinder",
        "RegentCardPool.cs": "Regent",
    }
    
    for pool_file, pool_name in card_pools.items():
        pool_path = os.path.join(cardpools_dir, pool_file)
        if not os.path.exists(pool_path):
            continue
        
        with open(pool_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        matches = re.findall(r'ModelDb\.Card<(\w+)>', content)
        for class_name in matches:
            card_id = camel_to_snake(class_name).upper()
            if card_id in card_info:
                card_info[card_id]["pool"] = pool_name
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(card_info, f, indent=2, ensure_ascii=False)
    
    print(f"Extracted {len(card_info)} cards info to {output_file}")
    
    type_counts = {}
    pool_counts = {}
    rarity_counts = {}
    
    for card_id, info in card_info.items():
        t = info.get("type", "Unknown")
        p = info.get("pool", "Unknown")
        r = info.get("rarity", "Unknown")
        
        type_counts[t] = type_counts.get(t, 0) + 1
        pool_counts[p] = pool_counts.get(p, 0) + 1
        rarity_counts[r] = rarity_counts.get(r, 0) + 1
    
    print("\n类型统计:")
    for t, count in sorted(type_counts.items()):
        print(f"  {t}: {count}")
    
    print("\n卡池统计:")
    for p, count in sorted(pool_counts.items()):
        print(f"  {p}: {count}")
    
    print("\n稀有度统计:")
    for r, count in sorted(rarity_counts.items()):
        print(f"  {r}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="从Slay The Spire 2源代码中提取卡牌信息")
    parser.add_argument("--cards-dir", "-c", type=str, required=True,
                        help="卡牌源代码目录路径（包含.cs文件的目录）")
    parser.add_argument("--cardpools-dir", "-p", type=str, required=True,
                        help="卡池源代码目录路径")
    parser.add_argument("--output", "-o", type=str, default="card_rarity.json",
                        help="输出JSON文件路径（默认: card_rarity.json）")
    args = parser.parse_args()
    
    extract_card_info(args.cards_dir, args.cardpools_dir, args.output)
