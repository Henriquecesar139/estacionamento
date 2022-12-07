from tkinter import *

def mudancas():
    try:
        valor = int(preco.get())
        arq = open('janelas/preco.txt', 'w')
        arq.write(str(valor))
        n = int(nvagas.get())
        arq = open('janelas/vagas.txt', 'w')
        for c in range(1, n + 1):
            arq.write(f'{c} | livre | 0 | 0\n')
        arq = open('janelas/historico.txt', 'w')
        status['text'] = 'Sucesso'
        status['fg'] = 'green'
    except:
        status['text'] = 'erro'
        status['fg'] = 'red'

tela = Tk()
tela.resizable(False, False)
tela.title('Admin')
tela.geometry('300x240')

status = Label(tela)
status.pack(side = TOP)

msg = Label(tela, text = 'Número de vagas\n')
msg.pack(side = TOP)

nvagas = Entry(tela)
nvagas.pack(side = TOP)

msg2 = Label(tela, text = 'Preço por hora\n')
msg2.pack(side = TOP)

preco = Entry(tela)
preco.pack(side = TOP)

conf = Button(tela, text = 'Confirmar', width = 10, height = 2, command=mudancas)
conf.pack(side = BOTTOM)

tela.mainloop()