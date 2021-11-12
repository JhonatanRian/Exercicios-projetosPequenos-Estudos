from typing import List
from requests_html import HTMLSession
from unidecode import unidecode
from bs4 import BeautifulSoup
from time import sleep

def times(pais: str, serie: str) -> List:
    lista: list = []
    if serie.lower() == "1":
        url = f"https://www.soccerstats.com/latest.asp?league={unidecode(pais).lower()}{serie}"
        session = HTMLSession()
        resposta = session.get(url)
        resposta.html.render(sleep=3)
        html = resposta.html.html
        soup = BeautifulSoup(html, "html.parser")
        sear = soup.find_all("table")
        for i in range(len(sear)):
            if i == 4:
                times: BeautifulSoup = sear[i]
                time = times.find_all("a")
                for i in range(len(time)):
                    if i > 49:
                        lista.append(time[i].text)
                return lista
    
def time(pais, n_pais: str = None, time: str = None):
    url = f"https://www.soccerstats.com/team.asp?league={unidecode(pais).lower()}{n_pais}&stats=8-{unidecode(time).lower()}" 
    
    