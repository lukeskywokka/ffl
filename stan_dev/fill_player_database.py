import csv
import re
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import sqlite3
import time
import os

con = sqlite3.connect("wr.db")
with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS WR_WEEKLY (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            week1 TEXT,
            week2 TEXT,
            week3 TEXT,
            week4 TEXT,
            week5 TEXT,
            week6 TEXT,
            week7 TEXT,
            week8 TEXT,
            week9 TEXT,
            week10 TEXT,
            week11 TEXT,
            week12 TEXT,
            week13 TEXT,
            week14 TEXT,
            week15 TEXT,
            week16 TEXT,
            week17 TEXT,
            week18 TEXT,
            total TEXT
        );
    """)

sql = """
INSERT INTO WR_WEEKLY (
            name, 
            week1,
            week2,
            week3,
            week4,
            week5,
            week6,
            week7,
            week8,
            week9,
            week10,
            week11,
            week12,
            week13,
            week14,
            week15,
            week16,
            week17,
            week18,
            total ) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

def make_initial_entry():
    data_set = ("Name", "Week1", "Week2",
    "Week3", "Week4", "Week5", "Week6", "Week7", "Week8",
    "Week9", "Week10", "Week11", "Week12", "Week13", "Week14",
    "Week15", "Week16", "Week17", "Week18", "Total")
    with con:
        try:
            con.execute(sql, data_set)
        except sqlite3.IntegrityError:
            print("Whoops, that data must already exist")


def read_file(filename):
    """
    Get player names from CSV downloaded from fantasypros
    """
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    players = []
    for row in csvreader:
        #print(row)
        if len(row) > 2 and row[1] != "Rank":
            # regex for removing parentheses with team name
            ret = re.sub("[\(\[].*?[\)\]]", "", row[1])
            ret = ret.lower()
            if "." in ret:
                #print(ret)
                ret = re.sub("\.", "", ret)
            if "'" in ret:
                ret = re.sub("\'", "", ret)
            if " jr" in ret:
                ret = re.sub(" jr", "", ret)
            if " sr" in ret:
                ret = re.sub(" sr", "", ret)
            if " iii" in ret:
                ret = re.sub(" iii", "", ret)
            if " ii" in ret:
                ret = re.sub(" ii", "", ret)
            if " iv" in ret:
                ret = re.sub(" iv", "", ret)
            if " v" in ret:
                ret = re.sub(" v", "", ret)

            if ret[-1] == " ":
                ret = ret[:-1]
            players.append(ret)
            print(ret.lower())
        #print("====")
    the_file.close()
    print ("=============================")
    return players

def get_weekly_fantasy_points(wr, weeks):
    ret = [wr]
    for k, w in enumerate(weeks):
        cols = w.find_all("td")
        print(len(cols))
        # print(cols)
        print("===")
        # skipping headers
        if k == 0 or k == 1:
            continue

        if "BYE" in cols[1].text:
            ret.append("BYE")
        elif len(cols) != 17:
            ret.append("OUT")
        elif len(cols) == 17:
            ret.append(cols[16].text)
        else:
            ret.append("IDK")
    
    return ret



def fetch_season_data(wrs):
    """
    """
    player_htmls = os.listdir("player_htmls")
    skipped = []
    for wr in wrs:
        print(wr)
        pattern = r' '
        mod_wr = re.sub(pattern, '-', wr)

        # check for local copy of html
        if f"{mod_wr}.html" in player_htmls:
            print(f"found {mod_wr} locally")
            with open(f'player_htmls/{mod_wr}.html') as f:
                soup = BeautifulSoup(f, "html.parser")       
        else:
            player_url = f"https://www.fantasypros.com/nfl/games/{mod_wr}.php?scoring=PPR"
            print(player_url)
            page = requests.get(player_url)
            with open(f'player_htmls/{mod_wr}.html', 'w') as f:
                f.write(page.text)
            soup = BeautifulSoup(page.content, "html.parser")
        games_table = soup.find("table")
        week_elements = games_table.find_all("tr")

        # this means wrong url. Will likely need custom fixes
        if len (week_elements) < 21:
            print(f"skipping {mod_wr}")
            skipped.append(mod_wr)
            continue
        d = get_weekly_fantasy_points(wr, week_elements)
        data_set = (d[0], d[1], d[2], d[3],
            d[4], d[5], d[6], d[7], d[8],
            d[9], d[10], d[11], d[12], d[13],
            d[14], d[15], d[16], d[17], d[18], d[19])
        print(data_set)
        with con:
            try:
                con.execute(sql, data_set)
            except sqlite3.IntegrityError:
                print("Whoops, that data must already exist")
        time.sleep(2)
        print("=============")
    print(skipped)
        


make_initial_entry()
wrs = read_file("wr_full_year.csv")
fetch_season_data(wrs)
# special_list = ["Mike Williams"]
with con:
    data = con.execute("SELECT * FROM WR_WEEKLY")
    for row in data:
        print(row)
    


# url = 'https://www.facebook.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)

# open('facebook.ico', 'wb').write(r.content)