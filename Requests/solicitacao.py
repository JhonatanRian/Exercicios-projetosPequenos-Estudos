"""import requests

url = "https://www.google.com"
response = requests.get(url)
print(response)

try:
    r = requests.get("https://google.com", timeout=0.01)
except requests.Timeout:
    print("Erro timeout")
    
#  Sempre configurar definir headers
he = {"user-agentt":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}


a = requests.get("https://google.com.br", headers=he)
print(a.status_code)

lista =[
    (10000, 50000),
    (10000, 50000),
    (10000, 50000),
    (10000, 50000),
    (10000, 50000)
]

def itera(valor):
    x = [x**valor[0] for x in range(1, valor[0])]
    y = [x**valor[1] for x in range(1, valor[1])]
    v = [x^1000000, y^1000000]
    
    return v

li = []
for item in lista:
    print("Calculando ...")
    r = threading.Thread(target=itera, args=(item,)).start()
    li.append(r)

"""
import requests

# download de imagem
req = requests.get("https://img.sportradar.com/ls/crest/medium/en.png")

imagem = open("Imagem.jpg", "bw") #ABRE EM MODO BINARIO E ESCRITA

imagem.write(req.content)  #CONTENT RETORNA EM BINARIO DIFERENTE DO TEXT

imagem.close()

