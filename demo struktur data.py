#tugas 1
#makanan2 = [
#   ['sate','soto','bakso'],
#    ['karih_kambing','karih_daging'],
#    ['asam',['santan',['keladi','humbut']],'bening']
#]

#a. buatlah kode program untuk mencetak "Gangan keladi dan humbut terbuat dari santan" catatan: keladi,humbut,dan santan diambil dari anggota list

#b. buatlah kode program untuk mencetak "sate,soto,dan bakso merupakan makanan yang sering dijual oleh pedagang di pasar"

#c. cetak semua anggota list pada index ke-2

#jawab

#a.
#print(f"Gangan {makanan2[2][1][1][0]} dan {makanan2[2][1][1][1]} terbuat dari {makanan2[2][1][0]}")

#Output dari program ini adalah:
#Gangan ikan dan kelapa terbuat dari bahan dasar

#b.
#for i in range(len(makanan2[0])-1):
#    print(makanan2[0][i], end=', ')
#print('dan', makanan2[0][-1], 'merupakan makanan yang sering dijual oleh pedagang di pasar')

#Output dari program ini adalah:
#sate, soto, dan bakso merupakan makanan yang sering dijual oleh pedagang di pasar

#c.
#for item1 in makanan2[2]:
#    if '[' in str(item1):
#        for item2 in item1:
#            if '[' in str(item2):
#                for item3 in item2:
#                    print(item3, end=' ')
#            else:
#                print(item2, end=' ')
#    else:
#        print(item1, end=' ')

#output
#asam santan keladi humbut bening



#tugas 2
#list1 = [10,20,[300,400,[5000,6000],500],30,40]

#a. buatlah program untuk menambahkan 7000 sebagai item baru setelah 6000.

#b. buatlah program untuk menyisipkan 5500 sebagai item baru antara 5000 dan 6000

#c. hapus item 5000 dari list

#d. buatlah program untuk menambahkan 600 sebagai item baru setelah 500

#e. tampilkan list1 

#jawab

#a. tambahkan 7000 sebagai item baru setelah 6000
#list1[2][2].append(7000)
#print(list1)

#Maka output yang dihasilkan adalah:
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

#b. sisipkan 5500 sebagai item baru antara 5000 dan 6000
#list1[2][2].insert(1, 5500)
#print(list1)

#Maka output yang dihasilkan adalah:
#[10, 20, [300, 400, [5000, 5500, 6000], 500], 30, 40]

#c. hapus item 5000 dari list
#list1[2][2].remove(5000)
#print(list1)

#Maka output yang dihasilkan adalah:
#[10, 20, [300, 400, [6000], 500], 30, 40].

#d. tambahkan 600 sebagai item baru setelah 500
#list1[2].insert(4, 600)
#print(list1)

#Maka output yang dihasilkan adalah:
#[10, 20, [300, 400, [5000, 6000, 600], 500], 30, 40]

#e. tampilkan list1
#print(list1)

#Maka output yang dihasilkan setelah dirubah list1 mulai dari point A-D
#[10, 20, [300, 400, [5500, 6000, 7000], 500, 600], 30, 40]

#Tugas 3
#list2 = [2,5,7,8,10,55,90]

#buatlah kode program untuk menampilkan list bilangan genap dan list bilangan ganjil dari list2

#contoh output:
#list bilangan genap yaitu : [2,8,10,90]
#list bilangan ganjil yaitu : [5,7,55]

#jawab
#genap = []
#ganjil = []

#for item in list2:
#    if item % 2 == 0:
#        genap.append(item)
#    else:
#        ganjil.append(item)

#print("list bilangan genap yaitu :", genap)
#print("list bilangan ganjil yaitu :", ganjil)

#Output dari program tersebut adalah sebagai berikut:
#list bilangan genap yaitu : [2, 8, 10, 90]
#list bilangan ganjil yaitu : [5, 7, 55]

#Tugas 4
#patients = [ ['Anang', 48,'male', 'smoker', 175],
#            ['Aluh', 39,'female', 'non-smoker',170],
#            ['Ani', 62,'female','smoker',150],
#            ['Tulamak',32,'female','smoker',165]]

#a. Untuk mencetak nama pasien wanita saja, dapat dilakukan dengan menggunakan perulangan dan percabangan. Berikut adalah contoh kode programnya:

#print("Daftar nama pasien wanita:")
#for patient in patients:
#    if patient[2] == 'female':
#        print(patient[0])

#Output:
#Daftar nama pasien wanita:
#Aluh
#Ani
#Tulamak

#b. Untuk mencetak data pasien perokok, dapat dilakukan dengan menggunakan perulangan dan percabangan juga. Berikut adalah contoh kode programnya:

#print("Daftar pasien perokok:")
#for patient in patients:
#    if patient[3] == 'smoker':
#        print("Nama:", patient[0])
#        print("Usia:", patient[1])
#        print("Jenis Kelamin:", patient[2])
#        print("Tinggi Badan:", patient[4])
#        print()
#Output:


#Daftar pasien perokok:
#Nama: Anang
#Usia: 48
#Jenis Kelamin: male
#Tinggi Badan: 175

#Nama: Ani
#Usia: 62
#Jenis Kelamin: female
#Tinggi Badan: 150

#Nama: Tulamak
#Usia: 32
#Jenis Kelamin: female
#Tinggi Badan: 165

#c. Untuk mencetak data pasien perokok yang umurnya kurang dari 40, dapat dilakukan dengan menggunakan perulangan dan percabangan juga. 
#Berikut adalah contoh kode programnya:

#print("Daftar pasien perokok dengan umur kurang dari 40 tahun:")
#for patient in patients:
#    if patient[1] < 40 and patient[3] == 'smoker':
#        print("Nama:", patient[0])
#        print("Usia:", patient[1])
#        print("Jenis Kelamin:", patient[2])
#        print("Tinggi Badan:", patient[4])
#        print()

#Output:

#Daftar pasien perokok dengan umur kurang dari 40 tahun:
#Tulamak

#Catatan: Pada output di atas hanya terdapat nama pasien saja karena hanya diminta untuk mencetak nama pasien yang umurnya kurang dari 40. 
#Jika ingin mencetak seluruh data pasien, bisa mengikuti contoh pada bagian b di atas.

#tugas 5
nilai_ulangan = [['Madhan', 85, 90, 65],
                 ['Ari', 75, 82, 63],
                 ['Fuad', 60, 66, 75],
                 ['Aspi', 93, 83, 60],
                 ['Roy', 75, 85, 85]]

#a. Untuk mencetak nilai pemrograman web dari setiap mahasiswa, dapat dilakukan dengan menggunakan perulangan for dan indeks list:
    
for nilai in nilai_ulangan:
    print(f"Nilai ulangan Pemrograman Web {nilai[0]} adalah {nilai[2]}")

#Output:
#Nilai ulangan Pemrograman Web Madhan adalah 65
#Nilai ulangan Pemrograman Web Ari adalah 63
#Nilai ulangan Pemrograman Web Fuad adalah 75
#Nilai ulangan Pemrograman Web Aspi adalah 60
#Nilai ulangan Pemrograman Web Roy adalah 85

#b. Untuk memodifikasi kode program dari soal a, agar nilai mahasiswa yang kurang dari 70 mendapatkan pesan bahwa nilainya kurang dari KKM, dapat menggunakan kondisi if:

for nilai in nilai_ulangan:
    if nilai[2] < 70:
        print(f"Nilai ulangan Pemrograman Web {nilai[0]} adalah {nilai[2]} (Kurang dari KKM)")
    else:
        print(f"Nilai ulangan Pemrograman Web {nilai[0]} adalah {nilai[2]}")

#Output:
#Nilai ulangan Pemrograman Web Madhan adalah 65 (Kurang dari KKM)
#Nilai ulangan Pemrograman Web Ari adalah 63 (Kurang dari KKM)
#Nilai ulangan Pemrograman Web Fuad adalah 75
#Nilai ulangan Pemrograman Web Aspi adalah 60 (Kurang dari KKM)
#Nilai ulangan Pemrograman Web Roy adalah 85

#c. Untuk menampilkan total nilai ulangan struktur data, dapat menggunakan perulangan for dan variabel penampung:

total_struktur_data = 0
for nilai in nilai_ulangan:
    total_struktur_data += nilai[1]

print(f"Total nilai ulangan Struktur Data adalah {total_struktur_data}")

#Output:
#Total nilai ulangan Struktur Data adalah 406

#d. Untuk menampilkan nilai rata-rata ulangan pemrograman web, dapat menggunakan perulangan for dan variabel penampung:

total_pemrograman_web = 0
for nilai in nilai_ulangan:
    total_pemrograman_web += nilai[2]

rata_rata_pemrograman_web = total_pemrograman_web / len(nilai_ulangan)

print(f"Rata-rata nilai ulangan Pemrograman Web adalah {rata_rata_pemrograman_web}")

#Output:
#Rata-rata nilai ulangan Pemrograman Web adalah 71.6


# Data nilai mahasiswa
nilai_mahasiswa = [
    {"nama": "Madhan", "pemrograman dasar": 85, "struktur data": 90, "pemrograman web": 65},
    {"nama": "Ari", "pemrograman dasar": 75, "struktur data": 82, "pemrograman web": 63},
    {"nama": "Fuad", "pemrograman dasar": 60, "struktur data": 66, "pemrograman web": 75},
    {"nama": "Aspi", "pemrograman dasar": 93, "struktur data": 83, "pemrograman web": 60},
    {"nama": "Roy", "pemrograman dasar": 75, "struktur data": 85, "pemrograman web": 85}
]

# e. Nilai tertinggi pada ulangan pemrograman dasar beserta nama mahasiswanya

nilai_tertinggi_pd = 0
mahasiswa_pd = ""
for mahasiswa in nilai_mahasiswa:
    if mahasiswa["pemrograman dasar"] > nilai_tertinggi_pd:
        nilai_tertinggi_pd = mahasiswa["pemrograman dasar"]
        mahasiswa_pd = mahasiswa["nama"]
print("Nilai tertinggi pada ulangan pemrograman dasar adalah", nilai_tertinggi_pd, "diperoleh oleh", mahasiswa_pd)

# f. Nilai terendah pada ulangan struktur data beserta nama mahasiswanya
nilai_terendah_sd = nilai_mahasiswa[0]["struktur data"]
mahasiswa_sd = nilai_mahasiswa[0]["nama"]
for mahasiswa in nilai_mahasiswa:
    if mahasiswa["struktur data"] < nilai_terendah_sd:
        nilai_terendah_sd = mahasiswa["struktur data"]
        mahasiswa_sd = mahasiswa["nama"]
print("Nilai terendah pada ulangan struktur data adalah", nilai_terendah_sd, "diperoleh oleh", mahasiswa_sd)

# g. Mengubah nilai ulangan tertentu sesuai pilihan user
# Meminta input nama mahasiswa
nama_mahasiswa = input("Masukkan nama mahasiswa: ")

# Meminta input mata kuliah
mata_kuliah = input("Masukkan mata kuliah (pemrograman dasar/struktur data/pemrograman web): ")

# Meminta input nilai baru
nilai_baru = int(input("Masukkan nilai baru: "))

# Mencari mahasiswa dengan nama yang sesuai
mahasiswa_index = -1
for i in range(len(nilai_mahasiswa)):
    if nilai_mahasiswa[i]["nama"] == nama_mahasiswa:
        mahasiswa_index = i
        break

# Jika mahasiswa tidak ditemukan, keluarkan pesan kesalahan
if mahasiswa_index == -1:
    print("Mahasiswa tidak ditemukan!")
else:
    # Jika mata kuliah tidak valid, keluarkan pesan kesalahan
    if mata_kuliah not in ["pemrograman dasar", "struktur data", "pemrograman web"]:
        print("Mata kuliah tidak valid!")
    else:
        # Mengubah nilai sesuai pilihan user
        nilai_mahasiswa[mahasiswa_index][mata_kuliah] = nilai_baru
        print("Nilai " + mata_kuliah + " untuk mahasiswa " + nama_mahasiswa + " telah diubah menjadi " + str(nilai_baru))
        print("Data nilai mahasiswa setelah diubah:")
        for mahasiswa in nilai_mahasiswa:
                print("Nama:", mahasiswa["nama"])
                print("Nilai pemrograman dasar:", mahasiswa["pemrograman dasar"])
                print("Nilai struktur data:", mahasiswa["struktur data"])
                print("Nilai pemrograman web:", mahasiswa["pemrograman web"])
                print("=======================")

#Tugas 6
#a. Untuk mencetak matriksA dan matriksB seperti pada contoh, dapat dilakukan dengan menggunakan perulangan for. Berikut adalah kode programnya:
#mencetak matriksA
matriksA = [
    [2,3,4],
    [3,4,5],
    [4,5,6]
]

matriksB = [
    [4,3,5],
    [7,4,6],
    [4,2,3]
]

print("Matriks A:")
for i in range(len(matriksA)):
    for j in range(len(matriksA[i])):
        print(matriksA[i][j], end="\t")
    print()

# mencetak matriksB
print("\nMatriks B:")
for i in range(len(matriksB)):
    for j in range(len(matriksB[i])):
        print(matriksB[i][j], end="\t")
    print()

#Output:
#Matriks A:
#2       3       4       
#3       4       5       
#4       5       6       

#Matriks B:
#4       3       5       
#7       4       6       
#4       2       3

#b. Untuk melakukan perkalian matriks, dapat menggunakan nested loop for untuk mengalikan setiap elemen pada baris matriksA dengan setiap elemen pada kolom matriksB.
# Berikut adalah kode programnya:
# inisialisasi matriks hasil kali
matriksC = [[0 for j in range(len(matriksB[0]))] for i in range(len(matriksA))]

# mengalikan matriksA dengan matriksB
for i in range(len(matriksA)):
    for j in range(len(matriksB[0])):
        for k in range(len(matriksB)):
            matriksC[i][j] += matriksA[i][k] * matriksB[k][j]

# mencetak matriks hasil kali
print("\nMatriks C (Hasil Kali Matriks A dan Matriks B):")
for i in range(len(matriksC)):
    for j in range(len(matriksC[i])):
        print(matriksC[i][j], end="\t")
    print()

#Output:
#Matriks C (Hasil Kali Matriks A dan Matriks B):
#8       9       20      
#21      16      30      
#16      10      18