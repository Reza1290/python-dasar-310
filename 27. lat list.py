# list data buku

from re import A


list_buku = [] #list kosong cangkang

while True:
    judul_buku = input("Masukkan judul Buku = ")
    penulis_buku = input("Masukkan Penulis Buku = ")
    tahunterbit = input("Masukkan Tahun Terbit = ")

    data_buku = [judul_buku,penulis_buku,tahunterbit]
    list_buku.append(data_buku)
    
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]} | {buku[2]}")

    lanjut = input("Lanjut? Y/N ")
    if lanjut == "n" or lanjut == "N":
        break



