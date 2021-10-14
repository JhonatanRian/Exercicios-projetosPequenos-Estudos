"""
    script para automatizar o trabalho de indentificar todas os municipios de um estado
"""

from os import write
import requests
from bs4 import BeautifulSoup

response = requests.get("https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_S%C3%A3o_Paulo_por_popula%C3%A7%C3%A3o")

soup = BeautifulSoup(response.text, "html.parser")

info = soup.find_all("td")

lista = []
with open("arquivo2.txt", "w") as arq:
    for i in info:
        info2 = i.find_next("a")
        if info2.text not in lista:
            arq.write(info2.text)
            arq.write("\n")
            lista.append(info2.text)
    

