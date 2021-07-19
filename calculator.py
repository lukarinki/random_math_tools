import random


def penjumlahan(x, y):
        return x + y

def pengurangan(x, y):
        return x - y

def perkalian(x, y):
        return x * y

def pembagian(x, y):
        return x / y

def modulus(x, y):
        return x % y

while True:
    pilih = input("Pilih operator (+, -, *, /, %): ")
        
    if pilih in ('+', '-', '*', '/', '%'):
        angka1 = int(input("Masukan angka: "))
        angka2 = int(input("Masukan angka: "))
            
        if pilih == "+":
            print(angka1, "+", angka2, "=", penjumlahan(angka1, angka2))
            break
        elif pilih == "-":
            print(angka1, "-", angka2, "=", pengurangan(angka1, angka2))
            break
        elif pilih == "*":
            print(angka1, "*", angka2, "=", perkalian(angka1, angka2))
            break
        elif pilih == "/":
            print(angka1, "/", angka2, "=", pembagian(angka1, angka2))
            break
        elif pilih == "%":
            print(angka1, "%", angka2, "=", modulus(angka1, angka2))
            break
        else:
            print("Tidak Valid.")

