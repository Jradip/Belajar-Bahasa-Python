def nilai():
    print()
    print("="*20)
    print("   Nilai Mahasiswa  ")
    print("="*20)
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilia UAS : "))
    total = (uts + uas) /2
    print("Rata-Rata",total)

def data():
    print("="*20)
    print("   Data Mahasiswa  ")
    print("="*20)
    nama = input("Nama : ")
    kelas = input("Kelas : ")
    npm = input("NPM : ")
    print(f"\nMahasiswa dengan nama {nama} dari kelas {kelas} dengan no NPM {npm} telah mengikuti ujuan")
    nilai()
data()

