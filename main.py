import json

FILE = "data toko.json"

def lihat_data():
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("--- DAFTAR BARANG ---")
    for i, barang in enumerate(data, 1):
        print(i, barang["nama"], "-", barang["kategori"],
            "- stok:", barang["stok"],
            "- Rp", barang["harga"])

    return data

def tambah_data(nama, kategori, stok, harga):
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append({"nama": nama, "kategori": kategori, "stok": stok, "harga": harga})

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return "Barang ditambah dan tersimpan!"

while True:
    print("===== TOKO KELONTONG =====")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Keluar")
    pilih = input("Pilih (1-3): ")

    if pilih == "1":
        lihat_data()

    elif pilih == "2":
        nama = input("Nama Barang : ")
        kategori = input("Kategori    : ")
        stok = int(input("Stok        : "))
        harga = int(input("Harga       : "))
        print(tambah_data(nama, kategori, stok, harga))

    elif pilih == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan salah, coba lagi.")