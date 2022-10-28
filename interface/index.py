import os
import shutil
import sys
from unittest.main import MAIN_EXAMPLES
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog, QMainWindow
from janelaPcd import JanelaPCD
from home import MainWindow
#declaração objetos globais para manipulação
app = QApplication(sys.argv)
main = MainWindow()

#main.exibir()

main.show()
app.exec()


