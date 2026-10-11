class Koleksi:
    def __init__(self, kode, nama):
        self.kode = kode
        self.__nama = nama

    def get_nama(self):
        return self.__nama


class Inventory:
    def __init__(self):
        self.Sepatu = [
            Koleksi("S01", "Salomon"),
            Koleksi("S02", "Adidas"),
            Koleksi("S03", "Nike")
        ]
        self.Tanaman = [
            Koleksi("T01", "Mawar"),
            Koleksi("T02", "Melati")
        ]
        self.Kendaraan = [
            Koleksi("K01", "Ferrari LaFerrari"),
            Koleksi("K02", "Lamborghini Aventador")
        ]
        self.Action_figure = [
            Koleksi("A01", "Gundam"),
            Koleksi("A02", "Iron Man"),
            Koleksi("A03", "Batman")
        ]


class TampilkanKoleksi:
    def __init__(self, inventory):
        self.inventory = inventory

    def tampilkan(self):
        print("\nPilih Koleksi untuk Ditampilkan:")
        print("1. Koleksi Sepatu")
        print("2. Koleksi Tanaman")
        print("3. Koleksi Kendaraan")
        print("4. Koleksi Action Figure")
        pilihan = int(input("Masukkan pilihan: "))

        collections = [
            self.inventory.Sepatu,
            self.inventory.Tanaman,
            self.inventory.Kendaraan,
            self.inventory.Action_figure
        ]

        if 1 <= pilihan <= 4:
            selected_collection = collections[pilihan - 1]
            if not selected_collection:
                print("Koleksi kosong.")
            else:
                for item in selected_collection:
                    print(f"Kode: {item.kode}, Nama: {item.get_nama()}")
        else:
            print("Pilihan tidak valid.")


class TambahKoleksi:
    def __init__(self, inventory):
        self.inventory = inventory

    def tambah(self):
        print("\nPilih Koleksi untuk Ditambahkan:")
        print("1. Koleksi Sepatu")
        print("2. Koleksi Tanaman")
        print("3. Koleksi Kendaraan")
        print("4. Koleksi Action Figure")
        pilihan = int(input("Masukkan pilihan: "))

        collections = [
            self.inventory.Sepatu,
            self.inventory.Tanaman,
            self.inventory.Kendaraan,
            self.inventory.Action_figure
        ]

        if 1 <= pilihan <= 4:
            kode = input("Masukkan kode barang: ")
            nama = input("Masukkan nama barang: ")
            collections[pilihan - 1].append(Koleksi(kode, nama))
            print("Barang berhasil ditambahkan.")
        else:
            print("Pilihan tidak valid.")


class HapusKoleksi:
    def __init__(self, inventory):
        self.inventory = inventory

    def hapus(self):
        print("\nPilih Koleksi untuk Dihapus:")
        print("1. Koleksi Sepatu")
        print("2. Koleksi Tanaman")
        print("3. Koleksi Kendaraan")
        print("4. Koleksi Action Figure")
        pilihan = int(input("Masukkan pilihan: "))

        collections = [
            self.inventory.Sepatu,
            self.inventory.Tanaman,
            self.inventory.Kendaraan,
            self.inventory.Action_figure
        ]

        if 1 <= pilihan <= 4:
            kode = input("Masukkan kode barang yang ingin dihapus: ")
            selected_collection = collections[pilihan - 1]

            for item in selected_collection:
                if item.kode == kode:
                    selected_collection.remove(item)
                    print("Barang berhasil dihapus.")
                    return

            print("Barang dengan kode tersebut tidak ditemukan.")
        else:
            print("Pilihan tidak valid.")
