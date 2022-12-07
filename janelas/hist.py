from tkinter import *

arq = open('janelas/historico.txt', 'r')

tela = Tk()
tela.geometry('300x400')
tela.title('Histórico')
tela.resizable(False, True)

for c in arq:
    Label(tela, text=c,).pack(side = TOP)

tela.mainloop()