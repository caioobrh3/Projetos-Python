import sqlite3 as lite

con = lite.connect('dados.db')


def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome,email,telefone,dia_em,estado,assunto) VALUES (?,?,?,?,?,?)"
        cur.execute(query,i)

def motrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)
    return lista

def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?,assunto=?, WHERE id=?"
        cur.execute(query,lista)


lista = [1]
with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query,lista)


