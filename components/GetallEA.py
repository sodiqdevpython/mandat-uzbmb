import os, json
from .fetch import fetch


def save(base_url, viloyat_ids, folder_path):
    result = {}
    endpoint = '/GetallEA?a='
    for viloyat, vid in viloyat_ids.items():
        url = f"{base_url}{endpoint}{vid}"
        data = fetch(url)
        if data is None:
            continue
        processed = []
        for item in data:
            try:
                ball = float(item.get("ball", 1))
                kechki = float(item.get("kechki", 1))
                kunduzgi = int(item.get("kunduzgi", 1))
                maxmin = int(item.get("maxmin", 1))
                processed.append({
                    "name": item.get("name", ""),
                    "Jami erkak abituriyentlar soni": maxmin,
                    "Erkaklar": ball,
                    "Ayollar": kechki,
                    "Jami ayol abituriyentlar soni": kunduzgi
                })
            except Exception as e:
                print(f"Xato item: {item} => {e}")
        result[viloyat] = processed

    filename = os.path.join(folder_path, "Erkaklar va Ayollarning o'rtacha ballari.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print("Erkaklar va Ayollarning o'rtacha ballari.json")
