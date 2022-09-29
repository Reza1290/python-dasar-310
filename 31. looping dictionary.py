# looping dictionarycls

nama_singkat = {
    "ai":"abi",
    "bi":"budi",
    "ci":"caci",
    "di":"dedi",
    "ri":"rudi"
}

for nama in nama_singkat :
    print(nama)
print(nama_singkat.keys())

for kunci in nama_singkat.keys():
    print(nama_singkat.get(kunci))

#item atau iterables adalah isi (values)

isi = nama_singkat.values()
print(isi)

for isian in nama_singkat.values():
    print(isian)

item = nama_singkat.items()
print(item)

for items in item:
    print(items)

    # sedangkan items adalah key + isi

# atau susahnya gini
for key,values in nama_singkat.items():
    print(f"kunci = {key}, values = {values}")



