from .generic_collector import collect

def process(data):
    processed = []
    for item in data:
        try:
            maxmin = float(item.get("maxmin", 0))
            processed.append({
                "name": item.get("name", ""),
                "Qiymatlanmaganlar joriy yil bitiruvchilari": int(maxmin)
            })
        except Exception as e:
            print(f"Xato item: {item} => {e}")
    return processed

def save(base_url, viloyat_ids, folder_path):
    collect(
        base_url=base_url,
        viloyat_ids=viloyat_ids,
        folder_path=folder_path,
        endpoint="/Getallmaktabqiy",
        filename="Qiymatlanmagan joriy yil bitiruvchilari.json",
        process_fn=process
    )
