import os, json
from .fetch import fetch

def save(base_url, viloyat_ids, folder_path):
    result = {}

    def process(data):
        processed = []
        for item in data:
            try:
                ball = float(item.get("ball", 0))
                maxmin = float(item.get("maxmin", 1))
                processed.append({
                    "name": item.get("name", ""),
                    "O'rtacha ball": ball / maxmin if maxmin != 0 else 0,
                    "Barcha abituriyentlar soni": int(maxmin)
                })
            except Exception as e:
                print(f"Xato item: {item} => {e}")
        return processed
    endpoint = '/Getallmaktaborta?a=0&x1=0'
    url = f"{base_url}{endpoint}"
    umumiy = fetch(url)
    if umumiy:
        result["Umumiy"] = process(umumiy)
    for viloyat, vid in viloyat_ids.items():
        vil_data = {}

        url = f"{base_url}/Getallmaktaborta?a={vid}&x1=0"
        vil_res = fetch(url)
        if vil_res:
            vil_data["umumiy"] = process(vil_res)
        tumans_url = f"{base_url}/GetTumans?a1={vid}"
        tumans = fetch(tumans_url)
        if tumans:
            tumanlar_data = {}
            for tuman in tumans:
                tuman_id = tuman.get("maxmin")
                tuman_name = tuman.get("name", f"Tuman-{tuman_id}")
                try:
                    tuman_url = f"{base_url}/Getallmaktaborta?a={vid}&x1={tuman_id}"
                    tuman_res = fetch(tuman_url)
                    if tuman_res:
                        tumanlar_data[tuman_name] = process(tuman_res)
                except Exception as e:
                    print(f"Xato: {tuman_name} => {e}")
            vil_data["tumanlar"] = tumanlar_data

        result[viloyat] = vil_data
    filename = os.path.join(folder_path, "Joriy yil bitiruvchilarining o‘rtacha ballari.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("Joriy yil bitiruvchilarining o‘rtacha ballari.json")
