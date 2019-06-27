4# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desain_GUI_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 414)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 110, 371, 61))
        self.label.setObjectName("label")
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(72, 160, 421, 22))
        self.namaEdit.setObjectName("namaEdit")
        self.halo = QtWidgets.QPushButton(Form)
        self.halo.setGeometry(QtCore.QRect(180, 200, 93, 28))
        self.halo.setObjectName("halo")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(290, 200, 93, 28))
        self.clear.setObjectName("clear")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(230, 360, 93, 28))
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        self.clear.clicked.connect(self.namaEdit.clear)
        self.exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Masukkan Nama Anda :</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.halo.setText(_translate("Form", "Halo"))
        self.clear.setText(_translate("Form", "Clear"))
        self.exit.setText(_translate("Form", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
