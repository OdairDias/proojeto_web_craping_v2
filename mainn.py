#importamos a library do excel.
import pandas as pd
import requests
from selenium import webdriver
#definir tamanho da tela
from selenium.webdriver.firefox.options import Options
options= Options()
options.add_argument('window=size=600,600')
import time
from bs4 import BeautifulSoup

lista_compras=[]

busca=input('Qual será a pesquisa de hoje?: ')
principal='https://lista.mercadolivre.com.br/'

resposta=(principal+busca)
navegador= webdriver.Firefox(options=options)
time.sleep(3)
navegador.get(resposta)

time.sleep(3)
#tranformar variavel utilizando Beautifulsoup
page_content=navegador.page_source

ml=BeautifulSoup(page_content, 'html.parser')
time.sleep(8)
#print(ml.prettify())

produtos=  ml.findAll( 'div', attrs= {'class':'ui-search-result__content-wrapper shops__result-content-wrapper'})

for produto in produtos:

    nome_produto=produto.find('h2', attrs={'class':'ui-search-item__title'})

    link_produto=produto.find('a', attrs={'class':'ui-search-link'})
    
    preço_produtoreal= produto.find('span', attrs={'class':'price-tag-fraction'})
    
    preço_produtocentavos= produto.find('span', attrs={'class':'price-tag-cents'})
    
    if (preço_produtocentavos):
        preçototal=(preço_produtoreal.text  + ',' + preço_produtocentavos.text)
    else:
        preçototal=(preço_produtoreal.text) 


    if(preço_produtocentavos):

        lista_compras.append([nome_produto.text,preçototal,link_produto['href']])
    else:
        lista_compras.append([nome_produto.text,preço_produtoreal.text,link_produto['href']])
    time.sleep(1)

pesquisa=pd.DataFrame(lista_compras,columns=['Produto','Preço produto','Link produto'])
print(pesquisa)
