from tkinter import *
from tkinter import ttk
from random import randint
# Cores

cor1 = "#ff0000" # Vermeho
cor2 = "#008c00" # Verde
cor3 = "#000000" # Preto

# Criando Janela

janela = Tk()
janela.title("")
janela.configure(bg=cor3)
janela.geometry("400x200")
janela.resizable(width=False,height=False)

# Fucao

def gerar():
    numero = str(randint(100000000, 999999999))

    novo_cpf = numero
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    cpf['text']=novo_cpf


# Textos

txtGerador = Label(janela,text="GERADOR DE CPF",bg=cor3,fg=cor1,font=('Ivy',20,'bold'))
txtGerador.place(x=75,y=20)

# Criando Botao

bnt = Button(janela,text="Gerar CPF",command=gerar,bg=cor2,font=('Ivy',15,'bold'),relief=RAISED,overrelief=SUNKEN)
bnt.place(x=150,y=70)

#CPF

cpf = Label(janela,text="",bg=cor3,fg=cor2,font=('Ivy',30,'bold'))
cpf.place(x=85,y=120)


janela.mainloop()


