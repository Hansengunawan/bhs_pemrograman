# function
def data():
    nama = "Hansen"
    jurusan = "Teknik Informatika"
    matkul = "UAS Bahasa Pemrograman"

    print(nama)
    print(jurusan)
    print(matkul)
    print("")
#contoh rekursif 
    def pangkat ():
        print("Contoh Pangkat")
        x = int (input("Masukkan bilangan pertama : "))
        y = int (input("Masukkan bilangan kedua : "))
        print("Hasilnya adalah = ",(x**y))
    pangkat()#ini adalah rekursif

    def faktorial(nilai):
        if nilai == 1:
            return nilai;
        else:
            return (nilai*faktorial(nilai-1))
    print("\nContoh Faktorial")
    bil = int(input("Masukan Bilangan : "))

    print("%d! = %d" % (bil, faktorial(bil)))
    
data() #ini adalah rekursif


