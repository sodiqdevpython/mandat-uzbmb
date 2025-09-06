import os, json
from .fetch import fetch

def collect(base_url, viloyat_ids, folder_path, endpoint, filename, process_fn):
    result = {}

    url = f"{base_url}{endpoint}?a=0&x1=0"
    umumiy = fetch(url)
    if umumiy:
        result["Umumiy"] = process_fn(umumiy)

    for viloyat, vid in viloyat_ids.items():
        vil_data = {}

        url = f"{base_url}{endpoint}?a={vid}&x1=0"
        vil_res = fetch(url)
        if vil_res:
            vil_data["umumiy"] = process_fn(vil_res)
            
        tumans_url = f"{base_url}/GetTumans?a1={vid}"
        tumans = fetch(tumans_url)
        if tumans:
            tumanlar_data = {}
            for tuman in tumans:
                tuman_id = tuman.get("maxmin")
                tuman_name = tuman.get("name", f"Tuman-{tuman_id}")
                try:
                    tuman_url = f"{base_url}{endpoint}?a={vid}&x1={tuman_id}"
                    tuman_res = fetch(tuman_url)
                    if tuman_res:
                        tumanlar_data[tuman_name] = process_fn(tuman_res)
                except Exception as e:
                    print(f"Xato: {tuman_name} => {e}")
            vil_data["tumanlar"] = tumanlar_data

        result[viloyat] = vil_data

    filepath = os.path.join(folder_path, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)