from tkinter import *

def desocupar():
    status[int(vaga.get()) - 1] = 'livre'
    placas[int(vaga.get()) - 1] = '0'
    arq2.write(f'vaga {vaga.get()} desocupada\n')
    custo[int(vaga.get()) - 1] = '0'
    arq = open('janelas/vagas.txt', 'w')
    for c in range(0, len(placas)):
        arq.write(f'{vagas[c]} | {status[c]} | {custo[c]} | {placas[c]}\n')
arq = open('janelas/vagas.txt', 'r')
arq2 = open('janelas/historico.txt', 'a')

tela = Tk()
tela.geometry('300x200')
tela.title('Desocupar')
tela.resizable(False, False)

placas = []
vagas = []
status = []
custo = []

for c in arq:
    vagas.append(c.split(' | ')[0])
    status.append(c.split(' | ')[1])
    custo.append(c.split(' | ')[2])
    placas.append(c.split(' | ')[3].rstrip('\n'))

msg0 = Label(tela, text='Vaga: \n\n')
msg0.pack(side = TOP)

vaga = Entry(tela)
vaga.pack(side = TOP)

des = Button(tela, text = 'desocupar', height=2, width=10, command=desocupar)
des.pack(side = BOTTOM)

tela.mainloop()