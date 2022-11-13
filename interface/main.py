import os
import shutil
import sys
import easygui
from unittest.main import MAIN_EXAMPLES
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QMainWindow, QInputDialog
import utils.reconstrucao as reconstruir
app = QApplication(sys.argv)


class JanelaPasta(QWidget):
    def __init__(self):
        super().__init__()
        self.le = QLineEdit(self)

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

        self.le.setGeometry(250,195,250,30)
    def criarPasta(self):
        try:
            os.mkdir('dataset/'+self.le.text())
            main.show()
            self.close()
            main.selecionarArquivos()
            main.criar3d()
        except:
            print("Deu erro")



class MainWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.dialog = QMessageBox(self) 
        self.input = QInputDialog(self)
        self.resize(600,500)
        self.setFixedSize(600,500)
        self.setWindowTitle("Main")

        btn = QPushButton("Criar pasta",self)
        btn.setGeometry(200,150,200,35)
        btn.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        btn.clicked.connect(self.janelaCriarPasta)

        btn2 = QPushButton("Selecionar arquivos",self)
        btn2.setGeometry(200,225,200,35) 
        btn2.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        btn2.clicked.connect(self.selecionarArquivos)
        
        btn3 = QPushButton("Criar 3d",self)
        btn3.setGeometry(200,300,200,35)
        btn3.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
        btn3.clicked.connect(self.criar3d)
    def criar3d(self):
            self.dialog.setText("Selecione o diretório dentro do dataset")
            self.dialog.exec()
            path = easygui.diropenbox()
            name = self.input.getText(self, 'input dialog', 'Escreva o nome do arquivo para textura ')
            reconstruir.exec(path, name[0])
            self.dialog.setText("Finalizado")
            self.dialog.exec()
    def janelaCriarPasta(self):
        try:
            main.close()
            janela.show()
        except:
            print("Erro ao abrir janela de criação de pastas")
    def selecionarArquivos(self):
        try:
            self.dialog.setText("O loop ira executar 8 vezes, para selecionar os arquivos necessários, 4 imagens e 4 pcds. Selecione o arquivo e em seguida o diretório")
            self.dialog.exec()
            for i in range(8):
                self.dialog.exec()
                path = easygui.fileopenbox()
                path2 = easygui.diropenbox()
                shutil.copy2(path, path2)
        except:
            print("me mama")
def rodar():
    main.show()
    app.exec()        

main = MainWindow()
janela = JanelaPasta()
rodar()
