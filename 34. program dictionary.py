# input data terus print
import os
import string
import random

template_mahasiswa = {
    "nama":"mahasiswa",
    "prodi":"PROD001",
    "nrp":"0000000",
    "sks":146,
}

mahasiswa_kosong = {
    
}

while True:
   # os.system("cls")
    # print(template_mahasiswa)

    mahasiswa = dict.fromkeys(template_mahasiswa)
    mahasiswa["nama"] = input("Masukkan Nama :")
    mahasiswa["nrp"] = input("Masukkan Nrp :")
    mahasiswa["prodi"] = input("Masukkan Prodi :")
    mahasiswa["sks"] = int(input("Masukkan Sksmu :"))

    print(f'{"Key":<5} {"Nama":<16} {"NRP":<8} {"Prodi":<16} {"SKS":<4}')
    print("=="*50)

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
    mahasiswa_kosong.update({KEY:mahasiswa})

    for mahasiswa in mahasiswa_kosong:
        KEY = mahasiswa

        NAMA = mahasiswa[KEY]['nama']
        NRP = mahasiswa[KEY]['nrp']
        PRODI = mahasiswa[KEY]['prodi']
        SKS = mahasiswa[KEY]['sks']

        print(f'{KEY:<5} {NAMA:<16} {NRP:<8} {PRODI:<16} {SKS:<4}') 
    
        lanjut = input("Lanjut? Y/N")
        if lanjut == N:
            break
        else:
            continue
    # print(mahasiswa)

