def menulisData():
    print("=====Menulis Data Ke File=====")
    file = open('data.txt','w')
    tanya = int(input("\nMasukkan banyak data : "))
    print('')
    for j in range(1, tanya + 1):
        print(f"\tdata ke-{j}")

        nama = input("Nama Anda : ")
        kelas = input("Kelas Anda : ")
        npm = input("NPM Anda : ")
        jurusan = input("Jurusan Anda : ")

        file.write(nama + '\n')
        file.write(kelas + '\n')
        file.write(npm + '\n')
        file.write(jurusan + '\n')
        print("Data telah dimasukkan ke dalam file.txt\n")
        file.close()
    
def bacaData():
    print("=====Membaca Data File=====")
    file = open("data.txt",'r')
    nama = file.readline()
    while nama:
        kelas = file.readline()
        npm = file.readline()
        jurusan = file.readline()

        nama = nama.rstrip()
        kelas = kelas.rstrip()
        npm = npm.rstrip()
        jurusan = jurusan.rstrip()

        print("\nMembaca Data yang ada di dalam data.txt")
        print(f"Nama    :{nama}")
        print(f"Kelas   :{nama}")
        print(f"NPM     :{nama}")
        print(f"Jurusan :{nama}")
        nama = file.readline()
        file.close()

def main():
    menulisData()
    bacaData()
main()