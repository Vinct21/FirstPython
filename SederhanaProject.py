
# judul
print("Menentukan Grade Nilai Siswa")

# Input Nama
Nama = input("Masukan Nama Siswa : ")
print("Selamat datang",Nama)

# Input Nilai Tugas, UTS, dan UAS
nilai_tugas = float(input("Masukan Nilai Tugas : "))
nilai_uts = float(input("Masukan Nilai UTS : "))
nilai_uas = float(input("Masukan Nilai UAS : "))

nilai_total = (0.20*nilai_tugas) + (0.30*nilai_uts) + (0.50*nilai_uas)

# Validasi Grade Nilai 
if nilai_total >= 90:
    grade = "A"
elif nilai_total >= 85:
    grade = "A-"
elif nilai_total >= 80:
    grade = "B+"
elif nilai_total >= 75:
    grade = "B"
elif nilai_total >= 70:
    grade = "B-"
elif nilai_total >= 65:
    grade = "C"
elif nilai_total >= 50:
    grade = "D"
elif nilai_total >= 0:
    grade = "E"

if nilai_total >=75:
    ucap = "Selamat anda lulus"
else:
    ucap = "Anda tidak lulus"

# Menampilkan Output

print("\nNama : ",Nama)
print("Total Nilai : ",nilai_total)
print("Grade : ",grade)
print(ucap)