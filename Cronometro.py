from tkinter import *
from tkinter import ttk

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela = Tk()
janela.title()
janela.geometry("300x180")
janela.configure(bg=cor1)
janela.resizable(width=FALSE,height=FALSE)

# funcao

tempo = "00:00:00"
rodar = False


# Label

label_app = Label(janela,text="Cronômetro",font=("Arial 10"),bg=cor1,fg=cor2)
label_app.place(x=20,y=5)

label_tempo = Label(janela,text=tempo,font=("Times 50 bold"),bg=cor1,fg=cor6)
label_tempo.place(x=20,y=30)

# Botao

botao_iniciar = Button(janela,text="iniciar",width=10,height=2,bg=cor1,fg=cor2,font=("Ivy 8 bold"),relief=RAISED,overrelief=RIDGE)
botao_iniciar.place(x=20,y=130)

botao_pausar = Button(janela,text="Pausar",width=10,height=2,bg=cor1,fg=cor2,font=("Ivy 8 bold"),relief=RAISED,overrelief=RIDGE)
botao_pausar.place(x=105,y=130)

botao_reiniciar = Button(janela,text="Reiniciar",width=10,height=2,bg=cor1,fg=cor2,font=("Ivy 8 bold"),relief=RAISED,overrelief=RIDGE)
botao_reiniciar.place(x=190,y=130)

janela.mainloop()