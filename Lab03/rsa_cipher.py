import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnEncrypt.clicked.connect(self.encrypt)
        self.ui.btnDecrypt.clicked.connect(self.decrypt)
        self.ui.btnGenKeys.clicked.connect(self.gen_keys)
        self.ui.btnSign.clicked.connect(self.sign)
        self.ui.btnVerrify.clicked.connect(self.verify)
        self.show()
        
    def encrypt(self):
        url = "http://127.0.0.1:5000/rsa/encrypt"
        plain = self.ui.txtPlain.toPlainText()
        params = {"message": plain, "key_type": "public"}
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
        url = "http://127.0.0.1:5000/rsa/decrypt"
        cipher = self.ui.txtCipher.toPlainText()
        params = {"ciphertext": cipher, "key_type": "private"}
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
            msg.exec()
            
    def gen_keys(self):
        url = "http://127.0.0.1:5000/rsa/generate_keys"
        try:
            response = requests.get(url)
            if (response.status_code == 200):
                response = response.json()
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText(response["message"])
                msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured: " + str(e))
            msg.exec()
            
    def sign(self):
        url = "http://127.0.0.1:5000/rsa/sign"
        params = {"message": self.ui.txtInfo.toPlainText()}
        try:
            response = requests.post(url, json=params)
            if (response.status_code == 200):
                response = response.json()
                self.ui.txtSignature.setPlainText(response["signature"])
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("Signature successful")
                msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured: " + str(e))
            msg.exec()
    
    def verify(self):
        url = "http://127.0.0.1:5000/rsa/verify"
        params = {
            "message" : self.ui.txtInfo.toPlainText(),
            "signature": self.ui.txtSignature.toPlainText() 
        }
        try:
            response = requests.post(url, json = params)
            if (response.status_code == 200):
                data = response.json()
                if (data["verified"] == True):
                    msg = QMessageBox()
                    msg.setWindowTitle("Success")
                    msg.setText("Signature verified")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Signature not verified")
                    msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured: " + str(e))
            msg.exec()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
                