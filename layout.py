# Form implementation generated from reading ui file '.\layout.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(898, 476)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 851, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.hawajska = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.hawajska.setObjectName("hawajska")
        self.verticalLayout.addWidget(self.hawajska)
        self.margharitta = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.margharitta.setObjectName("margharitta")
        self.verticalLayout.addWidget(self.margharitta)
        self.Quatro_formaggie = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.Quatro_formaggie.setObjectName("Quatro_formaggie")
        self.verticalLayout.addWidget(self.Quatro_formaggie)
        self.Capricciosa = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.Capricciosa.setObjectName("Capricciosa")
        self.verticalLayout.addWidget(self.Capricciosa)
        self.gridLayout.addLayout(self.verticalLayout, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.adres = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.adres.setMaximumSize(QtCore.QSize(156, 16777215))
        self.adres.setObjectName("adres")
        self.gridLayout.addWidget(self.adres, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.ser = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.ser.setObjectName("ser")
        self.gridLayout.addWidget(self.ser, 3, 2, 1, 1)
        self.zamow = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.zamow.setObjectName("zamow")
        self.gridLayout.addWidget(self.zamow, 4, 1, 1, 2)
        self.email = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.email.setMaximumSize(QtCore.QSize(156, 16777215))
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 0, 2, 1, 1)
        self.result = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 5, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.hawajska.setText(_translate("Dialog", "Hawajska"))
        self.margharitta.setText(_translate("Dialog", "Margheritta"))
        self.Quatro_formaggie.setText(_translate("Dialog", "Quatro_formaggie"))
        self.Capricciosa.setText(_translate("Dialog", "Capricciosa"))
        self.label_4.setText(_translate("Dialog", "Dodatkowe składniki"))
        self.label_2.setText(_translate("Dialog", "Adres"))
        self.label.setText(_translate("Dialog", "Email"))
        self.label_3.setText(_translate("Dialog", "Rodzaj pizzy"))
        self.ser.setText(_translate("Dialog", "Dodatkowy ser"))
        self.zamow.setText(_translate("Dialog", "zamow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
