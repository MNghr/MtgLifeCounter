import sys

from PyQt5 import QtGui
#from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.width = 240
        self.height = 500
        self.myLife = MyLife()
        self.opponentLife = OpponentsLife()

        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('ライフカウンタ(仮)')
        vbox = QVBoxLayout()
        vbox.addWidget(self.opponentLife)
        vbox.addWidget(self.myLife)
        self.setLayout(vbox)
        self.show()

    def keyPressEvent(self,event):
        self.myLife.keyPressEvent(event)
        self.opponentLife.keyPressEvent(event)

        
class OpponentsLife(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.life = 20
        self.width = 180
        self.height = 160
        self.initUI()
    
    def initUI(self):
        r = QApplication.desktop().screenGeometry()
        self.lbl = QLabel(self)
        self.lbl.setText("あなた")
        self.lbl.move(int((240-self.width)/2), int(self.height/6))

        self.lifeLabel = QLabel(self)
        self.lifeLabel.setText(str(self.life))
        self.lifeLabel.move(int((240-self.width)/2), int(self.height/2))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.lifeLabel.setFont(font)

        font.setPointSize(32)
        self.lbl.setFont(font)
        self.setGeometry(0, 0, self.width, self.height)
        #self.setWindowTitle('QLineEdit')
        #self.show()

    def keyPressEvent(self, event):
        '''キーが押された場合に呼ばれる。
        '''
        print(type(event.key()))
        if event.key() == 65: #キー入力がaのとき 
            self.life -= 1
            self.lifeLabel.setText(str(self.life))
        elif event.key() == 83: #キー入力がsのとき
            self.life += 1
            self.lifeLabel.setText(str(self.life))

class MyLife(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.life = 20
        self.width = 180
        self.height = 160
        self.initUI()
    
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.setText("わたし")
        self.lbl.move(int((240-self.width)/2), int(self.height/6))

        self.lifeLabel = QLabel(self)
        self.lifeLabel.setText(str(self.life))
        self.lifeLabel.move(int((240-self.width)/2), int(self.height/2))
        font = QtGui.QFont()
        font.setPointSize(96)
        self.lifeLabel.setFont(font)

        font1 = QtGui.QFont()
        font1.setPointSize(32)
        self.lbl.setFont(font1)
        self.setGeometry(0, 0, self.width, self.height)
        #self.setWindowTitle('QLineEdit')
        #self.show()

    def keyPressEvent(self, event):
        '''キーが押された場合に呼ばれる。
        '''
        print(type(event.key()))
        if event.key() == 75: #キー入力がkのとき 
            self.life -= 1
            self.lifeLabel.setText(str(self.life))
        elif event.key() == 76: #キー入力がlのとき
            self.life += 1
            self.lifeLabel.setText(str(self.life))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #window = QWidget()
    #layout = QVBoxLayout()
    #opponentLife = OpponentsLife()
    #myLife = MyLife()
    #layout.addWidget(opponentLife)
    #layout.addWidget(myLife)
    #window.setLayout(layout)
    #window.show()
    window = MainWidget()
    
    sys.exit(app.exec_())