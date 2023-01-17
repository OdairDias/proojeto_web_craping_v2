from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from enum import Enum

from bs4 import BeautifulSoup
import requests

lista_compras=[]

busca=input('Qual será a pesquisa de hoje?: ')
principal='https://lista.mercadolivre.com.br/'

resposta=(principal+busca)
navegador= webdriver.Firefox()
navegador.get(resposta)

time.sleep(8)
produtos=  navegador.find_element_by_name( <div class="ui-search-result__content-wrapper shops__result-content-wrapper"><div class="ui-search-item__group ui-search-item__group--title shops__items-group"><span class="ui-search-item__brand-discoverability ui-search-item__group__element shops__items-group-details">TOPPER</span><h2 class="ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title">Tenis Futsal Masculino Chuteira Futebol Quadra Topper Salão</h2></div><div class="ui-search-item__group ui-search-item__group--price shops__items-group"><div class="ui-search-item__group__element ui-search-price__part-without-link shops__items-group-details"><div class="ui-search-price ui-search-price--size-medium shops__price"><s class="price-tag ui-search-price__part ui-search-price__original-value shops__price-part price-tag__disabled"><span class="price-tag-text-sr-only">Antes: 159 reais con 99 centavos </span><span class="price-tag-amount" aria-hidden="true"><span class="price-tag-symbol">R$</span><span class="price-tag-fraction">159</span><span class="price-tag-decimal-separator">,</span><span class="price-tag-cents">99</span></span></s><div class="ui-search-price__second-line shops__price-second-line"><span class="price-tag ui-search-price__part shops__price-part"><span class="price-tag-text-sr-only">143 reais con 99 centavos </span><span class="price-tag-amount" aria-hidden="true"><span class="price-tag-symbol">R$</span><span class="price-tag-fraction">143</span><span class="price-tag-decimal-separator">,</span><span class="price-tag-cents">99</span></span></span><span class="ui-search-price__second-line__label shops__price-second-line__label"><span class="ui-search-price__discount shops__price-discount">10% OFF</span></span></div></div></div><span class="ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--LIGHT_GREEN"><div class="ui-search-installments-prefix"><span>em</span></div>4x <div class="ui-search-price ui-search-price--size-x-tiny ui-search-color--LIGHT_GREEN shops__price"><div class="ui-search-price__second-line shops__price-second-line"><span class="price-tag ui-search-price__part shops__price-part"><span class="price-tag-text-sr-only">36 reais</span><span class="price-tag-amount" aria-hidden="true"><span class="price-tag-symbol">R$</span><span class="price-tag-fraction">36</span></span></span></div></div>sem juros</span></div><div class="ui-search-item__group ui-search-item__group--shipping shops__items-group"><div class="ui-search-item__group__element ui-search-item__group__element--shipping shops__items-group-details"><p class="ui-search-item__shipping ui-search-item__shipping--free shops__item-shipping-free">Frete grátis</p></div></div></div>)


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