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
            estatísticas_finais.append({data})
            estatísticas_finais.append({casa})
            estatísticas_finais.append({fora})
            estatísticas_finais.append({golos_1})
            estatísticas_finais.append({golos_2})

                
        


        '--------------------------------------------------------------------------------WEB-SCRAPING-ESTATÍSTICAS-----------------------------------------------------------------------------------'

        estatísticas_aba = soup.find('a', attrs = {'data-analytics-alias': 'match-statistics'})
        sumário = estatísticas_aba.get('href')
        link = f'https://www.flashscore.pt{sumário}'''

        with sync_playwright() as p:
            browser = p.chromium.launch(headless = False)
            context = browser.new_context()
            page = context.new_page()





            page.goto(link)
            page.wait_for_timeout(random.uniform(2000, 3000))

            html_2 = page.content()

            soup = BeautifulSoup(html_2, 'html.parser')

            sections = soup.find_all('div', class_ = 'section')
    
            dict = {}

            ignore = ['Cartões vermelhos', 'Golos de cabeça']

            for sec in sections:
    
                estatísticas = sec.find_all('div', attrs = {'class': "wcl-row_2oCpS"})



                for nomes in estatísticas:
                    final = nomes.text
            #print (final)
                    if any(item in final for item in ignore):
                        continue  
              
                    hum = re.sub(r"\([^)]*\)", "", final)
                    match = re.match(r'^([\d%./+-]+)\s*([^\d%./+-]+)\s*([\d%./+-]+)$', hum)
            
                    if match:
                        numero_inicio, texto, numero_fim = match.groups()
                        if texto.strip() not in dict:
                            dict[texto.strip()] = f'{numero_inicio} : {numero_fim}'
                            estatísticas_finais.append(numero_inicio)
                            estatísticas_finais.append(numero_fim)

   
                        
            
        
'--------------------------------------------------------------------------------MAIN-------------------------------------------------------------------------------------------------'

scopes = [
    'https://www.googleapis.com/auth/spreadsheets'
]

credenciais = Credentials.from_service_account_file('credentials.json', scopes = scopes)
aut = gspread.authorize(credenciais)
key = aut.open_by_key('1nJERI9CLGEzQR6YlAprIzVrzq01IeMB4VQUCKDgQQRg')

EXCEL = key.get_worksheet(0)

df = get_as_dataframe(EXCEL)


colunas = (len(df.columns)) + 2
print (len(df.columns))
print (colunas)
#print (df.columns)



with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://www.flashscore.pt/futebol/portugal/liga-portugal-betclic/resultados/")
    page.wait_for_timeout(random.uniform(3000, 7000))
    html_resultados = page.content()
    soup_resultados = BeautifulSoup(html_resultados, 'html.parser')



    hum = soup_resultados.find(id = 'live-table')

    ok = hum.find_all('a')

    hum = random.sample(ok, 2)

    for links in hum:
        href = links.get('href')
        if href and 'https://www.flashscore.pt/jogo/futebol' in href:
            MAIN(href = href, page = page)
            

if len(estatísticas_finais) == len(df.columns):
    df.loc[len(df)] = estatísticas_finais

else:
    df.fillna(0, inplace = True)



print (df)




#df.loc[(len(df.columns))] = estatísticas_finais
#print (df)



#print (estatísticas_finais)


#df.loc[comprimento] = estatísticas_finais



#linhas = len(df)
#print (linhas)

df_novo = pd.DataFrame ({
                'DATE': data_jogos, 
                'HOME_TEAM': equipa_casa, 
                'AWAY_TEAM': equipa_fora, 
                'HOME_GOALS': golos_casa,
                'AWAY_GOALS': golos_fora
                })

df = pd.concat([df, df_novo], ignore_index = True)

print (estatísticas_finais)


comprimento = (len(df.columns))

df.loc[comprimento] = estatísticas_finais'''

#print (df)





