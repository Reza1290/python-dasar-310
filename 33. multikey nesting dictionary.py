# multikey / nest
import datetime

siswa1 = {
    "nama":"udin syah",
    "kelas":"mipa 1",
    "absen":"20",
    "ttl":datetime.datetime(2000,10,24)
}

siswa2 = {
    "nama":"budi gaming",
    "kelas":"mipa 1",
    "absen":"21",
    "ttl":datetime.datetime(2001,10,24)
}

siswa3 = {
    "nama":"asep galon",
    "kelas":"mipa 1",
    "absen":"25",
    "ttl":datetime.datetime(2000,11,24)
}

data_siswa = {
    "S1":siswa1,
    "S2":siswa2,
    "S3":siswa3
}

print(f"{'KUNCI':<6} {'NAMA':<20}  {'KELAS':<10} {'ABSEN':<5} {'TTL'}")
print("-"*50)
for kunci in data_siswa:
    KEY = kunci
    NAMA = data_siswa[KEY]["nama"]
    KELAS = data_siswa[KEY]["kelas"]
    ABSEN = data_siswa[KEY]["absen"]
    TTL = data_siswa[KEY]["ttl"]

    print(f"{KEY:<6} {NAMA:<20}  {KELAS:<10} {ABSEN:<5} {TTL}")

   