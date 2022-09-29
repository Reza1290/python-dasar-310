# Program Konverter Suhu 07/07/2022

print("\n Selamat Datang Di Kalkulator Suhu\n")

celsius = float(input("Masukkan Suhu dalam Celsius = "))

print("Suhu dalam satuan Celsius =", celsius,)

reamur = (4/5) * celsius
print("suhu dalam reamur adalah", reamur)

fahrenheit = ((9/5) * celsius) + 32
print("suhu dalam fahrenheit", fahrenheit)

kelvin = celsius + 273
print("suhu dalam kelvin", kelvin)

print(" \nKalkulator Reamur \n")

reamur = float(input("masukkan nilai reamur = "))
print("suhu dalam reamur", reamur)

celsius = (5/4) * reamur
print("suhu dalam celsius", celsius)

fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit", fahrenheit)

kelvin = ((5/4) * reamur + 273 )
print("suhu dalam kelvin", kelvin)

# Fahrenheit

print("\nKovereter Fahrenheit\n")

fahrenheit = float(input("masukkan fahrenheit"))
print("suhu dalam F", fahrenheit)

celsius = (5/9) * (fahrenheit - 32)
print("suhu dalam c", celsius)

reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam r", reamur)

kelvin = (5/9) * (fahrenheit - 32) + 273
print("suhu dalam k", kelvin)

#Kelvin

print("\nKalkulator Kelvin \n")
kelvin = float(input("masukkan kelvin = "))

celsius = kelvin - 273
print("suhu dalam kelvin", kelvin)

reamur = (celsius * 4/5)
print("suhu dalam reamur", reamur)

fahrenheit = (celsius * (9/5)) + 32 
print("suhu dalam fahrenheit",fahrenheit)

