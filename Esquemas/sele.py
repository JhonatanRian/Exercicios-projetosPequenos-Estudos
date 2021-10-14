from csv import writer
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
to_like = ( "CNPJ", 
            "Razão Social", 
            "Data da Abertura", 
            "E-mail", 
            "Telefone(s)", 
            "Município", 
            "Estado")

PROXY = "51.68.207.814:443"
web_op = webdriver.FirefoxOptions()
web_op.add_argument(f'--proxy-server={PROXY}')

def gera_cnpj(data: list) -> str:
    """
    Retorna uma string sem caracter; 
    usada no "get_paths"
    """
    cnpj = data[1]
    resulte: str = "".join(c for c in cnpj if c.isalnum())
    return resulte

def get_paths(cidade: str) -> list:
    """
    Retorna os cpfs achados na pesquisa para depois usar como caminho no requests
    """
    url: str = "https://cnpj.biz/procura/conselho de pastores "
    end: list = list() # lista que será retornada
    with webdriver.Firefox(options=web_op) as driver:
        driver.get(url+cidade)
        elemen: webdriver = driver.find_elements_by_tag_name("a")
        
        for element in elemen:
            text_tag: str = ((element.text).split())
            if text_tag[0] == "CNPJ:":
                path: str = gera_cnpj(text_tag)
                end.append(path)
    return end

def to_capture_data(data: list) -> dict:
    for_del: list = []
    info: dict = {}
    for i in data:
        var = (i.split(":"))
        if len(var) > 1:
            info[var[0]] = var[1]
    for k in info.keys():
        if k in to_like:
            ...
        else:
            for_del.append(k)
    for i in for_del:
        del info[i]
    return info
            
def capture_data(path: str):
    '''
    Faz uma requisição da pagina com o caminho(cnpj);
    path é o cnpj da cidade;
    - Testado e sem erro.
    ''' 
    url = "https://cnpj.biz/" + path
    dados = []
    response = requests.get(url, headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"})
    soup = BeautifulSoup(response.text, "html.parser")
    info = soup.find_all("p")
    for i in info:
        dados.append((i.text))
    return dados

def write_doc(data: dict) -> None:
    doc: list = []
    with open("document.csv", "a+") as file:
        write_csv = writer(file)
        for k in data.keys():
            doc.append(data[k])
        write_csv.writerow(doc)

if __name__ == "__main__":
    # test =get_paths("São Paulo")
    test2 = capture_data("09319513000134")
    test3 = to_capture_data(test2)
    write_doc(test3)