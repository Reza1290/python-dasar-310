# copy and pop

nama_singkat = {
    "ai":"abi",
    "bi":"budi",
    "ci":"caci",
    "di":"dedi",
    "ri":"rudi"
}

# copy menggunakan data.copy()
print(nama_singkat)

nama_s = nama_singkat
print(nama_singkat)
print(nama_s)

nama_s = nama_singkat.copy()

nama_singkat["ai"] = "ariani"

print(nama_singkat)
print(nama_s)

#pop diambil dipindah key saja

datapop = nama_singkat.pop("ai")
print("data yang di pop =", datapop)
print(nama_singkat)

#popitem, pop tapi key + value dan terakhirnya
datapopitem = nama_s.popitem()
print("data yang di pop =", datapopitem)
print(nama_s)


