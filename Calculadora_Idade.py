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

# Label baixo

data_incio = Label(freme_baixo,text="Data inicial",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Arial 11"),anchor=NW)
data_incio.place(x=40,y=30)

cal_1 = DateEntry(freme_baixo, width=13,bg="darkblue",fg=cor3,borderwidth=2,date_patter="mm/dd/y",y=2021)
cal_1.place(x=180,y=30)

data_nas = Label(freme_baixo,text="Data de nascimento",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Arial 11"),anchor=NW)
data_nas.place(x=40,y=70)

cal_2 = DateEntry(freme_baixo, width=13,bg="darkblue",fg=cor3,borderwidth=2,date_patter="mm/dd/y",y=2021)
cal_2.place(x=180,y=70)



janela.mainloop()