from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

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

# Func

unidades = {"Massa":[{"kg":1000},{"hg":100},{"dag":10},{"g":1},{"dg":0.1},{"cg":0.01},{"mg":0.001}],
            "Tempo": [{"hr": 1000}, {"mm": 100}, {"s": 10}, {"ms": 1}, {"ns": 0.1}, {"nns": 0.01}, {"nnns": 0.001}],
            "Comprimento": [{"KM": 1000}, {"hm": 100}, {"dam": 10}, {"m": 1}, {"dm": 0.1}, {"cm": 0.01}, {"mm": 0.001}],
            "Area": [{"KM": 1000}, {"hm": 100}, {"dam": 10}, {"m": 1}, {"dm": 0.1}, {"cm": 0.01}, {"mm": 0.001}],
            "Quantidade": [{"KM": 1000}, {"hm": 100}, {"dam": 10}, {"m": 1}, {"dm": 0.1}, {"cm": 0.01}, {"mm": 0.001}],
            "Velocidade": [{"KM": 1000}, {"hm": 100}, {"dam": 10}, {"m": 1}, {"dm": 0.1}, {"cm": 0.01}, {"mm": 0.001}],
            "Temperatura": [{"KM": 1000}, {"hm": 100}, {"dam": 10}, {"m": 1}, {"dm": 0.1}, {"cm": 0.01}, {"mm": 0.001}],
            "Energia": [{"KM": 1000}, {"hm": 100}, {"dam": 10}, {"m": 1}, {"dm": 0.1}, {"cm": 0.01}, {"mm": 0.001}],
            "Pressao": [{"KM": 1000}, {"hm": 100}, {"dam": 10}, {"m": 1}, {"dm": 0.1}, {"cm": 0.01}, {"mm": 0.001}],
            }

def mostrar_menu(i):

    unidades_de = []
    unidades_para = []
    unidades_valores = []

    for j in unidades[i]:
        for k,v in j.items():
            unidades_de.append(k)
            unidades_para.append(k)
            unidades_valores.append(v)

    c_de["values"] = unidades_de
    c_para["values"] = unidades_para

    l_unidade_nome["text"] = i

    l_info = Label(frame_direita, text="Digite o numero", width=16, height=2, padx=0, pady=3,relief=FLAT, fg=cor1, bg=cor2,anchor=NW, font=("Ivy 10 bold"))
    l_info.place(x=0, y=110)

    e_numero = Entry(frame_direita,width=9,font=("Ivy 15 bold"),justify=CENTER,relief=SOLID)
    e_numero.place(x=0,y=150)

    b_calcular = Button(frame_direita, text="Calcular", width=8, height=1, fg=cor2, bg=cor3, overrelief=RIDGE, relief=RAISED, anchor=NW,font=("Ivy 10 bold"))
    b_calcular.place(x=115,y=150)




# estilo

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Label cima

l_app_nome = Label(frame_cima,text="Calculadora De Unidade de Medidas",height=1,padx=0,fg=cor3,bg=cor2,anchor=CENTER,font=("Ivy 15 bold"))
l_app_nome.place(x=50,y=10)

# Botao Massa

img_0 = Image.open("images/balanca.png")
img_0 = img_0.resize((50,50))
img_0 = ImageTk.PhotoImage(img_0)

b_0 = Button(frame_esquerda,command=lambda:mostrar_menu("Massa"),text="Massa",image=img_0,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_0.grid(row=0,column=0,sticky=NSEW,padx=5,pady=5)

# Tempo

img_1 = Image.open("images/relogio.png")
img_1 = img_1.resize((50,50))
img_1 = ImageTk.PhotoImage(img_1)

b_1 = Button(frame_esquerda,command=lambda:mostrar_menu("Tempo"),text="Tempo",image=img_1,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_1.grid(row=0,column=1,sticky=NSEW,padx=5,pady=5)

# Comprimento

img_2 = Image.open("images/a-medida.png")
img_2 = img_2.resize((50,50))
img_2 = ImageTk.PhotoImage(img_2)

b_2 = Button(frame_esquerda,command=lambda:mostrar_menu("Comprimento"),text="Comprimento",image=img_2,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_2.grid(row=0,column=2,sticky=NSEW,padx=5,pady=5)

# Àrea

img_3 = Image.open("images/area.png")
img_3 = img_3.resize((50,50))
img_3 = ImageTk.PhotoImage(img_3)

b_3 = Button(frame_esquerda,command=lambda:mostrar_menu("Area"),text="Àrea",image=img_3,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_3.grid(row=1,column=0,sticky=NSEW,padx=5,pady=5)

# Quantidade

img_4 = Image.open("images/qunatidade.png")
img_4 = img_4.resize((50,50))
img_4 = ImageTk.PhotoImage(img_4)

b_4 = Button(frame_esquerda,command=lambda:mostrar_menu("Quantidade"),text="Quantidade",image=img_4,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_4.grid(row=1,column=1,sticky=NSEW,padx=5,pady=5)

# Velocidade

img_5 = Image.open("images/alta-velocidade.png")
img_5 = img_5.resize((50,50))
img_5 = ImageTk.PhotoImage(img_5)

b_5 = Button(frame_esquerda,command=lambda:mostrar_menu("Velocidade"),text="Velocidade",image=img_5,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_5.grid(row=1,column=2,sticky=NSEW,padx=5,pady=5)

# Temperatura

img_6 = Image.open("images/temperatura-alta.png")
img_6 = img_6.resize((50,50))
img_6 = ImageTk.PhotoImage(img_6)

b_6 = Button(frame_esquerda,command=lambda:mostrar_menu("Temperatura"),text="Temperatura",image=img_6,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_6.grid(row=2,column=0,sticky=NSEW,padx=5,pady=5)

# Energia

img_7 = Image.open("images/energia.png")
img_7 = img_7.resize((50,50))
img_7 = ImageTk.PhotoImage(img_7)

b_7 = Button(frame_esquerda,command=lambda:mostrar_menu("Energia"),text="Energia",image=img_7,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_7.grid(row=2,column=1,sticky=NSEW,padx=5,pady=5)

# Pressão

img_8 = Image.open("images/medidor-de-pressao.png")
img_8 = img_8.resize((50,50))
img_8 = ImageTk.PhotoImage(img_8)

b_8 = Button(frame_esquerda,command=lambda:mostrar_menu("Pressao"),text="Pressão",image=img_8,compound=LEFT,width=130,height=50,fg=cor2,bg=cor3,overrelief=SOLID,relief=FLAT,anchor=NW,font=("Ivy 10 bold"))
b_8.grid(row=2,column=2,sticky=NSEW,padx=5,pady=5)

# boton direita

l_unidade_nome = Label(frame_direita,text="----",width=17,height=2,padx=0,relief=GROOVE,fg=cor1,bg=cor2,anchor=CENTER,font=("Ivy 15 bold"))
l_unidade_nome.place(x=0,y=0)

# DE

l_de = Label(frame_direita,text="De",height=1,padx=3,relief=GROOVE,fg=cor1,bg=cor2,anchor=CENTER,font=("Ivy 10 bold"))
l_de.place(x=10,y=70)

c_de = ttk.Combobox(frame_direita,width=5,justify=CENTER,font=("Ivy 8 bold"))
c_de.place(x=38,y=70)

# Para

l_para = Label(frame_direita,text="Para",height=1,padx=3,relief=GROOVE,fg=cor1,bg=cor2,anchor=CENTER,font=("Ivy 10 bold"))
l_para.place(x=100,y=70)

c_para = ttk.Combobox(frame_direita,width=5,justify=CENTER,font=("Ivy 8 bold"))
c_para.place(x=140,y=70)


janela.mainloop()