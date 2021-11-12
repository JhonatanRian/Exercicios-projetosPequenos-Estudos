from requests_html import HTMLSession
import json
import base64


class AtenaSS:
    
    def __init__(self: object, pais: str, time: str) -> None:
        self.__url: str = f"https://pt.soccerstats247.com/equipas/{pais}/{time}/"
        self.__secao: HTMLSession = HTMLSession()
        self.__resposta = self.__secao.get(self.__url)
        self._html: HTMLSession = self.__resposta.html
        self.__nome_time: str = self._html.find('h1')[0].text
        self.__elementos_estatistica: HTMLSession = self._html.find("div[id='statisticsSlider'] tr")
        self.__bandeira: HTMLSession = self._html.find("#soccerContentPlaceHolder_imgTeamLogo")
        self.__elementos_gols: HTMLSession = self._html.find("#scoringMinutesSlider tr")
        self.__campeonatos: HTMLSession = self._html.find("#tabHeaders a")
        self.__jogadores: HTMLSession = self._html.find("#squadSlider tr")
        self.__estatistica: dict = self._estatistica()
        self.__minutos_gols: dict = self._min_gol()
        self.__partidas: dict = self._partidas()
        self.__equipe: dict = self._equipe()
        
    @property
    def nome_time(self:object) -> None:
        return self.__nome_time    
    
    @property
    def estatistica(self: object) -> dict:
        return self.__estatistica
    
    @property
    def min_gols(self: object) -> dict:
        return self.__minutos_gols
        
    @property
    def partidas(self: object) -> dict:
        return self.__partidas
    
    @property
    def equipe(self: object) -> dict:
        return self.__equipe
    
    def _estatistica(self: object) -> dict:
        elementos: HTMLSession = self.__elementos_estatistica
        dados: list = self.capturar(elementos)
        data = {}
        try:
            data[dados[0][0].split(',')[0]] = dados[0][0].split(',')[1]
        except:
            data[''] = ''
        try:
            data['Classificação'] = {'total': dados[1][1]}
        except:
            data['Classificação'] = {'total': ''}
        try:
            data['Partidas jogadas'] = {'total':dados[2][1], 'Em casa':dados[2][2], 'fora':dados[2][3]}
        except:
            data['Partidas jogadas'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Vitórias'] = {'total':dados[3][1], 'Em casa':dados[3][2], 'fora':dados[3][3]}
        except:
            data['Vitórias'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Empate'] = {'total':dados[4][1], 'Em casa':dados[4][2], 'fora':dados[4][3]}
        except:
            data['Empate'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Derrota'] = {'total':dados[5][1], 'Em casa':dados[5][2], 'fora':dados[5][3]}
        except:
            data['Derrota'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Gols marcados'] = {'total':dados[6][1], 'Em casa':dados[6][2], 'fora':dados[6][3]}
        except:
            data['Gols marcados'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Gols sofridos'] = {'total':dados[7][1], 'Em casa':dados[7][2], 'fora':dados[7][3]}
        except:
            data['Gols sofridos'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['pontos'] = {'total':dados[8][1], 'Em casa':dados[8][2], 'fora':dados[8][3]}
        except:
            data['pontos'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Jogos sem sofrer gols'] = {'total':dados[9][1], 'Em casa':dados[9][2], 'fora':dados[9][3]}
        except:
            data['Jogos sem sofrer gols'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Não conseguiu marcar'] = {'total':dados[10][1], 'Em casa':dados[10][2], 'fora':dados[10][3]}
        except:
            data['Não conseguiu marcar'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Média de gols marcados por jogo'] = {'total':dados[11][1], 'Em casa':dados[11][2], 'fora':dados[11][3]}
        except:
            data['Média de gols marcados por jogo'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Média de gols sofridos por jogo'] = {'total':dados[12][1], 'Em casa':dados[12][2], 'fora':dados[12][3]}
        except:
            data['Média de gols sofridos por jogo'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Média de tempo do 1° gol marcado'] = {'total':dados[13][1], 'Em casa':dados[13][2], 'fora':dados[13][3]}
        except:
            data['Média de tempo do 1° gol marcado'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Média de tempo do 1° gol sofrido'] = {'total':dados[14][1], 'Em casa':dados[14][2], 'fora':dados[14][3]}
        except:
            data['Média de tempo do 1° gol sofrido'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Partidas com mais de 2,5 gols'] = {'total':dados[15][1], 'Em casa':dados[15][2], 'fora':dados[15][3]}
        except:
            data['Partidas com mais de 2,5 gols'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Partidas com menos de 2,5 gols'] = {'total':dados[16][1], 'Em casa':dados[16][2], 'fora':dados[16][3]}
        except:
            data['Partidas com menos de 2,5 gols'] = {'total':'', 'Em casa':'', 'fora':''}
        try:
            data['Gols marcados em %'] = {'total':dados[17][1], 'Em casa':dados[17][2], 'fora':dados[17][3]}
        except:
            data['Gols marcados em %'] = {'total':'','Em casa':"", 'fora':""}
        try:
            data['Gols sofridos em %'] = {'total':dados[18][1], 'Em casa':dados[18][2], 'fora':dados[18][3]}
        except:
            data['Gols sofridos em %'] = {'total':'','Em casa':"", 'fora':""}
        return data
     
    def salvar_imagem(self: object) -> None:
        elemento: HTMLSession = self.__bandeira
        dados: str = elemento[0]
        dados = (dados.attrs)['src']
        data = (dados.replace('data:image/png;base64,', '')).replace(' ', '+')
        imgdata = base64.b64decode(data)
        filename = f'core/static/assets/img/{self.__nome_time}.png'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
        
    def _min_gol(self: object) -> dict:
        elementos = self.__elementos_gols
        dados = self.capturar(elementos)
        min_gols = {}
        mg = {}
        cont = 0
        for i in dados:
            try:
                mg[i[0]] = i[1]
                cont += 1
            except:
                mg[i[0]] = ''
        min_gols["Minutos dos gols"] = mg
        
        return min_gols
        
    def _partidas(self: object) -> dict:
        table_jogo = ['#allLeagues tr', '#match9 tr', '#match10 tr', '#match11 tr', "#match12", "#match13", "#match14", "#match15"]
        titulos = self.capturar_titulo(self.__campeonatos)
        jogo = {}
        cont = 0
        for tit in titulos:
            tb = self._html.find(table_jogo[cont])
            dados = self.capturar(tb)
            jogo[tit] = self.capturar_jogos(dados)
            cont += 1
        return jogo

    def _equipe(self: object) -> dict:
        jogadores = {}
        dados = self.capturar(self.__jogadores)
        cont = 0
        for dado in dados:
            try:
                jogadores[dado[1]] = {"camisa":dado[0],"nome":dado[1],"posição":dado[2],"minutos jogados":dado[3],"comparecimento":dado[4],"convocação":dado[5],"jogador a entrar":dado[6],"jogador a sair":dado[7],"gols":dado[8],"média de gols por comparência":dado[9],"cartão amarelo":dado[10],"catões vermelho amarelo":dado[11],"cartões vermelho":dado[12]}
            except:
                ...
            cont += 1
        return jogadores

    def capturar_jogos(self: object ,dados: list) -> dict:
        jogos = {}
        dado = {}
        cont = 0
        for i in dados:
            cont += 1
            dado["dia"] = i[0]
            dado["data"] = i[1]
            dado["campeonato"] = i[2]
            dado["placar"] = i[4]
            dado["resultado"] = i[3]+" "+i[4]+" "+i[5]
            jogos[cont] = dado
            dado = {}
        return jogos
        
    def capturar(self: object, elements: HTMLSession) -> list:
        lista = []
        for i in elements:
            string = i.text
            lista.append(string.split("\n"))
        return lista
    
    def capturar_titulo(self: object, elements: HTMLSession) -> list:
        lista = []
        for i in elements:
            string = i.text
            lista.append(string)
        return lista
    
def main():
    arquivo_save = {}
    with open('apps/atena/script_core/saida.json', 'r', encoding='utf8') as arq:
        paises: dict = json.load(arq)
        for pais, times in paises.items():
            for time in times:
                atena: AtenaSS = AtenaSS(pais, time)
                print(atena.nome_time)
                estatisticas = atena.estatistica
                minutos_gols = atena.min_gols
                partidas = atena.partidas
                jogadores = atena.equipe
                try:
                    caminho = f'{atena.nome_time}.png'.replace(' ', '')
                    atena.salvar_imagem()
                except:
                    caminho = ''
                arquivo_save[atena.nome_time] = {'estatisticas':estatisticas, 'minutos gols':minutos_gols, 'partidas':partidas, 'equipe':jogadores, 'bandeira':caminho}
            with open(f'paises/{pais}.json', 'w') as arquivo:
                json.dump(arquivo_save, arquivo)
                arquivo_save.clear()

if __name__ == "__main__":
    main()