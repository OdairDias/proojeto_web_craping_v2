import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

lista_compras=[]

principal='https://lista.mercadolivre.com.br/'

busca=input('Qual será a pesquisa de hoje?: ')
#print(principal+busca)

resposta= requests.get(principal+busca)

ml=BeautifulSoup(resposta.text, 'html.parser')


pagina = 1
while True:
    resposta = requests.get(principal+busca+'&page='+str(pagina))
    ml = BeautifulSoup(resposta.text, 'html.parser')
    produtos =  ml.findAll( 'div', attrs= {'class':"andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"})
    for produto in produtos:
        nome_produto=produto.find('h2', attrs={'class':'ui-search-item__title'})
        link_produto=produto.find('a', attrs={'class':'ui-search-link'})
        preço_produtoreal= produto.find('span', attrs={'class':'price-tag-fraction'})
        preço_produtocentavos= produto.find('span', attrs={'class':'price-tag-cents'})
        if (preço_produtocentavos):
            preçototal=(preço_produtoreal.text  + ',' + preço_produtocentavos.text)
        else:
            preçototal=(preço_produtoreal.text) 
        lista_compras.append([nome_produto.text,preçototal,link_produto['href']])
    proxima_pagina = ml.find('a', attrs={'class':'andes-pagination__link andes-pagination__link--next'})
    if proxima_pagina:
        pagina += 1
    else:
        break
    time.sleep(3)
pesquisa=pd.DataFrame(lista_compras,columns=['Produto','Preço produto','Link produto'])
pesquisa.to_excel('resultado_pesquisa.xlsx', index=False)