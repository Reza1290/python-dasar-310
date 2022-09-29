# function dengan argumen

from binascii import b2a_base64


def hello_world(nama):
    print(f"Halo Kamu{nama}")
    # di dalam kurung adalah argumen ( arg )


hello_world(" Budi Gaming") #sesuatu yang ada didalam kurung akan di convert 
#menjadi argumen (nama)
#menggunakan list
nama = ["udin","petot"]

hello_world(nama)

nama = {
    "1":"udin",
    "2":"petot",
}

hello_world(nama)
hello_world(nama.keys())
hello_world(nama.values())

# argumen untuk looping bisa juga

def pertambahan(a,b):
    c = a + b
    print("hasil : ",c)

pertambahan(1,2)

f = int(input("a : "))
g = int(input("b : "))
pertambahan(f,g)
