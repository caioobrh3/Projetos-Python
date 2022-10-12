from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("")
janela.geometry("310x400")

# Cores

cor1 = "#333333" # Preto
cor2 = "#3b3b3b" # cinza
cor3 = "#ffffff" # branco
cor4 = "#dea426" # Laranja

# Frame

freme_cima = Frame(janela, width=310, height=140,pady=0,padx=0,relief=FLAT,bg=cor1)
freme_cima.grid(row=0,column=0)

freme_baixo= Frame(janela, width=310, height=360,pady=0,padx=0,relief=FLAT,bg=cor2)
freme_baixo.grid(row=1,column=0)

# Label cima

l_calculadora = Label(freme_cima,text="Calculadora",fg=cor3 ,width=25,height=1,padx=3,relief=FLAT,anchor=CENTER,font=("Ivi 15 bold"),bg=cor1)
l_calculadora.place(x=0,y=30)

l_idade = Label(freme_cima,text="DE IDADE",fg=cor4 ,width=11,height=1,padx=0,relief=FLAT,anchor=CENTER,font=("Arial 35 bold"),bg=cor1)
l_idade.place(x=0,y=70)


janela.mainloop()