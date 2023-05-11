from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import *
import time
import re

#importando CRUD
from CRUD import *

    # Execução de um comando: SELECT ... CREATE
def imprimir_prod():
    
    mostrar_dados()

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
        
    print(descrivinho)
    print(precovinho)
        
    driver.quit()

def busca_produto():

    janela = Tk()
    janela.title("Vinicula Web - Monitoramento de Produtos ")
    janela.geometry("500x300")

    inserir = Button(janela, text="Cadastro Produto", border=None)
    inserir.grid(column=6, row=0, padx=10, pady=10)

    botao = Button(janela, text= "buscar produto Web", command=requisicao) 
    botao.grid(column=1, row=1, padx=10, pady=10)

    imprimir = Button(janela, text= "imprimir produtos", command=imprimir_prod) 
    imprimir.grid(column=2, row=1, padx=10, pady=10)

    janela.mainloop()    
