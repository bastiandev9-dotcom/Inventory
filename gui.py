import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QTextEdit, QVBoxLayout, QWidget
)
from koleksi import Inventory


class MainWindow(QMainWindow):
    def __init__(self, inventory):
        super().__init__()
        self.inventory = inventory
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Koleksi Barang")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Pilih Koleksi untuk Ditampilkan:")
        layout.addWidget(self.label)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Koleksi Sepatu")
        self.combo_box.addItem("Koleksi Tanaman")
        self.combo_box.addItem("Koleksi Kendaraan")
        self.combo_box.addItem("Koleksi Action Figure")
        layout.addWidget(self.combo_box)

        # Tombol Tampilkan
        self.show_button = QPushButton("Tampilkan")
        self.show_button.clicked.connect(self.show_collection)
        layout.addWidget(self.show_button)


        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

 
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_collection(self):

        pilih = self.combo_box.currentIndex()
        collections = [
            self.inventory.Sepatu,
            self.inventory.Tanaman,
            self.inventory.Kendaraan,
            self.inventory.Action_figure
        ]
        selected_collection = collections[pilih]

        # Menampilkan koleksi yang dipilih
        self.output.clear()
        if not selected_collection:
            self.output.append("Koleksi kosong.")
        else:
            for item in selected_collection:
                self.output.append(f"Kode: {item.kode}, Nama: {item.get_nama()}")
