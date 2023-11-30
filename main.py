import random
import sys

from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.zamow.clicked.connect(self.zamowienie)
        self.show()




    def zamowienie(self):
        adres = self.ui.adres.text()
        email = self.ui.email.text()
        czas = random.randint(10, 100)
        cena = 0
        cena_ser = 0
        if self.ui.hawajska.isChecked():
            cena = 30
            pizza = "hawajska"
        if self.ui.margharitta.isChecked():
            cena = 28
            pizza = "margharitta"
        if self.ui.Quatro_formaggie.isChecked():
            cena = 34
            pizza = "quatro formaggie"
        if self.ui.Capricciosa.isChecked():
            cena = 32
            pizza = "capricciosa"
        if self.ui.ser.isChecked():
             cena_ser = 5

        self.ui.result.setText(f"kupiłeś {pizza} do zapłlaty {cena + cena_ser}zł dostawa będzie za {cena} minut na adres {adres} wiadomość z potwierdzenie płatności została wysłana na {email}")







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())

