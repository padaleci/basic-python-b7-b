a = int(input("Masukkan nilai ujian teori: "))
b = int(input("Masukkan nilai ujian praktek: "))
c = int(70)

if a >= c & b >= c:
    print("Selamat, anda lulus!")
if a < c:
    print("Anda harus mengulang ujian teori")
if b < c:
    print("Anda harus mengulang ujian praktek")
else:
    print("Selamat, anda lulus!")