# looping list dan enumerate

list_angka = [1,4,6,3,5,4,3,4,2]

for i in list_angka:
    print(f"{i}")

# for Loop range

list_angka = [1,4,6,3,5,4,3,4,2]
panjang_angka = len(list_angka)

for i in range(panjang_angka):
    print(f"angka = {list_angka[i]}")

# while loop list

list_angka = [1,4,6,3,5,4,3,4,2]

panjang = len(list_angka)
while i < panjang:
    print(f"angka = {list_angka[i]}")
    i +=1

# list comprehension

list_angka = [1,4,6,3,5,4,3,4,2]

[print(f"angka = {i}") for i in list_angka] #list comprehension

# enumerate

list_angk = ["bahul",1,"kocak",4]

for index,data in enumerate(list_angk):
    print(f"index = {index}, data {data}")

    