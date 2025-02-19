import random

def sapa_acak():
    sapaan = ["assalamualaikum", "kelas", "selamat pagi"]
    nama = ["teman-teman", "kawan", "rekan-rekan", "sehat"]

    pilihan_sapaan = random.choice(sapaan)
    pilihan_nama = random.choice(nama)

    pesan = f"{pilihan_sapaan}, {pilihan_nama}! semangat belajar python!"
    return pesan

print(sapa_acak())

#Line 1 = Mengimpor modul random untuk memilih elemen
#Line 3 = Membuat fungsi
#Line 4 = List yang berisi beberapa sapaan
#Line 5 = List yang berisi beberapa nama
#Line 7 = Memilih satu sapaan secara acak
#Line 8 = Memilih satu nama secara acak
#Line 10 = Membuat pesan sapaan dengan format string (f-string)
#Line 11 = Fungsi mengembalikan pesan yang dibuat
#Line 13 = Memanggil fungsi dan mencetak hasilnya