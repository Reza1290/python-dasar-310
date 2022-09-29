#A
from re import X


print("ini adalah string")
print('ini adalah string')

print("C:\\newmember") #gunakan backslash untuk menghilangkan command
print("adadada\t adadadada")
print(r'dawdawwdawda') # r = raw 
print("""ASIAP
adadadadadadadadaadad
adadadd""") # Petik tiga buat bikin kolom tanpa \n

# OPERASI STRING

# Penambahan

x = " aku"
y = " suka"
z = " T"

sambung = x + y + z
print("jika disambung menjadi",str(sambung))

# Menghitung jumlah string ( panjang string )

x = " aku"
y = " suka"
z = " T"

sambung = x + y + z
print("panjang semua ", sambung, len(sambung))

# Mencari tahu apakah termasuk kedalam string atau tidak gunakan ( status )


T = "T"
status = T in sambung

print("apakah", T , "ada di", sambung, "jawaban = ", status )

#pengulangan string

badut = sambung*3
print(badut)

# indexing >>>> [number] 0 hingga tak hingga 

print("index number 1", sambung[1])
print("index number 2", sambung[2])
print("index number 7", sambung[7])

# mencari nilai terkecil

print("nilai terkecil dari kata", sambung , "adalah", min(sambung))

# mencari nilai terbesar

print("nilai terbesar dari kata", sambung, "adalah", max(sambung))

# mencari tahu besaran sebuah angka huruf dalam sebuah kata ( min max ) ASCII

ascii_code = ord("T")

print("nilai ASCII codemu sebesar", str(ascii_code) )# char to code

print(type(ascii_code))

data = 111

print("nilai ASCII codemu sebesar", chr(data))

# mencari berapa banyak sebuah angka atau huruf pada kalimat
jumlah = sambung.count("a")
print(jumlah)

jumlah = "asiap santuy".count("a")

print(jumlah)


# prat 2 operator method
# convert normal to lowercase

normal = "aku sayang T"
print("lowernya " + normal.lower())

normal2 = "aku sayang T "
print("uppernya ", normal2.upper())

# pengecekan lower upper dengan is, methode
normal3 = "AKU SAYANG KAMU"
normal4 = "aku sayang kamu"

print("afakah", normal3 , "lower?", normal3.islower())
print("afakah", normal4 , "upper?", normal4.isupper())

print("afakah", normal3 , "upper?", normal3.isupper())
print("afakah", normal4 , "lower?", normal4.islower())

# apakah terdapat huruf? isalpha
teks = "abcde1234"
print("afakah terdapat semuanya (huruf, huruf angka, angka, spasi)")
print(teks.isalpha())
print(teks.isalnum())
print(teks.isdecimal())
print(teks.isspace())

# mengecek judul apakah besar semua depannya istitle

judul = "Aku Sayang Dirinya Bismillah Jadi Istri"
print("apakah kata depan huruf besar?", judul.istitle())

# ngecek sebuah komponen apakah dimulai sebuah kata x ( startswith)
## atau diakhiri dengan kata y ( endswith )

judul2 = "Kamu Badut Dek"

print(judul2,"diawali dengan Kamu?", judul2.startswith("Kamu"))

print(judul2,"diakhiri dengan Dek?", judul2.endswith("Dek"))

# penggabungan komponen , join() split() PADA SEBUAH LIST list = []

inilist = ['Apel','Mangga','Jeruk']


y = "+"
print(y.join(inilist))

gabungan = "akuehmsayangehmkamuehmbanget"
print(gabungan.split('ehm'))

# Mempersimple hidup asiap ( justify ) rjust ljust center

teks1 = "Kamu Cantik"
print("|",teks1.rjust(20),"|")
print("|",teks1.center(20),"|")
print("|",teks1.ljust(20),"|")
#mengganti spasi dengan character

print("|",teks1.center(20,"="),"|")

# strip kebalikannya ngilangin tanda characternya

teks2 = teks1.center(20,"=")
print(teks2.strip("="))











