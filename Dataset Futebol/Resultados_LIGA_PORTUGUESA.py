from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

with sync_playwright() as p:

    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.flashscore.com/football/portugal/liga-portugal/results/")

    page.wait_for_timeout(3000)

    html = page.content()

'''with open ('LIGAPORTUGALRESULTADOS.html', 'w', encoding = 'utf-8') as f:
    f.write(html)


with open('LIGAPORTUGALRESULTADOS.html', 'r', encoding = 'utf-8') as f:
    ficheiro = f.read()'''
    

soup = BeautifulSoup(html, 'html.parser')

clubes = ['Rio Ave', 'Braga', 'Santa Clara', 'Estrela', 'Alverca', 'Benfica', 'Tondela', 'Estoril', 'Sporting CP',
'FC Porto', 'AFS', 'Famalicao', 'Vitoria Guimaraes', 'Arouca', 'Casa Pia', 'Nacional', 'Gil Vicente', 'Moreirense']

hum = soup.find_all('div', attrs = {'id': re.compile('^g_1_')})

for jogos in hum:    
    resultados = jogos.get_text(strip = True).replace(" ", "").lower() #STRIP extrai o texto sem espaços no inicio e no fim #REPLACE remove todos os espaços do texto " " substitui para ""
    #print(resultados)
    
    
    equipas = []

    for clube in clubes:
        nome_clubes = clube.replace(" ", "").lower()
        if nome_clubes in resultados:
            (equipas.append((resultados.find(nome_clubes), clube)))
            

    if len (equipas) == 2:
        equipas.sort()
        equipa_casa = equipas[0][1]
        equipa_fora = equipas [1][1]

        resultado = re.search(r'(\d{1,2})(\d{1,2})$', resultados) #(\d{1,2}) encontra o primeiro número a contar do fim $
        if resultado:

            golos1, golos2 = resultado.groups() #cria uma tupla ou seja separa cada número golos1 = (\d{1,2}) e golos2 = (\d{1,2})
            
            print(f'{equipa_casa} vs {equipa_fora} : {golos1} - {golos2}')
    

    
   
    '''if len(equipas) == 2:
        #print (equipas)
        
        final = re.search(r'(\d)(\d)$', resultados)
        if final:
            golos1, golos2 = final.groups()
            print(f'{equipas[0]} vs {equipas[1]} : {golos1} - {golos2}')'''




    '''equipas = [clube for clube in clubes if clube.replace(" ", "").lower() in resultados.lower()]
    print (equipas)
    #final = re.search(r"(\d)(\d)$", resultados)
    
    if len (equipas) == 1:
        equipa_casa = equipas[0]
        equipas_fora = equipas[1]

        #print (f'{equipa_casa} vs {equipas_fora}')
        #golos1, golos2 = (final.groups())
        #equipa_casa = equipas[0]
        #equipa_fora = equipas[1]

    #    print (f'{equipa_casa} vs {equipa_fora} : {golos1} - {golos2}')'''


      