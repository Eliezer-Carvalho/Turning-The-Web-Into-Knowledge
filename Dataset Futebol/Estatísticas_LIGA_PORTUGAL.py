from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import random
import re


'''with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.flashscore.pt/jogo/futebol/l8XU4D5T/#/sumario-do-jogo/sumario-do-jogo')

    page.wait_for_timeout(random.uniform(3000, 10000))

    page.click("button:has-text('ESTATÍSTICAS')")


    page.wait_for_timeout(random.uniform(3000, 10000))

    html = page.content()

    with open ('LIGAPORTUGALESTATÍSTICAS.html', 'w', encoding = 'utf-8') as f:
        f.write(html)'''


with open ('LIGAPORTUGALESTATÍSTICAS.html', 'r', encoding = 'utf-8') as f:
    ficheiro = f.read()


soup = BeautifulSoup(ficheiro, 'html.parser')

sections = soup.find_all('div', class_ = 'section')

for sec in sections:
    
    texto = sec.find('div', class_ = 'sectionHeader')
    if texto:
        print('\n')
              
    data = []

    estatísticas = sec.find_all('div', attrs = {'class': "wcl-row_2oCpS"})
    for nomes in estatísticas:
        final = nomes.text
        lista = final.split('\n')
        #print (lista)
        hum = re.sub(r"\([^)]*\)", "", final)
        match = re.match(r'^([\d%./+-]+)\s*([^\d%./+-]+)\s*([\d%./+-]+)$', hum)

        if match:
            numero_inicio, texto, numero_fim = match.groups()
            print(f"{texto.strip()} --> {numero_inicio} : {numero_fim}")
            
    


        