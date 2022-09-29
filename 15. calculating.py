# Kalkulator Gaming

header = "KALKULATOR DESU"
print(header.center(30,"="))

print("Menu".center(30))
print("""1. Perkalian
2. Pembagian
3. Penambahan
4. Pengurangan
""")


operator = int(input("Masukkan Operator sesuai Nomer diatas (1-4), "))
print(f"kamu memilih angka {operator}")
if operator == 1:
    angka1 = float(input("Masukkan Angka Pertama "))
    angka2 = float(input("Masukkan Angka Kedua "))
    hasil = angka1 * angka2
    print("hasilmu adalah" , hasil)
elif operator == 2:
    angka1 = float(input("Masukkan Angka Pertama "))
    angka2 = float(input("Masukkan Angka Kedua "))
    hasil = angka1 / angka2
    print("hasilmu adalah", hasil)
elif operator == 3:
    angka1 = float(input("Masukkan Angka Pertama "))
    angka2 = float(input("Masukkan Angka Kedua "))
    hasil = angka1 + angka2
    print("hasilmu adalah", hasil)
elif operator == 4:
    angka1 = float(input("Masukkan Angka Pertama "))
    angka2 = float(input("Masukkan Angka Kedua "))
    hasil = angka1 - angka2
    print("hasilmu adalah", hasil)
else:
    print(f"Operator {operator} Tidak Terdaftar ulangi kembali")







