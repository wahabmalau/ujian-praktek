print("TRANSAKSI TOKO")


nama_barang = input("Masukkan nama barang: ")

stok = int(input("Masukkan jumlah stok awal: "))

print("\nData barang berhasil disimpan!")
print("Nama Barang :", nama_barang)
print("Stok Awal   :", stok)


while True:
    print("MENU TRANSAKSI")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Cek Stok")
    print("4. Keluar")

    pilihan = input("Pilih transaksi (1-4): ")

   
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah barang masuk: "))

        if jumlah > 0:
            stok = jumlah
            print("Barang berhasil ditambahkan!")
        else:
            print("Jumlah harus lebih dari 0!")

    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah barang keluar: "))

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
        elif jumlah > stok:
            print("Stok Tidak Mencukupi!")
        else:
            stok -= jumlah
            print("Barang berhasil dikeluarkan!")


    elif pilihan == "3":
        print("\nNama Barang :", nama_barang)
        print("Jumlah Stok :", stok)

   
    elif pilihan == "4":
        print("       TRANSAKSI SELESAI")
        print("Nama Barang :", nama_barang)
        print("Sisa Stok   :", stok)
        print("Terima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak valid! Silakan coba lagi.") 





TRANSAKSI TOKO
Masukkan nama barang: tepung
Masukkan jumlah stok awal: 10

Data barang berhasil disimpan!
Nama Barang : tepung
Stok Awal   : 10
MENU TRANSAKSI
1. Barang Masuk
2. Barang Keluar
3. Cek Stok
4. Keluar
Pilih transaksi (1-4): 2
Masukkan jumlah barang keluar: 5
Barang berhasil dikeluarkan!
