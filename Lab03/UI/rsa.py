# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 350, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnGenKeys = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenKeys.setGeometry(QtCore.QRect(50, 20, 150, 40))
        self.btnGenKeys.setObjectName("btnGenKeys")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtPlain = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPlain.setGeometry(QtCore.QRect(50, 140, 500, 100))
        self.txtPlain.setObjectName("txtPlain")
        self.txtCipher = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCipher.setGeometry(QtCore.QRect(50, 300, 500, 100))
        self.txtCipher.setObjectName("txtCipher")
        self.txtInfo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtInfo.setGeometry(QtCore.QRect(650, 140, 500, 100))
        self.txtInfo.setObjectName("txtInfo")
        self.txtSignature = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSignature.setGeometry(QtCore.QRect(650, 300, 500, 100))
        self.txtSignature.setObjectName("txtSignature")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 100, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 260, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(150, 450, 120, 50))
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(350, 450, 120, 50))
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.btnSign = QtWidgets.QPushButton(self.centralwidget)
        self.btnSign.setGeometry(QtCore.QRect(750, 450, 120, 50))
        self.btnSign.setObjectName("btnSign")
        self.btnVerrify = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerrify.setGeometry(QtCore.QRect(950, 450, 120, 50))
        self.btnVerrify.setObjectName("btnVerrify")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text"))
        self.btnGenKeys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btnSign.setText(_translate("MainWindow", "Sign"))
        self.btnVerrify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
