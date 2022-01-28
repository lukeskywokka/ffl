import csv
from bs4 import BeautifulSoup
import re
import requests
import collections
import sys

# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# data = https://www.pro-football-reference.com/years/2020/fantasy.htm

cost_hash = {}
players = []
def read_file(filename):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    for k, row in enumerate(csvreader):
        # regex for removing parentheses with team name
        # print(row[1])
        ret = re.sub("[\(\[].*?[\)\]]", "", row[1])
        if " II" in ret:
            ret = re.sub(" II", "", ret)
        if " III" in ret:
            ret = re.sub(" III", "", ret)
        if ret[-1] == " ":
            ret = ret[:-1]
        cost_hash[ret] = int(row[2])
        players.append(ret)
        #print(ret)
        #print(len(ret))
    the_file.close()
    print ("=============================")

pts_hash = {}
rank_hash = {}
ppg_hash = {}
pos_hash = {}
def read_pts_file(filename):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    ppt_hash = {}
    for k, row in enumerate(csvreader):
        # if k == 0 or k == 1:
        #     continue
        #print(row)
        ret = re.sub("\\\\.*", "", row[1])
        if "*" in row[1]:
            ret = re.sub("\*", "", ret)
        if "+" in row[1]:
            ret = re.sub("\+", "", ret)
        if "." in row[1]:
            ret = re.sub("\.", "", ret)
        if ret[-1] == " ":
            ret = ret[:-1]
        # print(ret)
        try:
            pts_hash[ret] = float(row[27])
            pos_hash[ret] = row[3]
            ppg_hash[ret] = float(row[27]) / int(row[5])
            rank_hash[ret] = int(row[0])
            # print(ppg_hash[ret])
        except ValueError:
            #print("No data for player")
            continue
        if ret in cost_hash:
            pass
            #print(f"{ret} = {row[27]} : {cost_hash[ret]}")
    the_file.close()


# will eventually need to sort by 
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
def bang_for_buck():
    qb = 3
    rb = 4
    wr = 6
    te = 2
    bang_hash = {}
    for k, v in cost_hash.items():
        if k in pts_hash and k in cost_hash:
            bang_hash[k] = pts_hash[k] / cost_hash[k]
    
    # sort in descending by value
    bang_hash = {k: v for k, v in sorted(bang_hash.items(), key=lambda item: item[1], reverse=True)}
    for k, v in bang_hash.items():
        print(f"{k}: {v}")


def reset_pos_map(pos_map):
    pos_map["QB"] = 1
    pos_map["RB"] = 2
    pos_map["WR"] = 4
    pos_map["TE"] = 1

def update(pos_map, player, scores, guys):
    if player not in pos_hash:
        return False
    if pos_hash[player] == "RB" and pos_map["RB"] > 0:
        pos_map["RB"] -= 1
        scores.append(pts_hash[player])
        guys.append(player)
    if pos_hash[player] == "WR" and pos_map["WR"] > 0:
        pos_map["WR"] -= 1
        scores.append(pts_hash[player])
        guys.append(player)
    if pos_hash[player] == "QB" and pos_map["QB"] > 0:
        pos_map["QB"] -= 1
        scores.append(pts_hash[player])
        guys.append(player)
    if pos_hash[player] == "TE" and pos_map["TE"] > 0:
        pos_map["TE"] -= 1
        scores.append(pts_hash[player])
        guys.append(player)
    return True

def update_ppg(pos_map, player, scores, guys):
    if player not in pos_hash:
        return False
    if pos_hash[player] == "RB" and pos_map["RB"] > 0:
        pos_map["RB"] -= 1
        scores.append(ppg_hash[player])
        guys.append(player)
    if pos_hash[player] == "WR" and pos_map["WR"] > 0:
        pos_map["WR"] -= 1
        scores.append(ppg_hash[player])
        guys.append(player)
    if pos_hash[player] == "QB" and pos_map["QB"] > 0:
        pos_map["QB"] -= 1
        scores.append(ppg_hash[player])
        guys.append(player)
    if pos_hash[player] == "TE" and pos_map["TE"] > 0:
        pos_map["TE"] -= 1
        scores.append(ppg_hash[player])
        guys.append(player)
    return True

def is_eligible(pos_map, player):
    if player not in pos_hash:
        return False
    if pos_hash[player] == "RB" and pos_map["RB"] > 0:
        return True
    if pos_hash[player] == "WR" and pos_map["WR"] > 0:
        return True
    if pos_hash[player] == "QB" and pos_map["QB"] > 0:
        return True
    if pos_hash[player] == "TE" and pos_map["TE"] > 0:
        return True
    return False

def best_draft_total_season():
    ret = {}
    pos_map = {}
    reset_pos_map(pos_map)
    money = 200
    maxx = float('-inf')
    maxx_guys = []
    scores = []
    guys = []
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            scores = []
            guys = []
            reset_pos_map(pos_map)
            money = 200 - cost_hash[players[j]] - cost_hash[players[i]]
            update(pos_map, players[j], scores, guys)
            update(pos_map, players[i], scores, guys)

            for k in range(j + 1, len(players)):
                if players[k] not in cost_hash or players[k] not in pts_hash:
                    continue
                if (money - cost_hash[players[k]]) < 0:
                    #print("whoops, can't buy him")
                    continue
                if (money - cost_hash[players[k]]) == 0:
                    if is_eligible(pos_map, players[k]):
                        scores.append(pts_hash[players[k]])
                        guys.append(players[k])
                        break
                    else:
                        continue
                    
                update(pos_map, players[k], scores, guys)
                # if not ret:
                #     continue
                money = money - cost_hash[players[k]]
                
            
            if sum(scores) > maxx:
                maxx = sum(scores)
                maxx_guys = guys
            # print(f"{sum(scores)} : {guys}")
            ret[sum(scores)] = guys
    
    print(maxx)
    print(maxx_guys)

    # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    # sort by key
    ret = collections.OrderedDict(sorted(ret.items()))
    i = 0
    rank = 0
    for k, v in ret.items(): 
        rank = 0
        
        for pl in v:
            rank += rank_hash[pl]
        avg_rank = 0
        if len(v) > 0:
            avg_rank = (rank / len(v))
            print(f"{i} : {avg_rank} : {k} :  {v}")
        i += 1
        # if "Tom Brady" in v and "Derrick Henry" in v:\
        #     print(f"{i} : {avg_rank} : {k} :  {v}")


def best_draft_ppg():
    ret = {}
    pos_map = {}
    reset_pos_map(pos_map)
    money = 200
    maxx = float('-inf')
    maxx_guys = []
    scores = []
    guys = []
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            scores = []
            guys = []
            reset_pos_map(pos_map)
            money = 200 - cost_hash[players[j]] - cost_hash[players[i]]
            update_ppg(pos_map, players[j], scores, guys)
            update_ppg(pos_map, players[i], scores, guys)

            for k in range(j + 1, len(players)):
                if players[k] not in cost_hash or players[k] not in ppg_hash:
                    continue
                if (money - cost_hash[players[k]]) < 0:
                    #print("whoops, can't buy him")
                    continue
                if (money - cost_hash[players[k]]) == 0:
                    if is_eligible(pos_map, players[k]):
                        scores.append(ppg_hash[players[k]])
                        guys.append(players[k])
                        break
                    else:
                        continue
                    
                update_ppg(pos_map, players[k], scores, guys)
                # if not ret:
                #     continue
                money = money - cost_hash[players[k]]
                
            
            if sum(scores) > maxx:
                maxx = sum(scores)
                maxx_guys = guys
            # print(f"{sum(scores)} : {guys}")
            ret[sum(scores)] = guys
    
    print(maxx)
    print(maxx_guys)

    # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    # sort by key
    ret = collections.OrderedDict(sorted(ret.items()))
    i = 0
    for k, v in ret.items(): 
        print(f"{i} : {k}: {v}")
        i += 1

            





read_file("draft.csv")
read_pts_file("2020_fantasy_pts.csv")
# best_draft_ppg()
best_draft_total_season()
# for item in split_list:
#     print(item)



# best full team:
# 3242.3
# ['Kyler Murray', 'CeeDee Lamb', 'Tom Brady', "Le'Veon Bell", 'Ronald Jones', 'James Conner', 'Justin Herbert', "D'Andre Swift", 'Mark Ingram', 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller', 'Tyler Higbee', 'Danny Amendola', 'Sony Michel']

# superflex: best starters: 2qb, 3rb, 3wr, 1te
# 2329.2999999999997
# ['James Conner', 'Alvin Kamara', 'Justin Herbert', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller', 'Ben Roethlisberger']


# starters: 2qb 2rb 4wr 1te
# rank 1 of 10532 : 2306.4: ['Ronald Jones', 'Davante Adams', 'James Conner', 'Justin Herbert', 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller', 'Ben Roethlisberger']

# starters: 2qb 4rb 2wr 1te
# 1 of 10390 : 2261.6: ['Ronald Jones', 'Alvin Kamara', 'James Conner', 'Justin Herbert', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Darren Waller', 'Ben Roethlisberger']

# starters: 2qb 2rb 3wr 2te
# 10663 : 2289.4: ['Ronald Jones', 'Alvin Kamara', 'Justin Herbert', 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller', 'Tyler Higbee', 'Ben Roethlisberger']

# starters: 2qb, 3rb 2wr 2te
# 1 of 10598 : 2203.5: ['James Conner', 'Alvin Kamara', 'Justin Herbert', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Darren Waller', 'Tyler Higbee', 'Ben Roethlisberger']


# no superflex: 3wr
# 9697 : 1897.5: ['Justin Herbert', 'Alvin Kamara', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller']

# no superflex: 3rb
# 9834 : 1808.1: ['James Conner', 'Alvin Kamara', 'Justin Herbert', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Darren Waller']


# superflex: 1qb 4rb 3 wr 1 te
# 1 of 10136 : 2248.4: ['Ronald Jones', 'Alvin Kamara', 'James Conner', 'Justin Herbert', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller']

# superflex: 1qb 3rb 4wr 1te
# 1 of 10075 : 2229.0: ['Ronald Jones', 'Davante Adams', 'James Conner', 'Justin Herbert', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller']


# superflex: 1qb 2rb 5wr 1te
# 1 of 10074 : 2206.5: ['Justin Herbert', 'Aaron Jones', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller', 'Sterling Shepard', 'Tyler Lockett']

# superflex: 1qb 4rb 3wr 1te
# 1 of 10136 : 2248.4: ['Ronald Jones', 'Alvin Kamara', 'James Conner', 'Justin Herbert', "D'Andre Swift", 'Marquise Brown', 'Calvin Ridley', 'Adam Thielen', 'Darren Waller']