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
        btn.clicked.connect(self.diretorio)

    def diretorio(self):
        self.file = QFileDialog.getExistingDirectory(str("arquivo pcd"), '/home')
        self.txt_path.setText(self.file)
        self.file = str(self.file)
