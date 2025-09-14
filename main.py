from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import random
import re
import pandas as pd
from datetime import datetime





def MAIN(href, page):

   
    '--------------------------------------------------------------------------------WEB-SCRAPING-RESULTADOS-----------------------------------------------------------------------------------'

    estatísticas_finais = []

    page.goto(href)
    page.wait_for_timeout(random.uniform(1500, 3000))

    html = page.content()

    soup = BeautifulSoup(html, 'html.parser')

    
    data = soup.find(class_ = 'duelParticipant__startTime').get_text(strip = True)

    data_dt = datetime.strptime(data, "%d.%m.%Y %H:%M")
    data_formatada = data_dt.strftime("%d-%m-%Y")  
    estatísticas_finais.append(data_formatada)


    casa = soup.find('div', attrs = {'class': 'duelParticipant__home'}).get_text(strip = True)
    estatísticas_finais.append(casa)

    fora = soup.find('div', attrs = {'class': 'duelParticipant__away'}).get_text(strip = True)
    estatísticas_finais.append(fora)

    golos = soup.find(class_ = 'detailScore__wrapper')
    if golos:
        span = golos.find_all('span')
        if len(span) >= 2:
            golos_1 = span[0].get_text(strip = True)
            estatísticas_finais.append(golos_1)
            golos_2 = span[2].get_text(strip = True)
            estatísticas_finais.append(golos_2)
            

                
        


        '--------------------------------------------------------------------------------WEB-SCRAPING-ESTATÍSTICAS-----------------------------------------------------------------------------------'

    estatísticas_aba = soup.find('a', attrs = {'data-analytics-alias': 'match-statistics'})
    sumário = estatísticas_aba.get('href')
    
    link = f''
    
   
    page.wait_for_timeout(random.uniform(1500, 3000))
    page.goto(link)
    page.wait_for_timeout(random.uniform(1500, 3000))

    html_2 = page.content()

    soup = BeautifulSoup(html_2, 'html.parser')

    sections = soup.find_all('div', class_ = 'section')
    
    dict = {}

    ignore = ['Cartões vermelhos', 'Golos de cabeça', 'Cartões amarelos']

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
                    if dict:
                        estatísticas_finais.append(numero_inicio)
                        estatísticas_finais.append(numero_fim)

    return estatísticas_finais
                   

   
                        
            
        
'--------------------------------------------------------------------------------MAIN-------------------------------------------------------------------------------------------------'



df = pd.read_csv('')   #CSV


with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("")  #LINK
    page.wait_for_timeout(random.uniform(3000, 7000))

    while True:
        botão_mais_jogos = page.locator('text = Mostrar mais jogos')
        if botão_mais_jogos.count() == 0:
            break

        botão_mais_jogos.click()
        page.wait_for_timeout(random.uniform(1500, 3000))

    
    html_resultados = page.content()
    soup_resultados = BeautifulSoup(html_resultados, 'html.parser')



    hum = soup_resultados.find(id = 'live-table')

    ok = hum.find_all('a')
    


    for links in ok:
        href = links.get('href')
        if href and '' in href:       
            ESTAT = MAIN(href = href, page = page)
            df.loc[len(df)] = ESTAT
        

df.to_csv('', index = False)  #CSV
