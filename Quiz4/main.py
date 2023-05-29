import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
import random
file = open("games.csv","w",newline="\n",encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(["Title","Rating","Info"])


page = 1
while page < 6 :
    url = f"https://en.softonic.com/downloads/online-games/{page}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    games_soup = soup.find("ol",class_="topic-list mb-m")
    all_games = games_soup.find_all("li",class_="s-list-item topic-item topic-list__item")
    for games in all_games:
        title = games.find("h2",class_="app-info__name").text
        rating = games.find('div',class_="rating-info rating-info--fix-small").text
        info = games.find("h3",class_="app-info__description").text
        file.write(title + ',' + rating + ',' + info +','+'\n')
    page+=1
    sleep(random.randint(15,20))