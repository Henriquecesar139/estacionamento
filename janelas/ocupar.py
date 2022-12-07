from tkinter import *

def ocupar():
    if status[int(vaga.get()) - 1] == 'ocupado':
        msg['text'] = 'vaga já ocupada'
    else:
        status[int(vaga.get()) - 1] = 'ocupado'
        placas[int(vaga.get()) - 1] = placa.get()
        custo[int(vaga.get()) - 1] = int(tempo.get()) * preco
    
        arq2 = open('janelas/vagas.txt', 'w')
        for c in range(0, len(vagas)):
            arq2.write(f'{vagas[c]} | {status[c]} | {custo[c]} | {placas[c]}\n')
        msg['text'] = 'Sucesso'
        arq3 = open('janelas/historico.txt', 'a')
        arq3.write(f'vaga {vaga.get()} ocupada por {tempo.get()} horas\n')

arq = open('janelas/vagas.txt', 'r')
preco = int(open('janelas/preco.txt', 'r').read())

tela = Tk()
tela.geometry('300x400')
tela.title('Ocupar')
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


msg = Label(tela, text = '\n')
msg.pack(side = TOP)

msg2 = Label(tela, text = 'Vaga')
msg2.pack(side = TOP)

vaga = Entry(tela)
vaga.pack(side = TOP)

msg3 = Label(tela, text = '\n\nplaca')
msg3.pack(side = TOP)

placa = Entry(tela)
placa.pack(side = TOP)

msg3 = Label(tela, text = '\n\nTempo (em horas) que a vaga ficará ocupada')
msg3.pack(side = TOP)

tempo = Entry(tela)
tempo.pack(side = TOP)

bt = Button(tela, text = 'ocupar', height=2, width=10, command=ocupar)
bt.pack(side = BOTTOM)

tela.mainloop()