import os
import shutil
import sys
from unittest.main import MAIN_EXAMPLES
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog, QMainWindow

app = QApplication(sys.argv)

class JanelaPCD(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(600,500)
        self.setFixedSize(600,500)
        self.setWindowTitle("Selecionar Pcd")

        btn = QPushButton("Selecionar arquivo",self)
        btn.setGeometry(200,200,200,35)
        btn.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
       # btn.clicked.connect(self.diretorio)

    #def diretorio(self):
       # self.file = QFileDialog.getExistingDirectory
       # self.txt_path.setText(self.file)
        #self.file = str(self.file)

le = QLineEdit()
class JanelaPasta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,500)
        self.setFixedSize(600,500)
        self.setWindowTitle("Criar Pasta para PCDS")

        btn = QPushButton("Criar pasta",self)
        btn.setGeometry(200,300,200,35)
        btn.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        btn.clicked.connect(self.criarPasta)

        label = QLabel("Insira o nome da pasta:",self)
        label.adjustSize()
        label.setStyleSheet('font-size:15pt arial;')
        label.move(100,200)

        le.setGeometry(310,200,200,30)

    def criarPasta():
        pasta = le.text()
        print(pasta)

class MainWindow(QMainWindow):  
    janelapcd = JanelaPCD()
    janelapasta = JanelaPasta()
    def __init__(self):
        super().__init__()

        self.resize(600,500)
        self.setFixedSize(600,500)
        self.setWindowTitle("Backyardigans")

        btn = QPushButton("Criar pasta",self)
        btn.setGeometry(200,200,200,35)
        btn.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        btn.clicked.connect(self.btn1)

        btn2 = QPushButton("Seleção de PCD",self)
        btn2.setGeometry(200,300,200,35)
        btn2.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        btn2.clicked.connect(self.btn2)

    def btn1(self):
        main.close()
        self.janelapasta.show()

    def btn2(self):
        main.close()
        self.janelapcd.show()

def rodar():
    main.show()
    app.exec()        

main = MainWindow()
rodar()
