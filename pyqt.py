import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout

app = QApplication(sys.argv)

window_grid = QWidget()
window_grid.setWindowTitle("QGridLayout")
window_grid.resize(300, 100)

grid_layout = QGridLayout()
grid_layout.addWidget(QPushButton("Button x"), 0, 0)
grid_layout.addWidget(QPushButton("Button y"), 0, 1)
grid_layout.addWidget(QPushButton("Button z"), 1, 0)
grid_layout.addWidget(QPushButton("Button q"), 1, 1) 

window_grid.setLayout(grid_layout)

window_hbox = QWidget()
window_hbox.setWindowTitle(" QHBoxLayout")
window_hbox.resize(400, 100)

hbox_layout = QHBoxLayout()
hbox_layout.addWidget(QPushButton("چپ"))
hbox_layout.addWidget(QPushButton("وسط"))
hbox_layout.addWidget(QPushButton("راست"))

window_hbox.setLayout(hbox_layout)

window_vbox = QWidget()
window_vbox.setWindowTitle("QVBoxLayout")
window_vbox.resize(200, 200)

vbox_layout = QVBoxLayout()
vbox_layout.addWidget(QPushButton("بالا"))
vbox_layout.addWidget(QPushButton("وسط"))
vbox_layout.addWidget(QPushButton("پایین"))

window_vbox.setLayout(vbox_layout)

window_grid.show()
window_hbox.show()
window_vbox.show()

sys.exit(app.exec())
