#program looping bikin segitiga?

# cara dasar

print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")

# looping dengan for

dummy = 1 #kita integerkan

for i in range(10): #untuk i di range 1 - 10, 
    print(("*"*dummy)) # 1 dikalikan dengan bintang (str x str)
    dummy += 1 # kembali lagi menjadi 1+1, 2+1, ... ( keatas )


# looping dengan while

segitiga = "*"
angka = 1

while True:
    print((segitiga*angka))
    angka += 1
    if angka == 5:
        break

print("end")

# ganjil saja
segitiga = "*"
angka = 1

while True:
    if angka%2:
        print((segitiga*angka).center(19))
        angka += 1
    else :
        angka += 1
        continue

    if angka > 5:
        break

print("end")



