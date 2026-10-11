import sys
from PyQt5.QtWidgets import QApplication
from koleksi import Inventory, TampilkanKoleksi, TambahKoleksi, HapusKoleksi
from gui import MainWindow

if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("\nMenu Utama:")
        print("1. Tampilkan Koleksi (Terminal)")
        print("2. Tambah Koleksi")
        print("3. Hapus Koleksi")
        print("4. Tampilkan GUI")
        print("5. Keluar")
        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            tampilkan = TampilkanKoleksi(inventory)
            tampilkan.tampilkan()
        elif pilihan == 2:
            tambah = TambahKoleksi(inventory)
            tambah.tambah()
        elif pilihan == 3:
            hapus = HapusKoleksi(inventory)
            hapus.hapus()
        elif pilihan == 4:
            app = QApplication(sys.argv)
            window = MainWindow(inventory)
            window.show()
            sys.exit(app.exec_())
        elif pilihan == 5:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
