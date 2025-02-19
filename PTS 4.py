def cek_ganjil_genap(n):
    return "Ganjil" if n % 2 != 0 else "Genap"

print(cek_ganjil_genap(7))
print(cek_ganjil_genap(10))


#Line 1 = Fungsi menentukan apakah n ganjil atau genap
#Line 2 = Menggunakan ternary operator untuk mengembalikan "Ganjil" jika n tidak habis dibagi 2, sebaliknya mengembalikan "Genap"
#Line 4 = Memanggil fungsi dengan angka 7
#Line 5 = Memanggil fungsi dengan angka 10