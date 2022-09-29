# mempermudah pemanggilan dengan format f"text {data}"

datalist = 'ayam','bebek','angsa'

print(f"data hewan {datalist}")

angka = 200.4

print(f"angka {angka}")

angka_desimal = 200.4313131

print(f"angka {angka:.3f}")

# berlaku petik triplets dan line standar multiline
judul = "BIODATA"
data_nama = "reza"
data_umur = 18
data_dom = "indonesia"


print("\n",judul.center(15,"="))
print(f"""
nama = {data_nama}
umur = {data_umur}
dom = {data_dom}"""
 )
