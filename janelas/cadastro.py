from tkinter import *

def cadastrar():
    arq = open('janelas/user.txt', 'a')
    arq.write(f'{nome.get()} | {senha.get()}\n')


tela = Tk()
tela.geometry('250x300')
tela.title('Cadastro')
tela.resizable(False, False)

msg = Label(tela, text='Nome\n')
msg.pack(side = TOP)

nome = Entry(tela)
nome.pack(side = TOP)

msg = Label(tela, text='\nSenha\n')
msg.pack(side = TOP)

senha = Entry(tela)
senha.pack(side = TOP)

cad = Button(tela, text = 'logar', width = 8, height = 2, command=cadastrar)
cad.pack(side = BOTTOM)

tela.mainloop()