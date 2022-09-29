# dictionary pt2
# key harus str, data dikanan boleh apa saja
dict_data = {
     "ai":"abi",
    "bi":"budi",
    "ri":"rudi"
}

panjangdict = len(dict_data)

print("panjang dict", panjangdict)

# pemanggilan dictionary
print(dict_data["ai"])
# print(dict_data["asu"]) # akan error jika kayak list

# gunakan nama.get("key") untuk pemanggilan
print(dict_data.get("ai"))
print(dict_data.get("as")) # saat tidak ada akan menghasilkan none
print(dict_data.get("asu","Tidak Ditemukan"))
# saat None akan digantikan dengan str "tidak ditemukan"
# kalo ditemukan gimana? apakah ke print juga?
print(dict_data.get("ai","Tidak Ketemu")) # jawabannya tidak di print

# mengecek apakah Key tersebut ada di dalam dictionary kita
# search () gunakan in
# jika ada
kunci = "ai"
cekkunci = kunci in dict_data
print("apakah kunci",kunci, "ada di dict?:", cekkunci)
# tidak ada
kunci = "as"
cekkunci = kunci in dict_data
print("apakah kunci",kunci, "ada di dict?:", cekkunci)

# mengupdate kunci ( update list , mengganti list)
# menggunakan index seperti list
# menggunakan data.update({"key":"isi"})
# 1
dict_data["ai"] = "asi"
print(dict_data)
dict_data["zi"] = "zasi" # tambah baru
print("\n", dict_data)
# menggunakan data.update

dict_data.update({"ai":"asli"})
print(dict_data)
dict_data.update({"ra":"reza"}) # tambah baru
print(dict_data)

# apakah bisa delete?
# bisa gunakan del data

del dict_data["ra"]
print(dict_data)






