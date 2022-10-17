import tkinter
from tkinter import *
from tkinter import ttk

# cores
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#004338"

janela = Tk()
janela.title('')
janela.geometry('530x205')
janela.configure(bg=cor1)



# Label

tela = Label(janela,bg=cor0,width=40,height=10,bd=1)
tela.grid(row=0,column=0)

frame_direira = Frame(janela,bg=cor1,)
frame_direira.grid(row=0,column=1,pady=5)

frame_baixo = Frame(janela,bg=cor1,)
frame_baixo.grid(row=1,column=0,columnspan=2,pady=15)

# codigo

def escala(valor):
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()
    rgb = f'{r},{g},{b}'
    hexadecimal = '#%02x%02x%02x'%(r, g, b)

    tela['bg'] = hexadecimal
    e_cor.delete(0,END)
    e_cor.insert(0, hexadecimal)



#clicacommand=escala),r
def onClicar():

    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()



# frame direira

l_red = Label(frame_direira,text="Red",width=7,bg=cor1,fg='red',anchor=NW,font=('Time New Roman',12,'bold'))
l_red.grid(row=0,column=0)
s_red=Scale(frame_direira,command=escala,from_=0,to=255,length=150,bg=cor1,fg='red',orient=HORIZONTAL)
s_red.grid(row=0,column=1)

l_green = Label(frame_direira,text="Green",width=7,bg=cor1,fg='green',anchor=NW,font=('Time New Roman',12,'bold'))
l_green.grid(row=1,column=0)
s_green=Scale(frame_direira,command=escala,from_=0,to=255,length=150,bg=cor1,fg='green',orient=HORIZONTAL)
s_green.grid(row=1,column=1)

l_blue = Label(frame_direira,text="Blue",width=7,bg=cor1,fg='blue',anchor=NW,font=('Time New Roman',12,'bold'))
l_blue.grid(row=2,column=0)
s_blue=Scale(frame_direira,command=escala,from_=0,to=255,length=150,bg=cor1,fg='blue',orient=HORIZONTAL)
s_blue.grid(row=2,column=1)

# frame baixo

l_rgb = Label(frame_baixo,text="CÒDIGO HEX :",bg=cor1,font=('Ivy',12,'bold'))
l_rgb.grid(row=0,column=0,padx=5)

e_cor = Entry(frame_baixo,width=12,font=('Ivy',12,'bold'),justify=CENTER)
e_cor.grid(row=0,column=1,padx=5)

# botao copiar

b_copiar = Button(frame_baixo,command=onClicar,text="Copiar a cor",bg=cor1,font=('Ivy',8,'bold'),relief=RAISED,overrelief=RIDGE)
b_copiar.grid(row=0,column=2,padx=5)


# app nome

l_nome = Label(frame_baixo,text="Seletor de Cores",bg=cor1,font=('Ivy',15,'bold'))
l_nome.grid(row=0,column=3,padx=15)

janela.mainloop()