#Rumus
import os


def rumus():
    print("1 = Rumus Persegi Panjang\n2 = Rumus Persegi\n3 = Persegi\n4 = Jajar Genjang\n5 = Layang-Layang\n6 = Belah Ketupat\n7 = Trapesium\n8 = Lingkarang")
    pilihan_user = int(input("Pilih angka: "))
    
    if pilihan_user == 1: #PERSEGI PANJANG
        print("MENGHITUNG LUAS & KELILING PERSEGI PANJANG")
        panjang = float(input("\nMasukan Panjang: "))
        lebar = float(input("Masukan Lebar: "))
        luas = panjang*lebar
        keliling = 2 * (panjang+lebar)
        print("\nLuas Persegi Panjang \t\t:",luas)
        print("Keliling Persegi Panjang\t:",keliling)
        
    elif pilihan_user == 2: #PERSEGI
        print("MENGHITUNG LUAS & KELILING PERSEGI")
        sisi = float(input("\n Masukan Sisi: "))
        luas = sisi**2
        keliling = 4 * sisi
        print("\nLuas Persegi \t\t: ", luas)
        print("Keliling Persegi\t: ", keliling)
    elif pilihan_user == 3: #SEGITIGA
        print("MENGHITUNG LUAS & KELILING SEGITIGA")
        alas = int(input("Masukan Alas: "))
        tinggi = int(input("Masukan Tinggi: "))
        luas = 1/2*alas*tinggi
        sisi = int(input("Masukan sisi: "))
        keliling = sisi**3
        print("\nLuas Segitiga \t\t: ", luas)
    elif pilihan_user == 4: #JAJAR GENJANG
        print("MENGHITUNG LUAS & KELILING JAJAR GENJANG")
        alas = int(input("Masukan Alas: "))
        tinggi = int(input("Masukan Tinggi: "))
        sisi1 = int(input("Masukan sisi 1: "))
        sisi2 = int(input("Masukan sisi 2: "))
        luas = alas*tinggi
        keliling = 2*(sisi1+sisi2)
        print("\nLuas Jajar Genjang \t\t: ", luas)
        print("Keliling Jajar Genjang\t: ", keliling)
    elif pilihan_user == 5: #Layang-Layang
        print("MENGHITUNG LUAS & KELILING Layang-Layang")
        d1 = int(input("Masukan D1: "))
        d2 = int(input("Masukan D2: "))
        sisi_a = int(input("Masukan Sisi A: "))
        sisi_b = int(input("Masukan Sisi B: "))
        luas = 1/2*d1*d2
        keliling = 2*(sisi_a+sisi_b)
        print("\nLuas Layang-Layang \t\t: ", luas)
        print("Keliling Layang-Layang\t: ", keliling)
    elif pilihan_user == 6: #Belah Ketupat
        print("MENGHITUNG LUAS & KELILING Belah Ketupat")
        d1 = int(input("Masukan D1: "))
        d2 = int(input("Masukan D2: "))
        sisi = int(input("Masukan Sisi: "))
        luas = 1/2*d1*d2
        keliling = 4*sisi
        print("\nLuas Belah Ketupat \t\t: ", luas)
        print("Keliling Belah Ketupat\t: ", keliling)
    elif pilihan_user == 7: #Trapesium
        print("MENGHITUNG LUAS & KELILING Trapesium")
        a = int(input("Masukan A: "))
        b = int(input("Masukan B: "))
        c = int(input("Masukan C: "))
        d = int(input("Masukan D: "))
        tinggi = int(input("Masukan Tinggi: "))
        luas = 1/2*(a+c)*tinggi
        keliling = a + b + c + d
        print("\nLuas Trapesium \t\t: ", luas)
        print("Keliling Trapesium\t: ", keliling)
    elif pilihan_user == 8: #Lingakaran
        print("MENGHITUNG LUAS & KELILING Lingkaran")
        phi = 3,14
        r = int(input("Masukan jari-jari (r): "))
        luas = phi*r*r
        keliling = 2*phi*r
        print("\nLuas Lingkaran \t\t: ", luas)
        print("Keliling Lingkaran\t: ", keliling)
    elif pilihan_user == "0":
        return None

os.chdir(r"D:\!Coding\Python\Video_Bakat")
while True:
    print("\n1 = Calculator\n2 = Rumus Bangun Datar\n")
    x = input("Pilih (input1): ")
    os.system("cls")
    if x == "1":
        os.system("python calculator.py")

    elif x == "2":
        rumus()

    #print (os.getcwd())
    # os.system("python calculator.py")
    #        rumus()
    # elif x == "2":
    #     calculator()
    else:
        print("Nilai yang kamu masukan tidak valid.")