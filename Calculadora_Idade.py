from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry

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

# Contador

data_anos = Label(freme_baixo,text="27",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Ivi 25 bold"),anchor=CENTER)
data_anos.place(x=53,y=135)
data_anos_nome = Label(freme_baixo,text="Anos",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Ivi 11 bold"),anchor=CENTER)
data_anos_nome.place(x=50,y=175)

data_meses = Label(freme_baixo,text="11",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Ivi 25 bold"),anchor=CENTER)
data_meses.place(x=133,y=135)
data_meses_nome = Label(freme_baixo,text="Meses",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Ivi 11 bold"),anchor=CENTER)
data_meses_nome.place(x=130,y=175)

data_dias = Label(freme_baixo,text="27",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Ivi 25 bold"),anchor=CENTER)
data_dias.place(x=211,y=135)
data_dias_nome = Label(freme_baixo,text="Dias",fg=cor3,bg=cor2,height=1,padx=0,relief=FLAT,font=("Ivi 11 bold"),anchor=CENTER)
data_dias_nome.place(x=210,y=175)



janela.mainloop()