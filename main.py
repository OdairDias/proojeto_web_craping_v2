from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from enum import Enum

from bs4 import BeautifulSoup
import requests


busca=input('Qual será a pesquisa de hoje?: ')
principal='https://lista.mercadolivre.com.br/'

resposta=(principal+busca)
navegador= webdriver.Firefox()
navegador.get(resposta)

