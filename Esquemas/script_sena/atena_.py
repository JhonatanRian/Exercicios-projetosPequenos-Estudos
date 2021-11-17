from requests_html import HTMLSession

class AtenaSS:
    
    def __init__(self: object, pais: str, time: str) -> None:
        self.__url: str = f"https://pt.soccerstats247.com/equipas/{pais}/{time}/"
        self.__secao: HTMLSession = HTMLSession()
        self.__resposta = self.__secao.get(self.__url)
        self._html: HTMLSession = self.__resposta.html
        self.__elementos_estatistica: HTMLSession = self._html.find("div[id='statisticsSlider'] tr")
        self.__elementos_gols: HTMLSession = self._html.find("#scoringMinutesSlider tr")
        self.__campeonatos: HTMLSession = self._html.find("#tabHeaders a")
        self.__jogadores: HTMLSession = self._html.find("#squadSlider tr")
        self.__estatistica: dict = self._estatistica()
        self.__minutos_gols: dict = self._min_gol()
        self.__partidas: dict = self._partidas()
        self.__equipe: dict = self._equipe()
        
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
        data[dados[0][0].split(',')[0]] = dados[0][0].split(',')[1]
        try:
            data['Classificação'] = {'total': dados[1][1]}
        except:
            data['Classificação'] = {'total': ''}
        data['Partidas jogadas'] = {'total':dados[2][1], 'Em casa':dados[2][2], 'fora':dados[2][3]}
        data['Vitórias'] = {'total':dados[3][1], 'Em casa':dados[3][2], 'fora':dados[3][3]}
        data['Empate'] = {'total':dados[4][1], 'Em casa':dados[4][2], 'fora':dados[4][3]}
        data['Derrota'] = {'total':dados[5][1], 'Em casa':dados[5][2], 'fora':dados[5][3]}
        data['Gols marcados'] = {'total':dados[6][1], 'Em casa':dados[6][2], 'fora':dados[6][3]}
        data['Gols sofridos'] = {'total':dados[7][1], 'Em casa':dados[7][2], 'fora':dados[7][3]}
        data['pontos'] = {'total':dados[8][1], 'Em casa':dados[8][2], 'fora':dados[8][3]}
        data['Jogos sem sofrer gols'] = {'total':dados[9][1], 'Em casa':dados[9][2], 'fora':dados[9][3]}
        data['Não conseguiu marcar'] = {'total':dados[10][1], 'Em casa':dados[10][2], 'fora':dados[10][3]}
        data['Média de gols marcados por jogo'] = {'total':dados[11][1], 'Em casa':dados[11][2], 'fora':dados[11][3]}
        data['Média de gols sofridos por jogo'] = {'total':dados[12][1], 'Em casa':dados[12][2], 'fora':dados[12][3]}
        data['Média de tempo do 1° gol marcado'] = {'total':dados[13][1], 'Em casa':dados[13][2], 'fora':dados[13][3]}
        data['Média de tempo do 1° gol sofrido'] = {'total':dados[14][1], 'Em casa':dados[14][2], 'fora':dados[14][3]}
        data['Partidas com mais de 2,5 gols'] = {'total':dados[15][1], 'Em casa':dados[15][2], 'fora':dados[15][3]}
        data['Partidas com menos de 2,5 gols'] = {'total':dados[16][1], 'Em casa':dados[16][2], 'fora':dados[16][3]}
        data['Gols marcados em %'] = {'total':dados[17][1], 'Em casa':dados[17][2], 'fora':dados[17][3]}
        data['Gols sofridos em %'] = {'total':dados[18][1], 'Em casa':dados[18][2], 'fora':dados[18][3]}
        return data
        
    def _min_gol(self: object) -> dict:
        elementos = self.__elementos_gols
        dados = self.capturar(elementos)
        min_gols = {}
        mg = {}
        cont = 0
        for i in dados:
            mg[i[0]] = i[1]
            cont += 1
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
        jogador = {}
        jogadores = {}
        dados = self.capturar(self.__jogadores)
        cont = 0
        for dado in dados:
            if cont > 0:
                try:
                    jogador[cont] = {"camisa":dado[0],"nome":dado[1],"posição":dado[2],"minutos jogados":dado[3],"comparecimento":dado[4],"convocação":dado[5],"jogador a entrar":dado[6],"jogador a sair":dado[7],"gols":dado[8],"média de gols por comparência":dado[9],"cartão amarelo":dado[10],"catões vermelho amarelo":dado[11],"cartões vermelho":dado[12]}
                    jogadores[cont] = jogador
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
    

if __name__ == "__main__":    
    bot = AtenaSS("brasil", "abc")
    print(bot.estatistica)