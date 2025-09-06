import os, json
from .fetch import fetch


def save(base_url, viloyat_ids, folder_path):
    result = {}
    endpoint = '/Getallmaktabortatop?a='
    for viloyat, vid in viloyat_ids.items():
        url = f"{base_url}{endpoint}{vid}"
        data = fetch(url)
        if data is None:
            continue
        processed = []
        for item in data:
            try:
                ball = float(item.get("ball", 0))
                maxmin = float(item.get("maxmin", 1))
                processed.append({
                    "name": item.get("name", ""),
                    "ball": ball / maxmin if maxmin != 0 else 0,
                    "Abituriyentlar soni": maxmin
                })
            except Exception as e:
                print(f"Xato item: {item} => {e}")
        result[viloyat] = processed

    filename = os.path.join(folder_path, "Joriy yil bitiruvchilarining top 10 ta'lim muassasalari.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print("Joriy yil bitiruvchilarining top 10 ta'lim muassasalari.json")
