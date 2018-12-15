import   design.drammashine as drammashine
import sys
from  PyQt5 import QtWidgets
from  playsound import playsound
import threading

class ExamoleAPP(QtWidgets.QMainWindow, drammashine.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sound7)
        self.pushButton_5.clicked.connect(self.sound1)
        self.pushButton_2.clicked.connect(self.sound2)
        self.pushButton_7.clicked.connect(self.sound3)
        self.pushButton_8.clicked.connect(self.sound4)
        self.pushButton_3.clicked.connect(self.sound5)

    def sound7(self):
        threading.Thread(target=self.sound77).start()

    def sound77(self):
        playsound('zvuki-barabanov-bongo-sborka.mp3')

    def sound1(self):
        threading.Thread(target=self.sound11).start()

    def sound11(self):
        playsound('Dj+Street+Style+feat+Vanessa+Mae+Zvuki+prirodypianinoskripkabitpianino.mp3')

    def sound2(self):
        threading.Thread(target=self.sound22).start()

    def sound22(self):
        playsound('Glaze+Fabrika+Radugiigral+na+pianino+i+drugie+instrumen.mp3')

    def sound3(self):
        threading.Thread(target=self.sound33).start()

    def sound33(self):
        playsound('Minus+instrumenty+gitara+skripka+pianino+i+bit.mp3')

    def sound4(self):
        threading.Thread(target=self.sound44).start()

    def sound44(self):
        playsound('Skripkasovremennaya+obrabotka+BiTskripka+pianino+i+elektro+gitara+Mix.mp3')

    def sound5(self):
        threading.Thread(target=self.sound55).start()

    def sound55(self):
        playsound('VAMocart+Blizhe+k+mechte+skripka+i+royal+Vsem+izvestnye+skripka+i+pianino (1).mp3')
app = QtWidgets.QApplication(sys.argv)
window = ExamoleAPP()
window.show()
app.exec()