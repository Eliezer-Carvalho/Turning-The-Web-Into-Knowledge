from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import random
import re
import requests


def MAIN():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        contexto = browser.new_context()
        page = contexto.new_page()
        #page_2 = contexto.new_page()

        '--------------------------------------------------------------------------------WEB-SCRAPING-RESULTADOS-----------------------------------------------------------------------------------'



        page.goto('https://www.flashscore.pt/jogo/futebol/fc-porto-S2NmScGp/gil-vicente-CS0fFFd8/?mid=hKpskA9E')
        page.wait_for_timeout(random.uniform(1500, 3000))

        html = page.content()

        soup = BeautifulSoup(html, 'html.parser')

    
        data = soup.find(class_ = 'duelParticipant__startTime').get_text(strip = True)


        equipa_casa = soup.find(class_ = 'duelParticipant__home').get_text(strip = True)

        equipa_fora = soup.find(class_ = 'duelParticipant__away duelParticipant--winner').get_text(strip = True)

        golos = soup.find(class_ = 'detailScore__wrapper')
        if golos:
            span = golos.find_all('span')
            if len(span) >= 2:
                golos_casa = span[0].get_text(strip = True)
                golos_fora = span[2].get_text(strip = True)


        estatísticas_aba = soup.find('a', attrs = {'data-analytics-alias': 'match-statistics'})
        sumário = estatísticas_aba.get('href')
        link = f'https://www.flashscore.pt{sumário}'

       
       
        hum = requests.get(link)
        #print (hum.text

        soup = BeautifulSoup(hum.text, 'html.parser')
        















































'''page_2.goto(link)

        page_2.wait_for_timeout(random.uniform(1500, 3000))


        page_2.click("[data-testid='wcl-tab']:has-text('Estatísticas')")

        page_2.wait_for_timeout(random.uniform(1500, 3000))

    

    soup_estatísticas = BeautifulSoup(hum.text, 'html.parser')


    sections = soup_estatísticas.find_all('div', class_ = 'section')

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
                print (texto.strip(), numero_inicio, numero_fim)'''
            
    














'''with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    contexto = browser.new_context()
    page = contexto.new_page()


    page.goto("https://www.flashscore.pt/futebol/portugal/liga-portugal-betclic/resultados/")
    page.wait_for_timeout(random.uniform(3000, 7000))
    html_resultados = page.content()
    soup_resultados = BeautifulSoup(html_resultados, 'html.parser')


    clubes = ['Rio Ave', 'Braga', 'Santa Clara', 'Estrela', 'Alverca', 'Benfica', 'Tondela', 'Estoril', 'Sporting CP',
    'FC Porto', 'AFS', 'Famalicao', 'Vitoria Guimaraes', 'Arouca', 'Casa Pia', 'Nacional', 'Gil Vicente', 'Moreirense']

    

    hum = soup_resultados.find(id = 'live-table')

    ok = hum.find_all('a')

    
    random_teste = random.choice(ok)
    href = random_teste.get('href')
    page.goto(href)
    page.wait_for_timeout(random.uniform(1000, 2500))
    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')
    RESULTADOS(soup)











        #if href and 'https://www.flashscore.pt/jogo/futebol' in href:'''
            