from .generic_collector import collect

def process(data):
    processed = []
    for item in data:
        try:
            erkaklar_ball = float(item.get("ball", 0))
            erkaklar_soni = int(item.get("maxmin", 0))
            ayollar_ball = float(item.get("kechki", 0))
            ayollar_soni = int(item.get("kunduzgi", 0))
            processed.append({
                "name": item.get("name", ""),
                "Erkaklar o'rtacha ball": erkaklar_ball,
                "Jami erkak abituriyentlar soni": erkaklar_soni,
                "Ayollar o'rtacha ball": ayollar_ball,
                "Jami ayol abituriyentlar soni": ayollar_soni
            })
        except Exception as e:
            print(f"Xato item: {item} {e}")
    return processed

def save(base_url, viloyat_ids, folder_path):
    collect(
        base_url=base_url,
        viloyat_ids=viloyat_ids,
        folder_path=folder_path,
        endpoint="/GetallEA21",
        filename="Erkak va Ayollarning o'rtacha ballari joriy yil bitiruvchilari.json",
        process_fn=process
    )
