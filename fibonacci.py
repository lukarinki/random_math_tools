#Program Fibonacci
def fibonacci():    
    suku_n = int(input("Masukan n: "))
    n1, n2 = 0, 1
    awal = 0

    # cek apakah nilai suku valid
    if suku_n <= 0:
        print("masukan angka lebih dari 0: ")
    # elif suku_n == 1:
    #    print(n1)
    else:
        print("Deret Fibonacci:")
        while awal < suku_n:
            print(n1)
            n = n1 + n2
            n1 = n2
            n2 = n
            awal += 1
            
fibonacci()
