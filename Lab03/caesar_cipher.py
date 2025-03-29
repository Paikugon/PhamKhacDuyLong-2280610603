import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI.caesar import Ui_MainWindow
import requests


class MyApp(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnEncrypt.clicked.connect(self.encrypt)
        self.ui.btnDecrypt.clicked.connect(self.decrypt)
        self.show()
        
    def encrypt(self):
        url = "http://127.0.0.1:5000/caesar/encrypt"
        plain = self.ui.txtPlain.toPlainText()
        key = self.ui.txtKey.toPlainText()
        params = {"plaintext": plain, "key": int(key)}
        try:
            response = requests.post(url, json=params)
            response = response.json()
            self.ui.txtCipher.setPlainText(response["ciphertext"])
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Encryption successful")
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured: " + str(e) + "\n")
            msg.exec_()
        
    def decrypt(self):
        url = "http://127.0.0.1:5000/caesar/decrypt"
        cipher = self.ui.txtCipher.toPlainText()
        key = self.ui.txtKey.toPlainText()
        params = {"ciphertext": cipher, "key": int(key)}
        try:
            response = requests.post(url, json=params)
            response = response.json()
            self.ui.txtPlain.setPlainText(response["plaintext"])
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Decryption successful")
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured: " + str(e))
            msg.exec_()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    