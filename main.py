import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 


busca=input('Qual será a pesquisa de hoje?: ')

for limit in range(1, 152, 51):

    lista_compras=[]

    principal='https://lista.mercadolivre.com.br/'

    #print(principal+busca)

    resposta= requests.get(principal+busca+'_Desde_{}_NoIndex_True'.format(limit) )

print()