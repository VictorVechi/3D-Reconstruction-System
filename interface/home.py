import os
import shutil
import sys
import this
from unittest.main import MAIN_EXAMPLES
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog, QMainWindow

from janelaPcd import JanelaPCD
app = QApplication(sys.argv)
class MainWindow(QWidget):  
    
    window = JanelaPCD()
    def __init__(self):
        super().__init__()

        self.resize(600,500)
        self.setFixedSize(600,500)
        self.setWindowTitle("Backyardigans")

        btn = QPushButton("Criar pasta",self)
        btn.setGeometry(200,200,200,35)
        btn.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        #btn.clicked.connect(janelaNova)

        btn2 = QPushButton("Seleção de PCD",self)
        btn2.setGeometry(200,300,200,35)
        btn2.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        btn2.clicked.connect(self.btn1)

    def btn1(self):
        main.close()
        self.window.show()
        
main = MainWindow()
        