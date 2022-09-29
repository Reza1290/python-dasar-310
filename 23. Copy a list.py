# copy lsit (duplikat)

a = ["rudi","budi","agus"]

print(f"a = {a}")

b = a

print(f"b = {b}")

# same address

b.sort()

print(f"a = {a}")
print(f"b = {b}")

# same memory

print(f"b = {hex(id(b))}")
print(f"a = {hex(id(a))}")

a[1] = "badut"
print(f"a = {a}")
print(f"b = {b}") 

# gimana biar adressnya gasama?
# gunakan copy() > maka c = a.copy()

c = a.copy()

print(f"a = {hex(id(a))}")
print(f"b = {hex(id(b))}")
print(f"c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")

c[1] = "rubi" # disaat di ganti yang a tidak terpengaruh
# karena beda address   

print(f"c = {c}")

