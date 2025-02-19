def menu():
    print("===========================")
    print("        MENU PILIHAN       ")
    print("===========================")
    print("1. Nilai ")
    print("2. Perulangan ")
    print("3. Keluar")
    print("===========================")

def perulangan():
    print("\n==========Perulangan==========")
    mulai = int(input("Masukkan Awal : "))
    akhir = int(input("Masukkan Akhir : "))
    kelipatan = int(input("Masukkan Kelipatan : "))
    for a in range(mulai,akhir,kelipatan):
        print(a)
    menu()

def nilai():
    print("=======================")
    print("     Nilai Mahasiswa   ")
    print("=======================")
    input("Masukkan Nama : ")
    input("Masukkan Kelas : ")
    input("Masukkan NPM : ")
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    total = (uts+uas)/2
    print("Rata-rat Nilai",total)


    if total >= 90:
        print("Grade A")
    elif total >=80:
        print("Grade B")
    elif total >= 70:
        print("Grade C")
    else:
        print("Remedial")
    menu()
menu()

while 1:
    print()
    pilih = int(input("Masukkan Pilihan = "))

    if pilih == 1:
        nilai()
    elif pilih == 2:
        perulangan()
    elif pilih == 3:
        print("===========================")
        print("Terima Kasih")
        break
    else:
        print("Maaf pilihan tidak terdaftar")
        print("Coba lagi ? [Y/N]")
        coba = input().upper()
        if coba == "Y":
            menu()
        else:
            print("")
            break
                
