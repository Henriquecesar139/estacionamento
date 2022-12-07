from tkinter import *
from os import system
import webbrowser

def logar():
    global aut
    system('python janelas/login.py')
    arq = open('janelas/aut.txt', 'r')
    aut = arq.read()

def cadastrar():
    system('python janelas/cadastro.py')

def ver():
    system('python janelas/ver.py')

def ocupar():
    print(aut)
    if aut == '1':
        system('python janelas/ocupar.py')
    else:
        system('python aviso.py')

def desocupar():
    if aut == '1':
        system('python janelas/desocupar.py')
    else:
        system('python aviso.py')

def historico():
    system('python janelas/hist.py')

def definicoes():
    if aut == '1':
        system('python janelas/definicoes.py')
    else:
        system('python aviso.py')

arq = open('janelas/aut.txt', 'w')
arq.write('0')
arq = open('janelas/aut.txt', 'r')
aut = arq.read()

tela = Tk()
tela.geometry('248x200')
tela.title('Estacionamento')
tela.resizable(False, False)

login = Button(tela, text = 'login', width = 12, height = 2, command=logar)
login.grid(row = 0, column = 0)

cadastro = Button(tela, text = 'cadastro', width = 12, height = 2, command=cadastrar)
cadastro.grid(row = 0, column = 1)

ver_vagas = Button(tela, text = 'Ver vagas', width = 12, height = 2, command=ver)
ver_vagas.grid(row = 1, column = 0)

ocupar_vagas = Button(tela, text = 'Ocupar vagas', width = 12, height = 2, command=ocupar)
ocupar_vagas.grid(row = 1, column = 1)

desocupar_vagas = Button(tela, text = 'Desocupar vagas', width = 12, height = 2, command=desocupar)
desocupar_vagas.grid(row = 2, column = 0)

relatorio = Button(tela, text = 'relatório', width = 12, height = 2, command=historico)
relatorio.grid(row = 2, column = 1)

admin = Button(tela, text = 'Página de admin', width = 12, height = 2, command=definicoes)
admin.grid(row = 3, column = 0)

git = Button(tela, text="GITHUB", command=lambda: webbrowser.open('https://github.com/henriquecesar139'), width = 12, height = 2)
git.grid(row = 3, column = 1)

tela.mainloop()
