#bibliotecas 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

lista_compras=[]

principal='https://lista.mercadolivre.com.br/'

busca=input('Qual será a pesquisa de hoje?: ')
#print(principal+busca)

resposta= requests.get(principal+busca)

ml=BeautifulSoup(resposta.text, 'html.parser')

produtos=  ml.findAll( 'div', attrs= {'class':"andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"})

print(produtos)