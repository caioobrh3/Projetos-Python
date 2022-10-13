from tkinter import *
from tkinter import ttk

# Cores

cor1 = '#3b3b3b' # preta / black
cor2 = '#ffffff' # branca / white
cor3 = '#48b3e0' # azul / blue

janela = Tk()
janela.title()
janela.geometry("650x260")
janela.config(bg=cor1)

# Frames

frame_cima = Frame(janela,width=450,height=50,bg=cor2,pady=0,padx=3,relief=FLAT)
frame_cima.place(x=2,y=2)

frame_esquerda = Frame(janela,width=450,height=220,bg=cor2,pady=0,padx=3,relief=FLAT)
frame_esquerda.place(x=2,y=54)

frame_direita = Frame(janela,width=198,height=260,bg=cor2,pady=0,padx=3,relief=FLAT)
frame_direita.place(x=454,y=2)

# estilo

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Label cima

l_app_nome = Label(frame_cima,text="Calculadora De Unidade de Medidas",height=1,padx=0,fg=cor3,bg=cor2,anchor=CENTER,font=("Ivy 15 bold"))
l_app_nome.place(x=50,y=10)

# Freme esquerda

b_0 = Button(frame_esquerda,text="Peso",width=10,height=2,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_0.grid(row=0,column=0,sticky=NSEW,padx=5,pady=5)


janela.mainloop()