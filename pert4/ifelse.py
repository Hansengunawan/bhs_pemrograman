#if else in python

def login():
    print("="*100)
    print("{:^100}".format("Silahkan Login"))
    print("="*100)
    user=input("Username : ")
    pw=input("Password : ")

    if user == "Hansen" and pw == "hansen":
        print("Login Berhasil")
        AKADEMIK()
    else:
        login_salah() 
    
def login_salah():
    print("")
    print("Username/Password Salah\n""Silahkan Coba Lagi")
    print("")
    login()

def AKADEMIK() :
    print("")
    print("1. Data")
    print("2. Perkuliahan")
    print("3. Registrasi Semester")
    print("4. Daftar Nilai")
    print("5. Exit Program")
    x = input("=>> : ")

    if x == "1" : 
        data()
    elif x == "2" :
        Perkuliahan()
    elif x == "3" :
        Registrasi_Semester()
    elif x == "4" :
        Daftar_Nilai()
    elif x == "5":
        exit()
    else :
        print("Coba Lagi")
        AKADEMIK()
        
def data(): 
    print("1. Biodata Mahasiswa")
    print("2. Tagihan Mahasiswa")
    print("3. Surat Keterangan Lulus")
    print("4. Back")
    x = input("=>> : ")
   
    while True:
        if x == "1" : 
            Biodata_Mahasiswa()
        elif x == "2" :
            Tagihan_Mahasiswa()
        elif x == "3" :
            SKL()
        elif x == "4":
            AKADEMIK()
        break
        

def Perkuliahan():
    print("1. Kurikulum")
    print("2. Kegiatan Akademik")
    print("3. Back")
    x =int(input(">>= : "))
    if x == 1:
        kurikulum()
    elif x == 2:
        KA()
    elif x == 3:
        AKADEMIK()
    else:
        Perkuliahan()
   
def Registrasi_Semester():
    print("1. KRS")
    print("2. Jadwal Kuliah")
    print("3. Absensi Kuliah")
    print("4. Quisioner")
   
def Daftar_Nilai():
    print("1. KHS")
    print("2. Kemajuan Belajar")
    print("3. Riwayat Mengulang")
    print("4. Resume Nilai")

def Biodata_Mahasiswa():
    n="Hansen"
    nim="20210801355"
    se="semester 3"
    print("{:^100}".format(n),"\n")
    print("{:^100}".format(nim),"\n")
    print("{:^100}".format(se),"\n")
    data()

def Tagihan_Mahasiswa():
    t=1800000
    s=6
    total=t*s
    print("Total Tagihan yang harus dibayar :", total)
    data()

def SKL():
    skl=int(input("Masukkan semester berapa : "))
    if skl == 8:
        print("Sedang dimuat")
    else:
        print("Belum lulus")     
    data()

def kurikulum():
    smt=int(input("Masukkan Semester berapa : "))
    data_smt1=("- Algoritma\n""- Dasar Sistem Informasi\n""- Aljabar Linier\n")
    data_smt2=("- Struktur Data\n""- Kalkulus 1\n""- Desain dan Analisis Algo\n")
    data_smt3=("- Basis Data\n""- Kalkulus 2\n""- Bahasa Pemrograman\n")
    if smt == 1:
        print(data_smt1)
    elif smt == 2:
        print(data_smt2)
    elif smt == 3:
        print(data_smt3)
    else:
        print("bntr")
    Perkuliahan()

def KA():
    print("SKRIPSI")
    smt=int(input("Masukkan semester berapa : "))
    if smt == 7:
        print("Cicil skripsi")
    elif smt == 8:
        print("Skripsian")
    else:
        Perkuliahan()
    Perkuliahan()
login()