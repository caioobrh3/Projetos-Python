import tkinter
from tkinter import *
from tkinter import ttk


# cores
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

janela = Tk()
janela.title()
janela.geometry("260x370")
janela.configure(bg=fundo)
janela.resizable(width=FALSE,height=FALSE)

# Frame

frame_cima = Frame(janela,width=240,height=100,bg=co1,relief=RAISED)
frame_cima.grid(row=0,column=0,sticky=NW,padx=10,pady=10)

frame_corpo = Frame(janela,width=240,height=300,bg=fundo,relief=FLAT)
frame_corpo.grid(row=1,column=0,sticky=NW)

# config freme cima

app_x = Label(frame_cima,text="X",height=1,relief=FLAT,anchor=CENTER,font=("Ivy 40 bold"),bg=co1,fg=co7)
app_x.place(x=25,y=10)

app_x = Label(frame_cima,text="Jogador 1",height=1,relief=FLAT,anchor=CENTER,font=("Ivy 7 bold"),bg=co1,fg=co0)
app_x.place(x=17,y=70)

app_xpontos = Label(frame_cima,text="0",height=1,relief=FLAT,anchor=CENTER,font=("Ivy 30 bold"),bg=co1,fg=co0)
app_xpontos.place(x=80,y=20)

app_separador = Label(frame_cima,text=":",height=1,relief=FLAT,anchor=CENTER,font=("Ivy 30 bold"),bg=co1,fg=co0)
app_separador.place(x=110 ,y=20)

app_o = Label(frame_cima,text="O",height=1,relief=FLAT,anchor=CENTER,font=("Ivy 40 bold"),bg=co1,fg=co4)
app_o.place(x=170 ,y=10)

app_o = Label(frame_cima,text="Jogador 2",height=1,relief=FLAT,anchor=CENTER,font=("Ivy 7 bold"),bg=co1,fg=co0)
app_o.place(x=165,y=70)

app_opontos = Label(frame_cima,text="0",height=1,relief=FLAT,anchor=CENTER,font=("Ivy 30 bold"),bg=co1,fg=co0)
app_opontos.place(x=130,y=20)


# logica

jogador_1 = "X"
jogador_2 = "O"

ponto_1 = 0
ponto_2 = 0

tabela = [['1','2','3'],['4','5','6'],['7','8','9']]

jogando = "X"
joga = ""
contador = 0

def iniciar_jogo():
    def controle(i):
        global jogando
        global contador
        global jogar

        if i == str(1):
            if b_0['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[[0][0]] = jogando

                if jogando =='X':
                    jogando = 'O'
                    jogar = 'jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                contador += 1








    def vencedor():
        pass

    def terminar():
        pass

    # linhas

    app_ = Label(frame_corpo, text="", height=23, relief=FLAT, pady=5, anchor=CENTER, font=("Ivy 5 bold"), bg=co0,
                 fg=co4)
    app_.place(x=90, y=15)
    app_ = Label(frame_corpo, text="", height=23, relief=FLAT, pady=5, anchor=CENTER, font=("Ivy 5 bold"), bg=co0,
                 fg=co4)
    app_.place(x=157, y=15)

    app_ = Label(frame_corpo, text=" ", width=47, relief=FLAT, pady=1, anchor=CENTER, font=("Ivy 5 bold"), bg=co0,
                 fg=co4)
    app_.place(x=30, y=63)
    app_ = Label(frame_corpo, text=" ", width=47, relief=FLAT, pady=1, anchor=CENTER, font=("Ivy 5 bold"), bg=co0,
                 fg=co4)
    app_.place(x=30, y=127)

    # boton

    b_0 = Button(frame_corpo,command=lambda:controle('1'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_0.place(x=30 ,y=15)
    b_1 = Button(frame_corpo,command=lambda:controle('2'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_1.place(x=96 ,y=15)
    b_2 = Button(frame_corpo,command=lambda:controle('3'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_2.place(x=163 ,y=15)

    b_3 = Button(frame_corpo,command=lambda:controle('4'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_3.place(x=30 ,y=75)
    b_4 = Button(frame_corpo,command=lambda:controle('5'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_4.place(x=96 ,y=75)
    b_5 = Button(frame_corpo,command=lambda:controle('6'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_5.place(x=163 ,y=75)

    b_6 = Button(frame_corpo,command=lambda:controle('7'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_6.place(x=30 ,y=135)
    b_7 = Button(frame_corpo,command=lambda:controle('8'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_7.place(x=96 ,y=135)
    b_8 = Button(frame_corpo,command=lambda:controle('9'),text=" ",width=3,height=1,font=("Ivy 20 bold"),overrelief=RIDGE,relief=FLAT,bg=fundo,fg=co7)
    b_8.place(x=163 ,y=135)

# jogar

b_jogar = Button(frame_corpo,command=iniciar_jogo,text="Jogar",width=10,height=1,font=("Ivy 10 bold"),overrelief=RIDGE,relief=RAISED,bg=fundo,fg=co0)
b_jogar.place(x=85 ,y=210)


janela.mainloop()
