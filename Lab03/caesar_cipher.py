import sys
from PyQt5 import QtApplication, QtMainWindow, QmessageBox
from UI.caesar import Ui_MainWindow
import requests


class MyApp(QtMainWindow) :
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
        key = self.ui.txtKey.text()
        params = {"plaintext": plain, "key": int(key)}
        try:
            response = requests.get(url, params=params)
            response = response.json()
            self.ui.txtCipher.setPlainText(response["ciphertext"])
            msg = QmessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Encryption successful")
            msg.exec_()
        except:
            msg = QmessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured")
            msg.exec_()
        
    def decrypt(self):
        url = "http://127.0.0.1:5000/caesar/decrypt"
        cipher = self.ui.txtCipher.toPlainText()
        key = self.ui.txtKey.text()
        params = {"plaintext": cipher, "key": int(key)}
        try:
            response = requests.get(url, params=params)
            response = response.json()
            self.ui.txtPlain.setPlainText(response["plaintext"])
            msg = QmessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Decryption successful")
            msg.exec_()
        except:
            msg = QmessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured")
            msg.exec_()
        
if __name__ == "__main__":
    app = QtApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    