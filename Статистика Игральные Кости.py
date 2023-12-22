import sys
import random
from PyQt6 import QtWidgets
def countAtt():
    a = int(input_text.text())
    arr_results = []
    for x in range(a):
        arr_results.append(random.randint(1, 6))
    a1 = str(round(arr_results.count(1) / a * 100, 2))
    a2 = str(round(arr_results.count(2) / a * 100, 2))
    a3 = str(round(arr_results.count(3) / a * 100, 2))
    a4 = str(round(arr_results.count(4) / a * 100, 2))
    a5 = str(round(arr_results.count(5) / a * 100, 2))
    a6 = str(round(arr_results.count(6) / a * 100, 2))
    result.setText("<b>1:</b> "+a1+"<br><b>2:</b> "+a2+"<br><b>3:</b> "+a3+"<br><b>4:</b> "+a4+"<br><b>5:</b> "+a5+"<br><b>6:</b> "+a6)
    label.hide()
    input_text.hide()
    btnSend.hide()
    btnQuit.show()
    input_text.setText("")
    result.show()
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Статистика")
window.resize(300, 70)
label = QtWidgets.QLabel("сколько бросков надо выполнить")
input_text = QtWidgets.QLineEdit()
btnSend = QtWidgets.QPushButton("вычислить")
btnQuit = QtWidgets.QPushButton("закрыть")
result = QtWidgets.QLabel("")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(input_text)
vbox.addWidget(btnSend)
vbox.addWidget(result)
vbox.addWidget(btnQuit)
result.hide()
btnQuit.hide()
window.setLayout(vbox)
btnSend.clicked.connect(countAtt)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec())