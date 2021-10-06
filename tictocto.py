from functools import partial
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class TicTocTOE(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("tic.ui" , None)
        self.ui.show()

        self.game = [[self.ui.btn_1,self.ui.btn_2,self.ui.btn_3],
                    [self.ui.btn_4,self.ui.btn_5,self.ui.btn_6],
                    [self.ui.btn_7,self.ui.btn_8,self.ui.btn_9]]

        self.game[0][0] = self.ui.btn_1
        self.game[0][1] = self.ui.btn_2
        self.game[0][2] = self.ui.btn_3
        self.game[1][0] = self.ui.btn_4
        self.game[1][1] = self.ui.btn_5
        self.game[1][2] = self.ui.btn_6
        self.game[2][0] = self.ui.btn_7
        self.game[2][1] = self.ui.btn_8
        self.game[2][2] = self.ui.btn_9
        
        #self.x_score.clicked.connect(self.Board)
        # self.menu.addAction(self.menuFile.menuAction())

        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet("color:black; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.3125 rgba(128, 71, 174, 255), stop:0.886364 rgba(255, 255, 255, 255));")
                self.game[i][j].clicked.connect(partial( self.play,i ,j))
    
        self.player = "x"

    def play(self, i, j):
        if self.game[i][j].text() == "":
            if self.player == "x":
                self.game[i][j].setText("x")
                self.game[i][j].setStyleSheet("color:green; background-color: black                      qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(27, 80, 251, 255), stop:1 rgba(255, 255, 255, 255));")
                self.player = "o"
                
            else:
                self.game[i][j].setText("o")
                self.game[i][j].setStyleSheet("color:red; background-color:  blue                        qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(128, 76, 116, 255), stop:1 rgba(255, 45, 89, 255));")
                self.player = "x"

        self.check()        

    def check(self):
        if (self.game[0][0].text()== "x" and  self.game[0][1].text()== "x" and  self.game[0][2].text()== "x")  or \
           (self.game[1][0].text()== "x" and  self.game[1][1].text()== "x" and  self.game[1][2].text()== "x") or \
           (self.game[2][0].text()== "x" and  self.game[2][1].text()== "x" and  self.game[2][2].text()== "x") :    
           msgBox = QMessageBox()
           msgBox.setText("player 1 wins")
           msgBox.exec()
    
        if (self.game[0][0].text()== "o" and  self.game[0][1].text()== "o" and  self.game[0][2].text()== "o")  or \
           (self.game[1][0].text()== "o" and  self.game[1][1].text()== "o" and  self.game[1][2].text()== "o") or \
           (self.game[2][0].text()== "o" and  self.game[2][1].text()== "o" and  self.game[2][2].text()== "o") :    
           msgBox = QMessageBox()
           msgBox.setText("player 2 wins")
           msgBox.exec()    
    def Board(self):
        self.x_score = 0
        self.playerO = 0

app = QApplication([])
window = TicTocTOE()

app.exec()