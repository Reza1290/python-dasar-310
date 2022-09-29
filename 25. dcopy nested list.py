
#deep Copy LIST

from copy import deepcopy


list1 = [1,2]
list2 = [3,4]

listgab = [list1,list2]

print(listgab) 

#pemanggilan permunculan

print(f"angka ke- 1 \t\t = {listgab[0]}")
print(f"list ke -1 urutan 1\t = {listgab[0][0]}")

listgab_copy = listgab.copy()
listgab_copy[1][1] = 5

print(f"angka sudah di copy = {listgab_copy}")
print(listgab, "belum di deep copy")

# dalem banget copynya
deepcopy(listgab)
listgab[1][1] = 9
print(listgab, "sudah di deep")





