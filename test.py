angka_1 = float(input("masukan angka pertama: "))
operator = str(input("pilih operator +, -, *, /: "))
angka_2 = float(input("masukan angka kedua: "))

tambah = angka_1 + angka_2
kurang = angka_1 - angka_2
kali = angka_1 * angka_2
bagi = angka_1 / angka_2

if operator == "+":
    print(tambah)
elif operator == "-":
    print(kurang)
elif operator == "*":
    print(kali)
elif operator == "/":
    print(bagi)
else:
    print("masukan input dengan benar")

print("Program selesai")