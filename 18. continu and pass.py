# continue, pass, break

# pass > tidak di eksekusi alias di skip asiap kamutu 
#gadiajak

angka = 0

while angka < 5:

    angka += 1
    if angka == 3:
        continue
    #dibawah continu tidak di eksekusi tetapi balik ke line 
    print(f"{angka}")
print("end")

angka = 0

while angka < 5:

    angka += 1
    if angka == 3:
        pass #nothing effect in this line
    print(f"{angka}")
print("end")
