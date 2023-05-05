import requests
from tkinter import *

def cotacoes():
  requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

  requisicao_doc = requisicao.json()

  cota_dolar = requisicao_doc['USDBRL']['bid']
  cota_euro = requisicao_doc['EURBRL']['bid']
  cota_bitcon = requisicao_doc['BTCBRL']['bid']  

  texto = f'''
          Dolar: {cota_dolar}
          Euro: {cota_euro}
          Bitcon: {cota_bitcon}'''

  texto_cotacao["text"] = texto

janela = Tk()
janela.title("Cotações de moeda ")
janela.geometry("300x200")


texto = Label(janela, text="Verificar cotações atuais das moedas USD - EUR - BTC")
texto.grid(column=2, row=0, padx=10, pady=10)

botao = Button(janela, text= "Atualizar cotações", command=cotacoes) 
botao.grid(column=2, row=1, padx=10, pady=10)

texto_cotacao = Label(janela, text = "")
texto_cotacao.grid(column=2, row=2, padx=10, pady=10)

janela.mainloop()