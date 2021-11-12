import requests
import json
from datetime import date
from pprint import pprint

class MatchIDToday:
    
    def __init__(self: object) -> None:
        self.__data: date = date.today()
        self.__url: str = f"https://widgets.fn.sportradar.com/common/en/America:Montevideo/gismo/sport_matches/1/{str(self.__data)}"
        self.__response: requests = self.get_response()
        self.__matchID: dict = self.get_matchID()
        
    @property
    def url(self: object) -> str:
        return self.__url
    
    @property
    def matchID(self: object) -> dict:
        return self.__matchID
        
    def get_response(self: object) -> requests:
        response: requests = requests.get(self.__url)
        return response
    
    def get_matchID(self: object) -> dict:
        resposta = self.__response
        texto = resposta.text
        matchID = {}
        ret = json.loads(texto)
        ret = ret["doc"]
        ret = ret[0]
        ret = ret['data']
        ret = ret["sport"]
        ret = ret['realcategories']
        for r in ret:
            list_tournaments = r['tournaments']
            for tournaments in list_tournaments:
                list_matches = tournaments['matches']
                for matches in list_matches:
                    try:
                        id = matches['_id']
                    except:
                        id = ""
                    try:
                        teams = matches['teams']
                    except:
                        ...
                    try:
                        teams_away = teams['away']
                    except:
                        ...
                    try:
                        teams_home = teams["home"]
                    except:
                        ...
                    try:
                        team_away = teams_away['name']
                    except:
                        team_away = ''
                    try:
                        team_home = teams_home['name']
                    except:
                        team_home = ''
                    matchID[id] = {'away':team_away,'home':team_home}
        return matchID
    
def matchID(data: str) -> dict:
    resposta = requests.get(f"https://widgets.fn.sportradar.com/common/en/America:Montevideo/gismo/sport_matches/1/{data}")
    texto = resposta.text
    matchID = {}
    ret = json.loads(texto)
    ret = ret["doc"]
    ret = ret[0]
    ret = ret['data']
    ret = ret["sport"]
    ret = ret['realcategories']
    for r in ret:
        list_tournaments = r['tournaments']
        for tournaments in list_tournaments:
            list_matches = tournaments['matches']
            for matches in list_matches:
                try:
                    id = matches['_id']
                except:
                    id = ""
                try:
                    teams = matches['teams']
                except:
                    ...
                try:
                    teams_away = teams['away']
                except:
                    ...
                try:
                    teams_home = teams["home"]
                except:
                    ...
                try:
                    team_away = teams_away['name']
                except:
                    team_away = ''
                try:
                    team_home = teams_home['name']
                except:
                    team_home = ''
                matchID[id] = {'away':team_away,'home':team_home}
    return matchID
                    
if __name__ == "__main__":
     m = MatchIDToday()
     pprint(m.matchID)
    