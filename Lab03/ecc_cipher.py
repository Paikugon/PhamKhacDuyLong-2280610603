import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI.ecc import Ui_MainWindow
import requests


class MyApp(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSign.clicked.connect(self.sign)
        self.ui.btnVerify.clicked.connect(self.verify)
        self.show()
        
    def sign(self):
        url = "http://127.0.0.1:5000/ecc/sign"
        try:
            message = self.ui.plainTextEdit.toPlainText()
            params = {"message": message}
            response = requests.post(url, json=params)
            response = response.json()
            self.ui.plainTextEdit_2.setPlainText(response["signature"])
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Signing successful")
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("An error occured: " + str(e) + "\n")
            msg.exec_()
        
    def verify(self):
        url = "http://127.0.0.1:5000/ecc/verify"
        try:
            message = self.ui.plainTextEdit.toPlainText()
            signature = self.ui.plainTextEdit_2.toPlainText()
            params = {"message": message, "signature": signature}
            response = requests.post(url, json=params)
            response = response.json()
            isVerified = response["verified"]
            msg = QMessageBox()
            msg.setWindowTitle("Verification")
            if isVerified:
                msg.setText("Signature is valid")
            else:
                msg.setText("Signature is invalid")
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
    