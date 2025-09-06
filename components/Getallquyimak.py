from .generic_collector import collect

def process(data):
    processed = []
    for item in data:
        try:
            ball = float(item.get("ball", 0))
            maxmin = float(item.get("maxmin", 0))
            processed.append({
                "name": item.get("name", ""),
                "56.7 dan yuqori": int(ball),
                "56.7 dan quyi": int(maxmin)
            })
        except Exception as e:
            print(f"Xato item: {item} => {e}")
    return processed

def save(base_url, viloyat_ids, folder_path):
    collect(
        base_url=base_url,
        viloyat_ids=viloyat_ids,
        folder_path=folder_path,
        endpoint="/Getallquyimak",
        filename="Joriy yil bitiruvchilarining maksimal ballning 30% bo'yicha ko'rsatkichlari.json",
        process_fn=process
    )
