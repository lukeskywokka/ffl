import csv
from bs4 import BeautifulSoup
import re
import requests
import collections
import sys
import csv
import itertools
import datetime

players = []
cost_hash = {}
def get_cost():
    """
    This page looks like it's updated.  Everytime we run this script, 
    we should probably just pull from there. No need to cache this file.
    """
    cost_url = "https://www.footballdiehards.com/fantasyfootball/dailygames/Draftkings-Salary-data.cfm"
    cost_page = requests.get(cost_url)
    soup_cost = BeautifulSoup(cost_page.content, "html.parser")
    cost_table = soup_cost.find("table")
    cost_rows = cost_table.find_all("tr")
    for k, row in enumerate(cost_rows):
        if k == 0 or k == 1:
            continue
        cols = row.find_all("td")
        # print(cols[0].text)
        name = cols[0].text.split(",")
        name[1] = name[1].replace(" ", "")
        # print(name)
        first_last = name[1] + " " + name[0]
        players.append(first_last)
        cost_hash[first_last] = int(cols[4].text.replace("$", ""))

    print(len(cost_rows))
    sys.exit(1)
    print(cost_hash)
    print("======")



# get player stats
# stats_url = "https://fantasydata.com/nfl/fantasy-football-leaders?position=1&season=2021&seasontype=3&scope=1&subscope=1&scoringsystem=2&startweek=1&endweek=1&aggregatescope=1&range=1"
# stats_page = requests.get(stats_url)
# soup_stats = BeautifulSoup(stats_page.content, "html.parser")
# if 'Tyreek' in soup_stats:
#     print("found reek")
# stats_table = soup_stats.find("table")
# stats_rows = stats_table.find_all("tr")

ppg_hash = {}
pts_hash = {}
pos_hash = {}
def read_file(filename):
    """
    Get player names from CSV downloaded from fantasypros
    """
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    # header = next(csvreader)
    # print(header)
    #players = []
    for row in csvreader:
        # print(row)
        name = row[1].split(" ")
        # print(name)
        fname = name[0]
        lname = name[1]
        suffix = ""
        if name[2] != 'Q' or name[2] != '':
            suffix = " " + name[2]

        fullname = fname + " " + lname + suffix
        if fullname[-1] == " ":
            fullname = fullname[:-1]
        ppg_hash[fullname] = float(row[-2])
        pts_hash[fullname] = float(row[-1])
        pos_hash[fullname] = (row[-13])
    the_file.close()
    print(pts_hash)
    print ("=============================")
    print(ppg_hash)
    print("===")
    print(pos_hash)
    print("=================")
    print(players)
            

def reset_pos_map(pos_map):
    pos_map["QB"] = 1
    pos_map["RB"] = 2
    pos_map["WR"] = 4
    pos_map["TE"] = 1

def update_pos_map(pos_map, pos):
    if pos not in pos_map or pos_map[pos] == 0:
        return False
    else:
        pos_map[pos] -= 1
        return True

def is_team_eligible(team, pos_map):
    money = 47200
    for p in team:
        money = money - cost_hash[p]
        if p not in pos_hash:
            return False
        elif money < 0:
            return False
        elif update_pos_map(pos_map, pos_hash[p]):
            continue
        else:
            return False
    return True

def get_team_ppg(team):
    ppg = 0
    for p in team:
        ppg += ppg_hash[p]
    return ppg

def get_team_total(team):
    tot = 0
    for p in team:
        tot += pts_hash[p]
    return tot

def best_draft_itertools():
    start = datetime.datetime.now()
    ret = itertools.combinations(players, 8)
    pos_map = {}
    ret_ppg = {}
    ret_pts = {}
    for r in ret:
        reset_pos_map(pos_map)
        ppg = 0
        total = 0
        if is_team_eligible(r, pos_map):
            ppg = get_team_ppg(r)
            total = get_team_total(r)
            ret_ppg[ppg] = r
            ret_pts[total] = r

    # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    # sort by key
    ret_ppg = collections.OrderedDict(sorted(ret_ppg.items()))
    i = 0
    for k, v in ret_ppg.items(): 
        print(f"{i} : {k} : {v}")
        i += 1
    stop = datetime.datetime.now()
    print("=======")
    print(start)
    print(stop)


get_cost()
read_file("playoff_stats.csv")
best_draft_itertools()
# best_draft_postseason()
# best_draft_itertools()
# best_draft_ppg()


# 3 rbs
# 1824 : 164.39999999999998 : ('Cam Akers', 'Jerick McKinnon', 'Joe Mixon', 'Byron Pringle', 'Patrick Mahomes', 'Odell Beckham Jr.', 'Travis Kelce', 'Tyreek Hill')

# 4 wrs
# 2110 : 167.7 : ('Jerick McKinnon', 'C.J. Uzomah', 'Joe Mixon', 'Byron Pringle', 'Mecole Hardman', 'Patrick Mahomes', 'Tyreek Hill', 'Cooper Kupp')

# 2 tes
# 2351 : 176.89999999999998 : ('Jerick McKinnon', 'C.J. Uzomah', 'Joe Mixon', 'Byron Pringle', 'Patrick Mahomes', 'Travis Kelce', "Ja'Marr Chase", 'Tyreek Hill')