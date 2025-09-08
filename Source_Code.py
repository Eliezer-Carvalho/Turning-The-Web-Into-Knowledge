from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import random
import re






def RESULTADOS(soup):

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
                return equipa_casa, equipa_fora, golos1, golos2

    

def ESTATÍSTICAS(soup):


    estatísticas_finais = []

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
                estatísticas_finais.append((texto.strip(), numero_inicio, numero_fim))        
                
    return estatísticas_finais
            

#------------------------------------------------------------------------------MAIN---------------------------------------------------------------------------------



with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://www.flashscore.pt/futebol/portugal/liga-portugal-betclic/resultados/")
    page.wait_for_timeout(random.uniform(3000, 7000))
    html_resultados = page.content()
    soup_resultados = BeautifulSoup(html_resultados, 'html.parser')


    clubes = ['Rio Ave', 'Braga', 'Santa Clara', 'Estrela', 'Alverca', 'Benfica', 'Tondela', 'Estoril', 'Sporting CP',
    'FC Porto', 'AFS', 'Famalicao', 'Vitoria Guimaraes', 'Arouca', 'Casa Pia', 'Nacional', 'Gil Vicente', 'Moreirense']

    soup = BeautifulSoup(soup_resultados, 'html.parser')

    hum = soup.find(id = 'live-table')

    ok = hum.find_all('a')


    for links in ok:
        href = links.get('href')
        if href and 'https://www.flashscore.pt/jogo/' in href:

            page.goto(href)
            page.click("[data-testid='wcl-tab']:has-text('Estatísticas')")
            page.wait_for_timeout(random.uniform(2000, 2800))
            html_estatísticas = page.content()
            soup_estatísticas = BeautifulSoup(html_estatísticas, 'html.parser')

            resultados_finais = RESULTADOS(soup_resultados)
            estatísticas_finais = ESTATÍSTICAS(soup_estatísticas)
            if resultados_finais and estatísticas_finais:
                equipa_casa, equipa_fora, golos1, golos2 = resultados_finais
                 
                print (f"{equipa_casa} vs {equipa_fora} : {golos1} - {golos2}")
                print ("\n Estatísticas do jogo: \n")

                for texto, numero_inicio, numero_fim in estatísticas_finais:
                    print (f'{texto} --> {numero_inicio} : {numero_fim} ')
                       
            
        


    
