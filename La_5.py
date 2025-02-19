data = []
def masukkanData():
    print("=====Masukkan Data=====")
    i = 0
    banyakData = int(input(f"Masukkan Banyak Data : "))
    while i < banyakData:
        dataBaru = input(f"Masukkan data ke - {i}: ")
        data.append(dataBaru)
        i += 1
    tambahData()

def tambahData():
    print("=====Tambah Data=====")
    i = 0
    banyaktmbhData = int(input("Banyaknya tambah data : "))
    while i < banyaktmbhData:
        tambah = int(input(f"Tambah Data ke -{i}: "))
        data.append(tambah)
        i += 1
    hapusData()

def hapusData():
    print("=====Hapus Data=====")
    i = 0
    bnykhpsdata = int(input("Banyaknya hapus data : "))
    while i < bnykhpsdata:
        hapus = int(input("Hapus data ke - : "))
        data.remove(data[hapus])
        i += 1
    cetakData()

def cetakData():
    print("=====Cetak Data=====")
    print(f"Isi data adalah : {data}")

masukkanData()