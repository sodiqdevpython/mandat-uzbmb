import threading
from config import base_url, viloyat_ids, folder_path
from components import Getallmaktabortatop,Getalljs,Getallprjs,Getalljs1,GetAllJsMj,Getallchetjs,GetallEA,Getallqiyjs,Getallmaktaborta,Getallquyimak,GetAllJsMj1,Getallmaktabqiy2,Getallmaktabqiy,GetallEA21

modules = [Getallmaktabortatop,Getalljs,Getallprjs,Getalljs1,GetAllJsMj,Getallchetjs,GetallEA,Getallqiyjs,Getallmaktaborta,Getallquyimak,GetAllJsMj1,Getallmaktabqiy2,Getallmaktabqiy,GetallEA21]

threads = []

print("\nnatijalar degan folder ochildi shuni ichiga yozilayabdi\n")

for mod in modules:
    t = threading.Thread(
        target=mod.save,
        args=(base_url, viloyat_ids, folder_path)
    )
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("\n\nmain.py tugadi")
