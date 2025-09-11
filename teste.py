from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import random
import re
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

from google.oauth2.service_account import Credentials












data_jogos = []
equipa_casa = []
equipa_fora = []
golos_casa = []
golos_fora = []

estatísticas_finais = []



def MAIN(href, page):

   
        '--------------------------------------------------------------------------------WEB-SCRAPING-RESULTADOS-----------------------------------------------------------------------------------'

        page.goto(href)
        page.wait_for_timeout(random.uniform(1500, 3000))

        html = page.content()

        soup = BeautifulSoup(html, 'html.parser')

    
        data = soup.find(class_ = 'duelParticipant__startTime').get_text(strip = True)
        data_jogos.append(data)

        casa = soup.find('div', attrs = {'class': 'duelParticipant__home'}).get_text(strip = True)
        equipa_casa.append(casa)

        fora = soup.find('div', attrs = {'class': 'duelParticipant__away'}).get_text(strip = True)
        equipa_fora.append(fora)

        golos = soup.find(class_ = 'detailScore__wrapper')
        if golos:
            span = golos.find_all('span')
            if len(span) >= 2:
                golos_1 = span[0].get_text(strip = True)
                golos_casa.append(golos_1)
                golos_2 = span[2].get_text(strip = True)
                golos_fora.append(golos_2)

        


        '--------------------------------------------------------------------------------WEB-SCRAPING-ESTATÍSTICAS-----------------------------------------------------------------------------------'

        estatísticas_aba = soup.find('a', attrs = {'data-analytics-alias': 'match-statistics'})
        sumário = estatísticas_aba.get('href')
        link = f'https://www.flashscore.pt{sumário}'

        page.goto(link)
        page.wait_for_timeout(random.uniform(2000, 3000))

        html_2 = page.content()

        soup = BeautifulSoup(html_2, 'html.parser')

        estatísticas_dicionário = {}

        sections = soup.find_all('div', class_ = 'section')

        for sec in sections:
    
            texto = sec.find('div', class_ = 'sectionHeader')

            estatísticas = sec.find_all('div', attrs = {'class': "wcl-row_2oCpS"})
            for nomes in estatísticas:
                final = nomes.text
                lista = final.split('\n')
            #print (lista)
                hum = re.sub(r"\([^)]*\)", "", final)
                match = re.match(r'^([\d%./+-]+)\s*([^\d%./+-]+)\s*([\d%./+-]+)$', hum)

                if match:
                    numero_inicio, texto, numero_fim = match.groups()
                    if texto.strip() not in estatísticas_dicionário:
                        estatísticas_dicionário[texto.strip()] = f'{numero_inicio} -  {numero_fim}'
                        print (f'{texto.strip()} : {numero_inicio} -  {numero_fim}')
                        #print(estatísticas_dicionário)
                        estatísticas_finais.append({'casa': numero_inicio, 'fora': numero_fim})
        

            
        
'--------------------------------------------------------------------------------MAIN-------------------------------------------------------------------------------------------------'

'''with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://www.flashscore.pt/futebol/portugal/liga-portugal-betclic/resultados/")
    page.wait_for_timeout(random.uniform(3000, 7000))
    html_resultados = page.content()
    soup_resultados = BeautifulSoup(html_resultados, 'html.parser')



    hum = soup_resultados.find(id = 'live-table')

    ok = hum.find_all('a')

    teste = random.choice(ok)
    
   
    href = teste.get('href')
    if href and 'https://www.flashscore.pt/jogo/futebol' in href:
        MAIN(href = href, page = page)'''
    

scopes = [
    'https://www.googleapis.com/auth/spreadsheets'
]

credenciais = Credentials.from_service_account_file('credentials.json', scopes = scopes)
aut = gspread.authorize(credenciais)
key = aut.open_by_key('1nJERI9CLGEzQR6YlAprIzVrzq01IeMB4VQUCKDgQQRg')

EXCEL = key.get_worksheet()

print (EXCEL)



#print (estatísticas_finais)


