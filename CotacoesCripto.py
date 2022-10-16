import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']


    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cot["text"] = texto

janela = Tk()
janela.title("Cotação atual moedas")

texto_orientcao = Label(janela, text="Clique para ver as cotações")
texto_orientcao.grid(column=0,row=0)

botao = Button(janela,text="Buscar cotações",command=pegar_cotacoes)
botao.grid(column=0,row=1)

texto_cot = Label(janela,text="")
texto_cot.grid(column=0,row=2)

janela.mainloop()