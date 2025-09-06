import os, json
from .fetch import fetch


def save(base_url, viloyat_ids, folder_path):
    result = {}
    endpoint = '/Getalljs1?a='
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
                    "56.7 dan yuqori": int(ball),
                    "56.7 dan quyi": int(maxmin)
                })
            except Exception as e:
                print(f"Xato item: {item} => {e}")
        result[viloyat] = processed

    filename = os.path.join(folder_path, "Maksimall ballning 30%.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print("Maksimall ballning 30%.json")
