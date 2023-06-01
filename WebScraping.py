from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import time
import re
import subprocess
from CRUD import *
from Tela_cad import main_cad


def main():

    def requisicao():
    # Instanciando o navegador
        url = "http://www.vinhosevinhos.com/"

        option = Options()
        option.headless = True
        driver = webdriver.Firefox(options=option)

        driver.get(url)
        time.sleep(10)


        driver.find_element(by=By.XPATH, value="/html/body/div[5]/main/div[2]/div/div[4]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]")
            
        busca = driver.find_element(By.XPATH, "/html/body/div[5]/main/div[2]/div/div[4]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]")
        htmlbusca = busca.get_attribute('outerHTML')

        #Utilizando a biblioteca BeautifulSoup para facilitar a busca de elementos HTML
        produtos = BeautifulSoup(htmlbusca, 'html.parser')

        for produto in produtos:
            descricao = produto.find_all_next("a", attrs={'class': re.compile('product-item-link')})
            preco = produto.find_all("span", attrs={"class" : re.compile("price-wrapper")})

        descrivinho = descricao[0].contents[0].text
        precovinho = preco[0].contents[0].text
            
        
        return descrivinho, precovinho
            
        driver.quit()

    def dados_tabela():
        tabelagrid = ['ID', 'Produto', 'Preço', 'Tipo', 'Região', 'Graduação%']

        listaprod = mostrar_dados()

        global tree

        tree = ttk.Treeview(frame_baixo, selectmode="extended", columns=tabelagrid, show="headings", height=20)
        tree.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo, orient="vertical", command=tree.yview)
        vsb.grid(column=1, row=0, padx=10, pady=10, sticky='ns')

        #horizontal scrollbar
        #hsb = ttk.Scrollbar(frame_baixo, orient="horizontal", command=tree.yview)
        #hsb.grid(column=0, row=1, padx=10, pady=10)

        tree.configure(yscrollcommand=vsb.set)

        hd=["center", "center", "center", "center", "center", "center"]
        h=[40, 200, 90, 100, 200, 90]
        n=0
        for c in tabelagrid:
            tree.heading(c, text=c.title(), anchor=CENTER)
            tree.column(c, width=h[n], anchor=hd[n])
            n+=1

        for item in listaprod:
            tree.insert('', 'end', values=item)

    def dados_web():
        tabelagrid = ['Produto Web', 'Preço Web']

        listaprod = requisicao()

        global tree

        tree = ttk.Treeview(frame_cima, selectmode="extended", columns=tabelagrid, show="headings", height=20)
        tree.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_cima, orient="vertical", command=tree.yview)
        vsb.grid(column=1, row=0, padx=5, pady=5, sticky='ns')

        #horizontal scrollbar
        #hsb = ttk.Scrollbar(frame_baixo, orient="horizontal", command=tree.yview)
        #hsb.grid(column=0, row=1, padx=10, pady=10)

        tree.configure(yscrollcommand=vsb.set)

        hd=["center", "center"]
        h=[200, 90]
        n=0
        for c in tabelagrid:
            tree.heading(c, text=c.title(), anchor=CENTER)
            tree.column(c, width=h[n], anchor=hd[n])
            n+=1

        for item in listaprod:
            tree.insert('', 'end', values=item)

    def cad_user():
        arquivo = "cadastra_user.py"
        subprocess.call(["python", arquivo])

    co1 = "#feffff"  # branca

    janela = Tk()
    janela.title("Vinicula Web - Monitoramento de Produtos ")
    janela.geometry("1300x600")
        # Frame parte de Cima
    frame_cima = Frame(janela, width=700, height=300, bg=co1, relief=FLAT)
    frame_cima.grid(column=1, row=2, sticky=NSEW)

    frame_baixo = Frame(janela, width=700, height=300, bg=co1, relief=FLAT)
    frame_baixo.grid(column=0, row=2, sticky=NSEW)

    inserir = Button(janela, text="Cadastrar Produto", command=main_cad, font=('Ivy 10 bold'), bg=co1, overrelief=RIDGE)
    inserir.grid(column=0, row=0, padx=1, pady=10)

    inserir_user = Button(janela, text="Cadastrar Usuario", command=cad_user, font=('Ivy 10 bold'), bg=co1, overrelief=RIDGE)
    inserir_user.grid(column=0, row=1, padx=1, pady=10)

    botao = Button(janela, text= "Buscar Produto Web", command=dados_web, font=('Ivy 10 bold'), bg=co1, overrelief=RIDGE) 
    botao.grid(column=1, row=0, padx=1, pady=10)

    site = Label(janela, text="Link da busca: https://www.vinhosevinhos.com/#&search-term=vinhos", font=('Ivy 10 bold'))
    site.grid(column=1, row=1, padx=1, pady=10)

    dados_tabela()

    janela.mainloop()