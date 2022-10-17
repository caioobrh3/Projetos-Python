from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random

# cores
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

frame_cima = Frame(janela,width=260,height=100,bg=co1,relief=RAISED)
frame_cima.grid(row=0,column=0,sticky=NW )

frame_baixo = Frame(janela,width=260,height=300,bg=co0,relief=FLAT)
frame_baixo.grid(row=1,column=0,sticky=NW )

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Label

app_1 = Label(frame_cima,text='Voce',height=1,anchor=CENTER,font=('Ivy 10 bold'),bg=co1,fg=co0)
app_1.place(x=25,y=75)

app_1_linha = Label(frame_cima,text='',height=10,anchor=CENTER,font=('Ivy 10 bold'),bg=co0,fg=co0)
app_1_linha.place(x=0,y=0)

app_1_pontos = Label(frame_cima,text='0',height=1,anchor=CENTER,font=('Ivy 30 bold'),bg=co1,fg=co0)
app_1_pontos.place(x=50,y=20)

app_ = Label(frame_cima,text=':',height=1,anchor=CENTER,font=('Ivy 30 bold'),bg=co1,fg=co0)
app_.place(x=125,y=20)


app_2_pontos = Label(frame_cima,text='0',height=1,anchor=CENTER,font=('Ivy 30 bold'),bg=co1,fg=co0)
app_2_pontos.place(x=170,y=20)

app_2 = Label(frame_cima,text='PC',height=1,anchor=CENTER,font=('Ivy 10 bold'),bg=co1,fg=co0)
app_2.place(x=205,y=75)

app_2_linha = Label(frame_cima,text='',height=10,anchor=CENTER,font=('Ivy 10 bold'),bg=co0,fg=co0)
app_2_linha.place(x=255,y=0)

app_linha = Label(frame_cima,text='',width=255,anchor=CENTER,font=('Ivy 1 bold'),bg=co0,fg=co0)
app_linha.place(x=0,y=95)

app_pc = Label(frame_baixo,text='',height=1,anchor=CENTER,font=('Ivy 10 bold'),bg=co0,fg=co0)
app_pc.place(x=190,y=10)
# jogo

global voce
global pc
global rondas
global pontos_vc
global pontos_pc

pontos_vc = 0
pontos_pc = 0
rondas = 5

def jogar(i):
    global rondas
    global pontos_vc
    global pontos_pc

    if rondas >0:
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i
        app_pc['text'] = pc
        app_pc['fg'] = co1

        if voce == 'Pedra' and pc == 'Pedra':
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'Papel' and pc == 'Papel':
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'Tesoura' and pc == 'Tesoura':
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'Pedra' and pc == 'Papel':
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10

        elif voce == 'Pedra' and pc == 'Tesoura':
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_vc += 10

        elif voce == 'Papel' and pc == 'Tesoura':
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10

        # tras

        elif voce == 'Tesoura' and pc == 'Papel':
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_vc += 10

        elif voce == 'Tesoura' and pc == 'Pedra':
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10

        elif voce == 'Papel' and pc == 'Pedra':
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_vc += 10

        app_1_pontos['text'] = pontos_vc
        app_2_pontos['text'] = pontos_pc

        rondas -=1

    else:
        app_1_pontos['text'] = pontos_vc
        app_2_pontos['text'] = pontos_pc

        fim_do_jogo()

def iniciar_jogo():

    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('pedra.png')
    icon_1 = icon_1.resize((50, 50))
    icon_1 = ImageTk.PhotoImage(icon_1)

    b_icon_1 = Button(frame_baixo,command=lambda:jogar("Pedra"), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 1 bold'),
                      anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('Papel.png')
    icon_2 = icon_2.resize((50, 50))
    icon_2 = ImageTk.PhotoImage(icon_2)

    b_icon_2 = Button(frame_baixo,command=lambda:jogar("Papel"), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 1 bold'),
                      anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=60)

    icon_3 = Image.open('Tesoura.png')
    icon_3 = icon_3.resize((50, 50))
    icon_3 = ImageTk.PhotoImage(icon_3)

    b_icon_3 = Button(frame_baixo,command=lambda:jogar("Tesoura"), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 1 bold'),
                      anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)

def fim_do_jogo():
    global rondas
    global pontos_vc
    global pontos_pc

    pontos_vc = 0
    pontos_pc = 0
    rondas = 5

    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    jogador_vc = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    if jogador_vc > jogador_pc:
        app_vencedor = Label(frame_baixo, text='Parabens voce Ganhou', height=1, anchor=CENTER, font=('Ivy 10 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)
    elif jogador_vc < jogador_pc:
        app_vencedor = Label(frame_baixo, text='Infelizmente voce Perdeu', height=1, anchor=CENTER, font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text='EMPATE', height=1, anchor=CENTER, font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=5, y=60)

    def jogar_novamente():
        app_1_pontos['text'] = 0
        app_2_pontos['text'] = 0
        app_vencedor.destroy()
        b_novamente.destroy()
        iniciar_jogo()

    b_novamente = Button(frame_baixo, command=jogar_novamente, width=30, text='Jogar novamente', bg=fundo, fg=co0,
                         font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_novamente.place(x=5, y=151)


# Jogar

b_jogar = Button(frame_baixo,command=iniciar_jogo,width=30,text='Jogar',bg=fundo,fg=co0,font=('Ivy 10 bold'),anchor=CENTER,relief=RAISED,overrelief=RIDGE)
b_jogar.place(x=5,y=151)


janela.mainloop()