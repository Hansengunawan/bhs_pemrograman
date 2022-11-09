
def login():
    nama= "Hansen"
    nim=20210801355
    print("="*100)
    print("{:^100}".format("CAPTEH"))
    print("="*100)
    print("")
    print("Nama :", nama)
    print("NIM :", nim)

while True:
    def menu():
        harga_cap=5000
        harga_teh=5500
        print("1. Harga Capucino : ",harga_cap)
        print("2. Harga Teh : ",harga_teh)
        x=int(input("\nMasukkan pilihan anda : "))
        y=int(input("Ingin beli berapa? : "))
        if x == 1:
            print("Segera membuat pesanan anda!")
            if y == 1:
                b=harga_cap*y
                a=b*10/100
                print("Total Harga : ",b)
                print("Total PPN : ",a)
                print("Jumlah yang harus dibayar : ",a+b)
                print("="*100)
                print("{:^100}".format("Terimakasih telah membeli!"))
                print("="*100)
            else:
                print("Total harga yang harus dibayar : ", harga_teh*y)
                print("="*100)
                print("{:^100}".format("Terimakasih telah membeli!"))
                print("="*100)
        elif x == 2:
            print("Segera membuat pesanan anda!")

    def jual():
        print("\nPilihan")
        print("1. Capucino")
        print("2. Teh")
        print("3. Exit\n")
        x =int(input("Masukkan pilihan :"))
        if x == 1:
            menu()
        elif x == 2:
            menu()
        elif x == 3:
            print("\nTerimakasih telah membeli!")
    
    login()
    jual()
    menu()