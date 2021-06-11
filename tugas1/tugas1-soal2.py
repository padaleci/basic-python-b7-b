x = (22/7)
y = int(input("Jari-jari dari lingkaran = "))
hasil = (x*y*y)
print("Luas lingkaran dari jari-jari", y, "cm adalah", hasil, "cm²")

value = hasil
formatted_string = "{:.2f}".format(value)
float_value = float(formatted_string)
print("Hasil luas diubah menjadi hanya 2 angka dibelakang koma adalah",float_value)
