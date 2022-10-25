from operator import le
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)
janelaPasta = QWidget()
le = QLineEdit("",janelaPasta)

def criarPasta():
    pasta = le.text()
    print(pasta)


def main():
    janela = QWidget()
    janela.resize(600,500)
    janela.setWindowTitle("Backyardigans")

    btn = QPushButton("Criar pasta",janela)
    btn.setGeometry(100,100,100,30)
    btn.setStyleSheet('background-color:#55A38B; color:#FFFFFF')


    janela.show()
    app.exec()
    
def janelaCriarPasta():
    janelaPasta.resize(600,500)
    janelaPasta.setWindowTitle("Backyardigans")

    btn = QPushButton("Criar pasta",janelaPasta)
    btn.setGeometry(200,300,200,35)
    btn.setStyleSheet('background-color:#55A38B; color:#FFFFFF')
    btn.clicked.connect(criarPasta)

    label = QLabel("Insira o nome da pasta:",janelaPasta)
    label.setStyleSheet('font-size:15pt arial;')
    label.move(100,200)
    
    le.setGeometry(310,200,200,30)


    janelaPasta.show()
    app.exec()

janelaCriarPasta()