#importamos a library do excel.
import requests
from selenium import webdriver
#definir tamanho da tela
from selenium.webdriver.chrome.options import Options
options= Options()
options.add_argument('window=size=600,600')
import time
from bs4 import BeautifulSoup

lista_compras=[]

busca=input('Qual será a pesquisa de hoje?: ')
principal='https://lista.mercadolivre.com.br/'

resposta=(principal+busca)
navegador= webdriver.Chrome(options=options)
time.sleep(3)
navegador.get(resposta)
time.sleep(30)
produtos=  navegador.find_element( 'div', attrs= {'class':"andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"})

