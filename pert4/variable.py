#Variable
a, b =5, 10
penjumlahan = a+b
print("Hasil dari a+b = ", penjumlahan)

def penjumlahan ():

    a=int(input("masukkan angka pertama : "))
    b=int(input("masukkan angka kedua : "))
    c=a+b
    print(c)

while True:
    print("1. Menu")
    print("2. Penjumlahan")
    print("3. Exit")
    choice = int(input("pilihanmu :"))
    if choice == 2 :
        penjumlahan()
    elif choice == 3:
        break
    else:
        print("Pilih Kembali")