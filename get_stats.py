from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#Analyzing the 2020/21 NBA Season
year = 2020

#URL page we will scraping
url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html".format(year)

#Get HTML from URL
html = urlopen(url)

soup = BeautifulSoup (html)

soup.findAll('tr', limit = 2)

headers = [th.getText() for th in soup.findAll('tr', limit = 2)
[0].findAll('th')]

headers = headers[1:]

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                                                for i in range(len(rows))]
stats = pd.DataFrame(player_stats, columns = headers)
stats.head(10)

#We have dataset with colums player names, position, age, team, games played/started, minutes played,
# FG/game, FGA/game, FG%, 3P/game, 3PA/game, 3P%, 2P/game, 2PA/game, 2P%, eFG%, FT/game, FTA, FT%, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS

#Trim dataset to only include Player, Team, TRB, AST, STL, BLK, TOV, PTS
stats = stats[['Player','Tm','TRB','AST','STL','BLK','TOV', 'PTS']]

#print(stats)
