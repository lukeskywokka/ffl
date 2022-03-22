import sqlite3
from bs4 import BeautifulSoup
import time
import os
import requests


url = "https://www.pro-football-reference.com/teams/sfo/2019.htm"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
stats_table = soup.find("table", id="team_stats")
rows = stats_table.find_all("tr")

# PF	Yds	Ply	Y/P	TO	FL	1stD	Cmp	Att	Yds	TD	Int	NY/A	1stD	Att	Yds	TD	Y/A	1stD	Pen	Yds	1stPy	#Dr	Sc%	TO%	Start	Time	Plays	Yds	Pts
for k, v in enumerate(rows):
    print(f"Row = {k}")
    data = v.find_all("td")
    if k == 2:
        # team stats

    elif k == 3:
        # opp stats

    elif k == 4:
        # off rank

    elif k == 5:
        # def rank


    for d in data:
        print(d.text)


def get_team_stats():

    pass


def get_opp_stats():
    pass


def get_off_rank():
    pass


def get_def_rank():
    pass