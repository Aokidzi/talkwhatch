import   design.Superwhatch as drammashine
import sys
from  PyQt5 import QtWidgets
import threading
import datetime
import random
import pyttsx3;
class ExamoleAPP(QtWidgets.QMainWindow, drammashine.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sound7)
        self.pushButton_2.clicked.connect(self.sound1)
        self.x= ''
        self.engine = pyttsx3.init();
        self.joke=['Зачем нам искусственный интеллект? Он у нас и так выглядит неестественным', 'Думаешь, что слова ничего не стоят? Значит, ты никогда не общался с адвокатами...', 'Любой каприз за ваши деньги. Вы платите - я капризничаю', ]
        threading.Thread(target=self.time).start()

    def sayjoke(self):
        self.engine.say(self.joke[random.randint(0,2)])
        self.engine.runAndWait();

    def sound7(self):
        threading.Thread(target=self.say).start()

    def say(self):
        self.engine.say(self.x);
        self.engine.runAndWait();

    def time(self):
        while True:
            self.x = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
            self.lcdNumber.display(self.x)




    def sound1(self):
        threading.Thread(target=self.sayjoke).start()

app = QtWidgets.QApplication(sys.argv)
window = ExamoleAPP()
window.show()
app.exec()