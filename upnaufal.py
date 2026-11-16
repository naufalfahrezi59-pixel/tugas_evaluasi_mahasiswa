# APLIKASI PEMBAYARAN PARKIR KENDARAAN

print("========================")
print("APLIKASI PARKIR KAMPUS")
print("========================")

# Input jumlah kendaraan
jumlah_kendaraan = int(input("Masukkan jumlah kendaraan: "))

total_semua = 0

# Perulangan kendaraan
for i in range(jumlah_kendaraan):

    print("\nKendaraan ke-", i + 1)
    print("1. Sepeda Motor")
    print("2. Mobil")
    print("3. Bus")

    jenis = input("Pilih jenis kendaraan (1/2/3): ")
    lama = int(input("Masukkan lama parkir (jam): "))

    # Percabangan tarif
    if jenis == "1":
        nama = "Sepeda Motor"
        tarif = 2000

    elif jenis == "2":
        nama = "Mobil"
        tarif = 5000

    elif jenis == "3":
        nama = "Bus"
        tarif = 10000

    else:
        print("Jenis kendaraan tidak valid!")
        continue

    # Menghitung biaya parkir
    biaya = tarif * lama

    # Percabangan biaya tambahan
    if lama > 5:
        tambahan = 5000
    else:
        tambahan = 0

    # Total pembayaran
    total = biaya + tambahan
    total_semua = total_semua + total

    # Tampilan hasil
    print("\n========== STRUK PARKIR ==========")
    print("Jenis kendaraan :", nama)
    print("Lama parkir      :", lama, "jam")
    print("Tarif parkir     : Rp", tarif)
    print("Biaya parkir     : Rp", biaya)
    print("Biaya tambahan   : Rp", tambahan)
    print("Total pembayaran : Rp", total)
    print("====================")

# Total seluruh kendaraan
print("\n=======================")
print("TOTAL SELURUH PEMBAYARAN")
print("Rp", total_semua)
print("Terima kasih telah menggunakan")
print("layanan parkir kampus!")
print("========================")