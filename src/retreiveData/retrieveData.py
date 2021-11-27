from chessdotcom import get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def get_most_recent_games(username):
    data = get_player_game_archives(username).json

    #reminder to change to data['archives'][-1] to get latest game
    url = data['archives'][-1]
    games = requests.get(url).json()
    last_game_played = games['games'][-1]
    moves = last_game_played['pgn']
    string = ""
    moveList = []
    count = 0
    for i in reversed(range(len(moves))):
        if moves[i] == 'n':
            break
        if moves[i] == ' ':
            moveList.append(string)
            string = ""
        string =  moves[i] + string
    # print(moveList[::-1])
    newList = []
    for i in moveList[::-1]:
        if count == 3:
            count = 0
        elif count == 1:
            newList.append(i)
            count = count + 1
        else:
            count = count + 1
    # print(moveList[::-1][0])
    return newList

def getColor(username):
    data = get_player_game_archives(username).json

    #reminder to change to data['archives'][-1] to get latest game
    url = data['archives'][-1]
    games = requests.get(url).json()
    last_game_played = games['games'][-1]
    # printer.pprint(last_game_played)
    black = last_game_played['black']
    white = last_game_played['white']
    if black['username'] == username:
        return "black"
    else:
        return "white"

