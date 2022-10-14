from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import requests
import json

# cores ---------------

co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#6f9fbd"  # azul / blue
co3 = "#cf8a15" # Laranja
fundo = "#484F60"

janela = Tk()
janela.title("")
janela.geometry("320x350")
janela.configure(bg=fundo)
janela.resizable(width=FALSE,height=FALSE)

def inf():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL"

    response = requests.get(api_link)

    dados = response.json()

    valor_usd = float(dados["USD"])
    valor_formatado_usd = "$ {:,.3f}".format(valor_usd)
    l_p_dolar['text'] = valor_formatado_usd

    valor_eur = float(dados["EUR"])
    valor_formatado_eur = "€ {:,.3f}".format(valor_eur)
    l_p_euro['text'] = "Em Euro são : "+ valor_formatado_eur

    valor_brl = float(dados["BRL"])
    valor_formatado_brl = "R$ {:,.3f}".format(valor_brl)
    l_p_real['text'] ="Em Reais são : "+ valor_formatado_brl

    frame_baixo.after(1000,inf)


# Frame

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)

frame_cima = Frame(janela,width=320,height=50,bg=co1,pady=0,padx=0,relief=FLAT)
frame_cima.grid(row=1,column=0)

frame_baixo = Frame(janela,width=320,height=300,bg=fundo,pady=0,padx=0,relief=FLAT)
frame_baixo.grid(row=2,column=0,sticky=NW)

imagem = Image.open('bitcoin.png')
imagem = imagem.resize((30,30))
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima,image=imagem,compound=RIGHT,bg=co1,relief=FLAT)
l_icon.place(x=250,y=5)

l_icon = Label(frame_cima,image=imagem,compound=LEFT,bg=co1,relief=FLAT)
l_icon.place(x=50,y=5)

l_nome = Label(frame_cima,text="Bitcoin Valor",bg=co1,fg=co3,relief=FLAT,anchor=CENTER,font=("Arial 18 bold"))
l_nome.place(x=90,y=5)

# baixo

l_p_dolar = Label(frame_baixo,text=" ",bg=fundo,fg=co1,relief=FLAT,anchor=CENTER,font=("Arial 20 "))
l_p_dolar.place(x=10,y=50)

l_p_euro = Label(frame_baixo,text="",bg=fundo,fg=co1,relief=FLAT,anchor=CENTER,font=("Arial 12 "))
l_p_euro.place(x=10,y=130)

l_p_real = Label(frame_baixo,text="",bg=fundo,fg=co1,relief=FLAT,anchor=CENTER,font=("Arial 12 "))
l_p_real.place(x=10,y=160)

inf()

janela.mainloop()