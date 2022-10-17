from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

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

# Frame Baixo

icon_1 = Image.open('pedra.png')
icon_1 = icon_1.resize((50,50))
icon_1 = ImageTk.PhotoImage(icon_1)

b_icon_1 = Button(frame_baixo,width=50,image=icon_1,compound=CENTER,bg=co0,fg=co0,font=('Ivy 1 bold'),anchor=CENTER,relief=FLAT)
b_icon_1.place(x=15,y=60)

janela.mainloop()