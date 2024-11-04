def hitung_luas_lingkaran (jari_jari):
    luas = (jari_jari ** 2)
    return luas 

# meminta input dari pengguna
jari_jari = float (input("masukkan jari_jari lingkaran: "))
luas = hitung_luas_lingkaran (jari_jari)

print(f"luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")