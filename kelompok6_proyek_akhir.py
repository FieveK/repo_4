import os
from materi import menu_materi
from latihan import menu_latihan
from ujian import menu_ujian
ulang = 'YA'
while ulang=='YA':
    pilih = input('>>MENU UTAMA<<'
    '\nA.Uraian materi'
    '\nB.Latihan'
    '\nC.Evaluasi/Ujian'
    '\nD.Profil Kelompok'
    '\nSilahkan di pilih Terlebih dahulu = ').upper()
    if pilih == "A" :
        os.system("cls")
        menu_materi()
    elif pilih == 'B':
        os.system("cls")
        menu_latihan()
    elif pilih == 'C':
        os.system("cls")
        menu_ujian()       
    elif pilih == 'D':
        os.system('cls')
        print ('=== Project kelompok 6 ===')
        print('\nAbdul Hayyi (2210131210015)\nMuhammad Salman Anshari Rizky (2210131210027)\nSabrina (2210131120003)')
    else :
        os.system ('cls')
        print ("Anda salah memasukkan pilihan")
    ulang = input("\nApakah anda ingin memilih menu yang lain ?\n[YA/Tidak] = ").upper()
    os.system("pause")
    os.system("cls")
print("program selesai terima kasih telah menggunakan program ini")
os.system("pause")
os.system("cls")




  
