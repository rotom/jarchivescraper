import requests
import bs4
import time

##Use beautifulsoup to get data about contestants and clues###

class jeopardyGame():

    def __init__(self, game_id):
        
        self.root = "http://www.j-archive.com/showgame.php?game_id="
        self.game_id = game_id
        self.req = requests.get(self.root+self.game_id)
        self.soup = bs4.BeautifulSoup(self.req.text, 'lxml')

    def get_clues_with_cats(self):
        
        pass

    def get_contestants(self, gender=False):

        contestants = self.soup.find_all('p', class_='contestants')[:3]
        return [c.contents[0].getText() for c in contestants]
        
        #return [p.contents[0].contents[0] for p in contestants]

    def get_date(self):
        
        date = self.soup.title.text.split(' ')[-1]
        year, month, day = date.split('-')
        return date

    def get_winner(self):
        pass

    def close(self):
        pass

class Contestant():

    def __init__(self, name, is_champ = False, winnings=0, streak=0):
        
        self.name = name
        self.is_champ = is_champ
        self.winnings = winnings
        self.streak = 0 #number of games won

    def get_gender(self):

        self.gender = get_gender_from_name(self.name)

class Clue():

    def __init__(self):

        self.text = text
        self.value = value
        self.category = category       
            

if __name__ == '__main__':
    #game_id = 1
    for game_id in range(1,500):
        game_id_str = str(game_id)
        game = jeopardyGame(game_id_str)
        print "Game", game_id_str,":", game.get_contestants()
        game.get_date()
        game.close()
        game_id += 1
            #raise Exception("Game",game_id_str,"not found.")
        #while 1:

            #game = jeopardyGame(game_id)
            #game_id += 1
    
