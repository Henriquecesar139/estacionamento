from tkinter import *

def logar():
    arq = open('janelas/user.txt', 'r')
    user = []
    for c in arq:
        user.append(c.split(' | '))
    if [nome.get(), senha.get()+'\n'] in user:
        arq2 = open('janelas/aut.txt', 'w')
        arq2.write('1')
        msg0['text'] = 'Sucesso'
    else:
        msg0['text'] = 'Erro'


tela = Tk()
tela.geometry('250x300')
tela.title('login')
tela.resizable(False, False)

msg0 = msg = Label(tela, text='\n')
msg0.pack(side = TOP)

msg = Label(tela, text='Nome\n')
msg.pack(side = TOP)

nome = Entry(tela)
nome.pack(side = TOP)

msg = Label(tela, text='\nSenha\n')
msg.pack(side = TOP)

senha = Entry(tela)
senha.pack(side = TOP)

log = Button(tela, text = 'logar', width = 8, height = 2, command=logar)
log.pack(side = BOTTOM)

tela.mainloop()