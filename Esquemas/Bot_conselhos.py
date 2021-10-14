from csv import writer
from sele import *

cidades: list = []
not_found: list = []


while True:
    try:
        with open("arquivo2.txt", "r") as arquivo:
            cidades = (arquivo.readlines())

        with open("document.csv", "a+") as file:
            w_now = writer(file)
            w_now.writerow(["CNPJ", "Razão Social", "Data da Abertura", "E-mail", "Telefone(s)", "Município", "Estado"])
        for cidade in cidades:
            caminhos = get_paths(cidade)
            if caminhos:
                for c in caminhos:
                    data = capture_data(c)
                    from_salve = to_capture_data(data)
                    write_doc(from_salve)
            else:
                if not_found.count(cidade) > 2:
                    break
                not_found.append(cidade)
    except:
        print("false")