# p date and time disingkat datetime

import datetime as dt

hari_ini = dt.date.today()

print(hari_ini)

# mau bikin borang data misalnyya oghey

hari_lahir = int(input("hari = "))
bulan_lahir = int(input("Bulan = "))
tahun_lahir = int(input("Tahun = "))


tanggal = dt.date(tahun_lahir,bulan_lahir,hari_lahir)

print(f"Kamu Lahir pada {tanggal}")

print(f"pada hari {tanggal:%A}")

umur = hari_ini - tanggal
umur_tahun = umur / 365
umur_ = umur_tahun.days
umur_sisabulan = (umur.days % 365) // 30 
print(umur_,"tahun") 
print(umur_sisabulan, "bulan")
