# nested list , list didalam list

# misal 

user_1 = ["wagyu", 15,"L"]
user_2 = ["burhan", 20,"L"]
user_3 = ["budi", 21,"L"]

semua_user = [user_1,user_2,user_3]

print(f"semua user {semua_user}\n")

for alluser in semua_user:
    print(f"Nama \t = {alluser[0]}") # 0 menandakan urutan ke 0
    print(f"Umur \t = {alluser[1]}") # 1 menandakan urutan ke 0
    print(f"Gender \t = {alluser[2]}\n") # 2 menandakan urutan ke 0
    
# jika di copy >

semua_copy = semua_user.copy()

print(semua_user)

semua_copy[1] = "rudi"
print(semua_user) # nothing change because bukan list yang
# didalem cuman permukaan > list 1>[list 2 >[]]
