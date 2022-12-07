from tkinter import *

tela = Tk()
tela.resizable(False, False)
tela.title('Erro')
tela.geometry('200x50')

Label(tela, text = 'Necessário Login', fg = 'red', font = 'arial 15 bold').pack(side = TOP)

tela.mainloop()