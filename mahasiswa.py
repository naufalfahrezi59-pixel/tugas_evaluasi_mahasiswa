print("=== SISTEM EVALUASI MAHASISWA ===")
nama = "Naufal Fahrezi"
tugas = 90
uts = 90
uas = 90
kehadiran = 100
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)


print("\n=== HASIL EVALUASI ===")
print("Nama mahasiswa:", nama)
print("Nilai tugas:", tugas)
print("Nilai UTS:", uts)
print("Nilai UAS:", uas)
print("Kehadiran:", kehadiran, "%")
print("Nilai akhir:", nilai_akhir)


if nilai_akhir >= 75 and kehadiran >= 80:
    if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
        print("Status: LULUS DENGAN PREDIKAT")
    else:
        print("Status: LULUS")
else:
    print("Status: BELUM LULUS")
