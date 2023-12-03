from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
win = QWidget()
win.resize(400, 200)
win.setWindowTitle("Генератор переможця")

winner = QLabel("Номер переможця")
result = QLabel("?")

gen_btn = QPushButton("Згенерувати")

line = QVBoxLayout()
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(result, alignment=Qt.AlignCenter)
line.addWidget(gen_btn, alignment=Qt.AlignCenter)

win.setLayout(line)

# в кінці
win.show() # показуємо вікно
app.exec_() # запускаємо програму

