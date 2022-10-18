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
    print("Coba Lagi")
    login()

def AKADEMIK() :
    print("1. Data")
    print("2. Perkuliahan")
    print("3. Registrasi Semester")
    print("4. Daftar Nilai")
    x = input("=>> : ")

    if x == "1" : 
        data()
    elif x == "2" :
        Perkuliahan()
    elif x == "3" :
        Registrasi_Semester()
    elif x == "4" :
        Daftar_Nilai()
    else :
        print("Coba Lagi")
        AKADEMIK()
    

def data(): 
    print("1. Biodata Mahasiswa")
    print("2. Tagihan Mahasiswa")
    print("3. Surat Keterangan Lulus")
   

def Perkuliahan():
    print("1. Kurikulum")
    print("2. Kegiatan Akademik")
   

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

    
login()