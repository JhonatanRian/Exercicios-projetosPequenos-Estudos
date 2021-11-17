from requests_html import HTMLSession

url_competicoes = 'https://pt.soccerstats247.com/competi%C3%A7%C3%B5es/'

#soccerContentPlaceHolder_domesticCompetitions
session = HTMLSession()
r = session.get(url_competicoes)
texto = r.html
elens = texto.find('[@id="soccerContentPlaceHolder_domesticCompetitions"] div')
for el in elens:
    try:
        if el.attrs['class'][0] == 'panel-title':
            pais = el.attrs['class'][0]
        elif el.attrs['class'][0] == 'panel-body':
            print(el.text)
    except:
        ...