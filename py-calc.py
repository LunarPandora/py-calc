# Created on Tue, September 22, 2021
# Author : WendyYansah

# Sebelum memulai, ada beberapa function yang telah kita tuliskan di file terpisah.
# Untuk meng-include function yang telah kita tuliskan, panggil file tersebut kedalam project ini.

import calc_function as operasi

# Kita akan memulai program ini dengan menambahkan beberapa variable terlebih dahulu.

a = 0
b = 0
    
# Mari kita coba nyatakan dulu 2 variable diatas bernilai 0
# Lalu, mari kita tampilkan menu kalkulator yang dapat diakses oleh user.

print("""
Selamat datang!
Silahkan pilih operasi yang ingin anda gunakan.      

1. Operasi penambahan (+)
2. Operasi pengurangan (-)
3. Operasi perkalian (*)
4. Operasi pembagian (/)
5. Operasi perpangkatan (^)
""")

# Setelah itu, berikan input yang dapat diisi oleh user untuk memilih operasi yang telah disediakan.

pilihan = input("Pilih operasi sesuai dengan nomor yang telah dicantumkan : ")

# Mari kita susun alur menu dalam program ini
# Jika user memilih angka yang sesuai, maka jalankan function yang sesuai pula.
# Lalu, minta user untuk mengisikan angka yang ingin dioperasikan, lalu masukkan ke a dan b.
# Setelah itu, panggil function yang sesuai dan masukkan nilai a dan b tersebut ke parameter yang telah disediakan.

if pilihan == "1":
    a = input("Masukkan nilai pertama (a) : ")
    b = input("Masukkan nilai kedua (b) : ")
    
    operasi.pertambahan(a, b)
    
elif pilihan == "2":
    a = input("Masukkan nilai pertama (a) : ")
    b = input("Masukkan nilai kedua (b) : ")
    
    operasi.pengurangan(a, b)
    
elif pilihan == "3":
    a = input("Masukkan nilai pertama (a) : ")
    b = input("Masukkan nilai kedua (b) : ")
    
    operasi.perkalian(a, b)
    
elif pilihan == "4":
    a = input("Masukkan nilai pertama (a) : ")
    b = input("Masukkan nilai kedua (b) : ")
    
    operasi.pembagian(a, b)
    
elif pilihan == "5":
    a = input("Masukkan nilai pertama (a) : ")
    b = input("Masukkan nilai kedua (b) : ")
    
    operasi.perpangkatan(a, b)
    
else:
    # Jika user tidak memasukkan input sesuai dengan yang telah dicantumkan di menu, maka akhiri program.
    print("Mohon menginputkan angka yang sesuai dengan yang telah ditentukan di menu operasi.")