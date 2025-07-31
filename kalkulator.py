# num1 = input("Masukkan angka pertama :")
# num2 = input("Masukkan angka kedua :")

# result= float(num1) + float(num2)

# print(result)

num1 = input("Masukkan angka pertama anda :")
num2 = input("Masukan angka kedua anda :")

pilihan = input("Masukkan pilihan anda   |+|   |-|   |/|   |*|  :" )

pertambahan = float(num1) + float(num2)
pengurangan = float(num1) - float(num2)
pembagian = int(num1) / int(num2)
perkalian = float(num1) * float(num2)

if pilihan == "|+|" :
    print(pertambahan)
elif pilihan == "|-|" :
    print(pengurangan)
elif pilihan == "|*|" :
    print(perkalian)
elif pilihan == "|/|" :
    print(pembagian)
else :
    print("Tidak ada di pilihan bro")
