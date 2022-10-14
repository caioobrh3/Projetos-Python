from tkinter import *
from tkinter import ttk

# cores ---------------

co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#6f9fbd"  # azul / blue
fundo = "#484F60"

janela = Tk()
janela.title("")
janela.geometry("320x350")
janela.configure(bg=fundo)
janela.resizable(width=FALSE,height=FALSE)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)

# Frame

frame_cima = Frame(janela,width=320,height=50,bg=co1,pady=0,padx=0,relief=FLAT)
frame_cima.grid(row=1,column=0)

frame_baixo = Frame(janela,width=320,height=300,bg=fundo,pady=0,padx=0,relief=FLAT)
frame_baixo.grid(row=2,column=0,sticky=NW)



janela.mainloop()