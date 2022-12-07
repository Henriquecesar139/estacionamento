from tkinter import *

arq = open('janelas/vagas.txt', 'r')

tela = Tk()
tela.geometry('300x400')
tela.title('Ver vagas')
tela.resizable(False, True)

lb = Label(tela, text='vaga  |  status  |  R$ |  placa').pack(side = TOP)

for c in arq:
    if 'livre' in c:
        lb = Label(tela, text = c, fg = 'green')
        lb.pack(side = TOP)
    if 'ocupado' in c:
        lb = Label(tela, text = c, fg = 'red')
        lb.pack(side = TOP)

tela.mainloop()
