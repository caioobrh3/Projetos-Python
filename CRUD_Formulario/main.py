from tkinter import *
from tkinter import font
from cgitb import text
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
from tkinter import messagebox

from view import *


# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

janela = Tk()
janela.title()
janela.geometry("1043x453")
janela.configure(bg=co9)
janela.resizable(width=FALSE,height=FALSE)

# Frames

frame_cima = Frame(janela,width=310,height=50,bg=co2,relief=FLAT)
frame_cima.grid(row=0,column=0)

frame_baixo = Frame(janela,width=310,height=400,bg=co1,relief=FLAT)
frame_baixo.grid(row=1,column=0,sticky=NSEW,padx=0,pady=1)

frame_direita = Frame(janela,width=588,height=400,bg=co1,relief=FLAT)
frame_direita.grid(row=0,column=1,rowspan=2,padx=1,pady=0,sticky=NSEW)

# label

app_nome = Label(frame_cima,text='Lista de consultas',anchor=NW,bg=co2,fg=co1,relief=FLAT,font=("Ivy 13 bold"))
app_nome.place(x=75,y=15)

global tree

def inserir():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_telefone.get()
    dia = e_cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()

    lista = [nome,email,tel,dia,estado,assunto]

    if nome == "":
        messagebox.showerror('Erro','O nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso','Os dados foram inserido')

        e_nome.delete(0,END)
        e_email.delete(0,END)
        e_telefone.delete(0,END)
        e_cal.delete(0,END)
        e_estado.delete(0,END)
        e_assunto.delete(0,END)
    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        e_cal.delete(0, END)
        e_estado.delete(0, END)
        e_assunto.delete(0, END)

        e_nome.insert(0,tree_lista[1])
        e_email.insert(0,tree_lista[2])
        e_telefone.insert(0,tree_lista[3])
        e_cal.insert(0,tree_lista[4])
        e_estado.insert(0,tree_lista[5])
        e_assunto.insert(0,tree_lista[6])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_telefone.get()
            dia = e_cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()

            lista = [nome, email, tel, dia, estado, assunto,valor_id]

            if nome == "":
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados')

                e_nome.delete(0, END)
                e_email.delete(0, END)
                e_telefone.delete(0, END)
                e_cal.delete(0, END)
                e_estado.delete(0, END)
                e_assunto.delete(0, END)
            for widget in frame_direita.winfo_children():
                widget.destroy()
            mostrar()

        b_confirmar = Button(frame_baixo, text='Confirmar',command=update, width=10, bg=co2, fg=co1, font=("Ivy 7 bold"),relief=RAISED, overrelief=RIDGE, anchor=CENTER)
        b_confirmar.place(x=110, y=375)


    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados')




# baixo

l_nome = Label(frame_baixo,text='Nome',anchor=NW,bg=co1,fg=co4,relief=FLAT,font=("Ivy 10 bold"))
l_nome.place(x=10,y=10)
e_nome = Entry(frame_baixo,width=45,justify=LEFT,relief=SOLID,)
e_nome.place(x=10,y=40)

l_email = Label(frame_baixo,text='Email',anchor=NW,bg=co1,fg=co4,relief=FLAT,font=("Ivy 10 bold"))
l_email.place(x=10,y=65)
e_email = Entry(frame_baixo,width=45,justify=LEFT,relief=SOLID,)
e_email.place(x=10,y=90)

l_telefone = Label(frame_baixo,text='Telefone',anchor=NW,bg=co1,fg=co4,relief=FLAT,font=("Ivy 10 bold"))
l_telefone.place(x=10,y=120)
e_telefone = Entry(frame_baixo,width=45,justify=LEFT,relief=SOLID,)
e_telefone.place(x=10,y=150)

l_cal = Label(frame_baixo,text='Data consulta',anchor=NW,bg=co1,fg=co4,relief=FLAT,font=("Ivy 10 bold"))
l_cal.place(x=10,y=190)
e_cal = DateEntry(frame_baixo,width=12,background='darkblue')
e_cal.place(x=12,y=213)

l_estado = Label(frame_baixo,text='Estado da consulta',anchor=NW,bg=co1,fg=co4,relief=FLAT,font=("Ivy 10 bold"))
l_estado.place(x=160,y=190)
e_estado = Entry(frame_baixo,width=20,justify=LEFT,relief=SOLID,)
e_estado.place(x=162,y=213)

l_assunto = Label(frame_baixo,text='Informação extra',anchor=NW,bg=co1,fg=co4,relief=FLAT,font=("Ivy 10 bold"))
l_assunto.place(x=10,y=260)
e_assunto = Entry(frame_baixo,width=45,justify=LEFT,relief=SOLID,)
e_assunto.place(x=13,y=285)

# botao

b_inserir = Button(frame_baixo,command=inserir,text='Inserir',width=10,bg=co6,fg=co1,font=("Ivy 9 bold"),relief=RAISED,overrelief=RIDGE,anchor=CENTER)
b_inserir.place(x=13,y=340)

b_atualizar = Button(frame_baixo,command=atualizar,text='Atualizar',width=10,bg=co2,fg=co1,font=("Ivy 9 bold"),relief=RAISED,overrelief=RIDGE,anchor=CENTER)
b_atualizar.place(x=100,y=340)

b_apagar = Button(frame_baixo,text='Deletar',width=10,bg=co7,fg=co1,font=("Ivy 9 bold"),relief=RAISED,overrelief=RIDGE,anchor=CENTER)
b_apagar.place(x=190,y=340)

#codigo

def mostrar():

    global tree

    lista = motrar_info()

    tabela_head = ['ID', 'Nome', 'email', 'telefone', 'Data', 'Estado', 'Sobre']

    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()

janela.mainloop()