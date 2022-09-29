# break while loop
# dia skip ke end ga balik awal

angka = 0

while angka > -1:

    angka += 1
    print(f"{angka}")
    
    if angka == 10:
        break

print("end")


data_int = int(input("Masukkan Angka"))

angka = 0
while True:
    angka += 1
    print(f"{angka}")
    if angka == data_int:
        break
print("end")