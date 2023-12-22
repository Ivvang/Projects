import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class PeriodicTableApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Таблица Менделеева')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.load_periodic_table()
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)

    def load_periodic_table(self):
        try:
            with open('periodictable.csv', 'r') as file:
                data = file.readlines()
                self.tableWidget.setRowCount(len(data))
                self.tableWidget.setColumnCount(20)

                for i, row in enumerate(data):
                    cell_data = row.strip().split(',')
                    for j, cell in enumerate(cell_data):
                        item = QTableWidgetItem(cell)
                        self.tableWidget.setItem(i, j, item)
        except FileNotFoundError:
            print('Файл periodictable.csv не найден')

if __name__ == '__main__':
    a = QApplication(sys.argv)
    window = PeriodicTableApp()
    window.show()
    sys.exit(a.exec())