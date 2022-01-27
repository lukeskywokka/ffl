import os 
from bs4 import BeautifulSoup
import requests



def test_local_soup():
    with open('player_htmls/deebo-samuel.html') as f:
        soup = BeautifulSoup(f, "html.parser")     

    games_table = soup.find("table")
    week_elements = games_table.find_all("tr")
    for w in week_elements:
        print(w)

def test_skip_pages_not_found():
    mod_wr = "cooper-kupp"
    player_url = f"https://www.fantasypros.com/nfl/games/{mod_wr}.php?scoring=PPR"
    page = requests.get(player_url)
    soup = BeautifulSoup(page.content, "html.parser")
    games_table = soup.find("table")
    #print(page)
    # print(soup)
    # print(games_table)
    week_elements = games_table.find_all("tr")
    print(len(week_elements))
    # for w in week_elements:
    #     print(w)



test_skip_pages_not_found()