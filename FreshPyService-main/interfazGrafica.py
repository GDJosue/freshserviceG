import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
import matplotlib.pyplot as plt
import datetime
from FreshPy import *


class ReportGenerator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Generador de Reportes')
        self.setGeometry(100, 100, 400, 300)

        # create label
        self.label = QLabel('Seleccione una subcategoría:', self)
        self.label.move(20, 20)

        # create combobox
        self.combobox = QComboBox(self)
        self.combobox.move(20, 50)
        self.combobox.resize(200, 30)

        # add options to combobox
        sub_category = ['Computadora', 'Impresoras', 'Celular', 'Telefono', 'Perifericos', 'Red', 'MS Office',
                        'Adobe Reader', 'Correo Electronico','Alpha ERP','Windows','Chrome','Ring Central','Biometrico',
                        'Otro Sotware','Acceso a internet','Red lenta','Tarjeta de red','Grabaciones','Monitoreo']
        self.combobox.addItems(sub_category)

        # create button
        self.button = QPushButton('Generar Reporte', self)
        self.button.move(20, 100)
        self.button.clicked.connect(self.generate_report)

    def generate_report(self):
        # get selected subcategory from combobox
        sub_category = self.combobox.currentText()

        # import class
        api_key = 'rSkqfcvIaeSD1uVLVunk'
        FreshService_domain = 'https://camen-q.freshservice.com/'
        FS = FreshPy(api_key, FreshService_domain)

        # get all tickets
        tickets = FS.all_tickets()

        # count tickets by subcategory
        count = {}
        for ticket in tickets:
            if 'sub_category' in ticket and ticket['sub_category'] == sub_category:
                if ticket['status'] in count:
                    count[ticket['status']] += 1
                else:
                    count[ticket['status']] = 1

        # plot pie chart
        fig, ax = plt.subplots()
        ax.pie(count.values(), labels=count.keys(), autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title(f'Tickets por subcategoría: {sub_category}')

        # show plot
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReportGenerator()
    window.show()
    sys.exit(app.exec_())
