from .generic_collector import collect

def process(data):
    processed = []
    for item in data:
        try:
            maxmin = float(item.get("maxmin", 0))
            kunduzgi = float(item.get("kunduzgi", 0))
            processed.append({
                "name": item.get("name", ""),
                "Abituriyentlar soni": int(maxmin),
                "To'g'ri ishlangan savollar soni": int(kunduzgi)
            })
        except Exception as e:
            print(f"Xato item: {item} => {e}")
    return processed

def save(base_url, viloyat_ids, folder_path):
    collect(
        base_url=base_url,
        viloyat_ids=viloyat_ids,
        folder_path=folder_path,
        endpoint="/GetAllJsMj1",
        filename="Joriy yil bitiruvchilarning majburiy fanlar bo'yicha ko'rsatkichi.json",
        process_fn=process
    )
