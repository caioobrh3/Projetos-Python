from tkinter import *
import tkinter

janela = Tk()

o1 = Button(janela,text ="FLAT", overrelief=FLAT )
o1.grid(column=0,row=0)
o2 = Button(janela,text ="RAISED", overrelief=RAISED )
o2.grid(column=0,row=1)
o3 = Button(janela,text ="SUNKEN", overrelief=SUNKEN )
o3.grid(column=0,row=2)
o4 = Button(janela,text ="GROOVE", overrelief=GROOVE )
o4.grid(column=0,row=3)
o5 = Button(janela,text ="RIDGE", overrelief=RIDGE )
o5.grid(column=0,row=4)

janela.mainloop()