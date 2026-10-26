nama = input("masukkan nama anda :")
umur = input("masukkan umur anda ")
alamat = input("masukkan alamat anda")

print("======output======")

print("nama anda :", nama)
print("umur anda :", umur)
print("alamat anada :", alamat)

# tipe data integegr, bilangan bulat
a =10
print("nilai a :", a)
print(" tipe data a :, type(a)")

# tipe data string, tulisan
b ="izza" 
print("nilai b :", (b))
print("tipe data b :", (b))

# tipe data float bilangan pecahan
c = 10.5
print("nilai c :",c)
print("tipe data c :, type (c)")
# tipe data bolean 
d = True
print("nilai d :",d)
print ("tipe data d :, type(d)")




print("================================")
print("    IDENTITAS MAHASISWA")
print("================================")

nama = input(" Masukkan Nama        : ")
nim = input("Masukkan NIM           : ")
prodi = input("Masukkan Prodi       : ")
dua_digit_ = input("Masukkan 2 Digit NIM  :")

nim_int = int(nim)
dua_digit_int = int(dua_digit_)

print("================================")
print("     HASIL PROGRAM")
print("================================")
print(f"\nNama        : {nama}")
print(f"NIM           : {nim_int}")
print(f"Prodi         : {prodi}")
print(f"2 Digit NIM   : {dua_digit_int}")

print(f"\nTipe Data Nama: {type(nama)}")
print(f":Tipe Data NIM : {type(nim_int)}")
print(f"Tipe Data Prodi : {type(prodi)}")
print(f"Tipe Data 2 Digit NIM : {type(dua_digit_int)}")
print("================================")