import os

base_url = 'https://mandat.uzbmb.uz/Bakalavr2025'

viloyatlar = [
    "Barchasi","Qoraqalpog'iston Respublikasi","Andijon viloyati","Namangan viloyati",
    "Fargʻona viloyati","Buxoro viloyati","Xorazm viloyati","Surxandaryo viloyati",
    "Qashqadaryo viloyati","Jizzax viloyati","Navoiy viloyati","Samarqand viloyati",
    "Sirdaryo viloyati","Toshkent viloyati","Toshkent shahri"
]

current_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(current_dir, "natijalar")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

viloyat_ids = {v: i for i, v in enumerate(viloyatlar)}

urls1 = {
    "Joriy yil bitiruvchilarining top 10 ta'lim muassasalari": '/Getallmaktabortatop?a=',
    "O'rtacha ballar": '/Getalljs?a=',
    "TOP 250": '/Getallprjs?a1=',
    "Maksimal ballning 30%": '/Getalljs1?a=',
    "Majburiy fanlarni ishlanish ko'rsatkichi": '/GetAllJsMj?a=',
    "Chetlashtirilgan abituriyentlar": '/Getallchetjs?a1=',
    "Qiymatlanmagan abituriyentlar": '/Getallqiyjs?a1=',
    "Erkak va Ayollarning o'rtacha ballari": "/GetallEA?a="
}
