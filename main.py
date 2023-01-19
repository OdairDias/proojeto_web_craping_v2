#bibliotecas 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

lista_compras=[]

principal='https://lista.mercadolivre.com.br/'

busca=input('Qual será a pesquisa de hoje?: ')
#print(principal+busca)


num_loop = int(input('Digite o número de Páginas: '))



#aqui estamos limitando o número de paginas a no máximo 11 
# caso queira mais paginas basta acrescentar a aprtir da 551 sempre de 50, a baixo a próxima seria por exemplo a 601 

pages_increment = ['0','51','101']

for x in range(0,num_loop):

    resposta= requests.get(principal+busca+'_Desde_'+pages_increment[x]+'_DisplayType_LF')

    ml=BeautifulSoup(resposta.text, 'html.parser')

    produtos=  ml.findAll( 'div', attrs= {'class':"andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"})

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
# print(ml.ar prettify())
    #print("Nome do Produto: ",nome_produto.text) 
    #print('link do produto:',link_produto['href'])
    #if (preço_produtocentavos):
        #print('Preço do produto: R$',preço_produtoreal.text  + ',' + preço_produtocentavos.text)
    #else:
       #print('Preço do produto: R$',preço_produtoreal.text) 
    #print('\n\n')


pesquisa=pd.DataFrame(lista_compras,columns=['Produto','Preço produto','Link produto'])
print(pesquisa)

#pesquisa.to_excel('resultado_pesquisa.xlsx', index=False)