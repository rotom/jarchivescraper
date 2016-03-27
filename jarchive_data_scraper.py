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
        return [p.contents[0].contents[0] for p in self.soup.find_all('p', class_='contestants')]

    def get_date(self):
        return self.soup.title.text.split(' ')[-1]

    def get_winner(self):
        pass

    def close(self):
        pass
        
            

if __name__ == '__main__':
    #game_id = 1
    for game_id in range(1,500):
        game_id_str = str(game_id)
        game = jeopardyGame(game_id_str)
        #print "Game", game_id_str,":", game.get_contestants()
        game.get_date()
        game.close()
        game_id += 1
            #raise Exception("Game",game_id_str,"not found.")
        #while 1:

            #game = jeopardyGame(game_id)
            #game_id += 1
    
