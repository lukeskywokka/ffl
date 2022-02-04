from csv import reader
from bs4 import BeautifulSoup
from re import sub
# import requests
from collections import OrderedDict
import sys
from datetime import datetime
from itertools import combinations
# import numpy
# import multiprocessing
# import math
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
print("Arg1 = no. of players, Arg2 = no. of QBs, Arg3 = no. of RBs, Arg4 = ")
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# PNUM = int(sys.argv[1])
# QBNUM = int(sys.argv[2])
# RBNUM = int(sys.argv[3])
# WRNUM = int(sys.argv[4])
# TENUM = int(sys.argv[5])
# MONEY = int(sys.argv[6])
# PPG = int(sys.argv[7])



# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# data = https://www.pro-football-reference.com/years/2020/fantasy.htm


# pypy python: https://doc.pypy.org/en/latest/install.html
# symlinked to pypi
# downloaded to ~/luke/PYPI

cost_hash = {}
players = []
def read_file(filename):
    """
    Read cost file
    """
    the_file = open(filename)
    csvreader = reader(the_file)
    header = next(csvreader)
    local_cost_hash = {}
    # print(header)
    rows = []
    for k, row in enumerate(csvreader):
        # regex for removing parentheses with team name
        # print(row[1])
        # if k == 45:
        #     break
        ret = sub("[\(\[].*?[\)\]]", "", row[1])
        if " III" in ret:
            ret = sub(" III", "", ret)
        if " II" in ret:
            ret = sub(" II", "", ret)
        if "." in ret:
            ret = sub("\.", "", ret)
        if " Jr" in ret:
            ret = sub(" Jr", "", ret)
        if ret[-1] == " ":
            ret = ret[:-1]
        cost_hash[ret] = int(row[2])
        players.append(ret)
        #print(ret)
        #print(len(ret))
    # sort by value in reverse
    #cost_hash = {k: v for k, v in sorted(local_cost_hash.items(), reverse=True, key=lambda item: item[1])}
    # print(cost_hash)
    the_file.close()
    # print(players)
    print ("=============================")

pts_hash = {}
# rank_hash = {}
ppg_hash = {}
pos_hash = {}
def read_pts_file(filename):
    the_file = open(filename)
    csvreader = reader(the_file)
    header = next(csvreader)
    # print(header)
    rows = []
    ppt_hash = {}
    for k, row in enumerate(csvreader):
        # if k == 0 or k == 1:
        #     continue
        # print(row)
        ret = sub("\\\\.*", "", row[1])
        if "*" in row[1]:
            ret = sub("\*", "", ret)
        if "+" in row[1]:
            ret = sub("\+", "", ret)
        if "." in row[1]:
            ret = sub("\.", "", ret)
        if " III" in ret:
            ret = sub(" III", "", ret)
        if " II" in ret:
            ret = sub(" II", "", ret)
        if " Jr" in ret:
            ret = sub(" Jr", "", ret)
        if ret[-1] == " ":
            ret = ret[:-1]
        # print(ret)
        try:
            pts_hash[ret] = float(row[27])
            pos_hash[ret] = row[3]
            ppg_hash[ret] = float(row[27]) / int(row[5])
            # rank_hash[ret] = int(row[0])
            # print(ppg_hash[ret])
        except ValueError:
            #print("No data for player")
            continue
        if ret in cost_hash:
            pass
            #print(f"{ret} = {row[27]} : {cost_hash[ret]}")
    the_file.close()

rank_hash = {}
def ppg_rank():
    # sort by value
    sort_ppg_hash = {k: v for k, v in sorted(ppg_hash.items(), reverse=True, key=lambda item: item[1])}
    for k, item in enumerate(sort_ppg_hash):
        rank_hash[item] = k + 1
    #print(rank_hash)
    

rbs = []
qbs = []
tes = []
wrs = []
def separate_hashes():
    for item in cost_hash:
        pos = pos_hash[item]
        if pos == "RB":
            rbs.append(item)
        if pos == "WR":
            wrs.append(item)
        if pos == "TE":
            tes.append(item)
        if pos == "QB":
            qbs.append(item)
        else:
            pass


def is_player_eligible(p, pos_map):
    if p not in pos_hash:
        return False
    elif update_pos_map(pos_map, pos_hash[p]):
        return True
    else:
        return False


def reset_pos_map(pos_map):
    pos_map["QB"] = QBNUM
    pos_map["RB"] = RBNUM
    pos_map["WR"] = WRNUM
    pos_map["TE"] = TENUM

def update_pos_map(pos_map, pos):
    if pos in pos_map and pos_map[pos] == 0:
        return False

    if pos in pos_map and pos_map[pos] > 0:
        pos_map[pos] -= 1
        return True
    return True

def is_team_eligible(team, pos_map):
    money = MONEY
    reset_pos_map(pos_map)
    for p in team:
        money = money - cost_hash[p]
        if money < 0:
            return False
        
        if update_pos_map(pos_map, pos_hash[p]):
            continue
        else:
            return False
    return True

def money_check(team, money):
    for p in team:
        money = money - cost_hash[p]
        if money < 0:
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
    
p1_ret = {}
p2_ret = {}
p3_ret = {}
p4_ret = {}
def player_loop(players, id):
    print(f"{id}: starting loop")
    pos_map = {}
    ret_ppg = {}
    for p in players:
        if is_team_eligible(p, pos_map):
            ppg = 0
            total = 0
            # print(r)
            ppg = get_team_ppg(p)
            # total = get_team_total(r)
            ret_ppg[ppg] = p
    print(f"{id}: Lists gathered. Going to order them: {datetime.now()}")
    ret_ppg = OrderedDict(sorted(ret_ppg.items(), reverse=True))
    print(f"{id}: Lists ordered. Going to print them: {datetime.now()}")
    i = 0
    print(f"{id}: PPG")
    for k, v in ret_ppg.items(): 
        if i == 10:
            break
        print(f"{i} : {k} : {v}")
        i += 1
    print("=============")
    
def best_positions_draft(player_group, num_players, money):
    start = datetime.now()
    print(start)
    ret = (combinations(player_group, num_players))
    pos_map = {}
    # print(f"Combos Received at {datetime.now()}...calculating points")
    ret_pts = {}

    # Single process
    ret_ppg = {}
    for r in ret:
        if money_check(r, money):
            ppg = 0
            ppg = get_team_ppg(r)
            ret_ppg[ppg] = r
    
    # print(f"Done collecting points information at {datetime.now()} ")

    # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    # sort by key
    ret_ppg = OrderedDict(sorted(ret_ppg.items(), reverse=True))
    i = 0
    # print("PPG")
    for k, v in ret_ppg.items(): 
        avg_rank = 0
        for j in v:
            avg_rank += rank_hash[j]
        avg_rank = avg_rank / len(v)
        if i == 10:
            break
        print(f"{i} : {k} : {v} : {avg_rank} : {money}")
        i += 1
    print("=============")
    stop = datetime.now()
    print("=======")
    #print(f"Start = {start}")
    #print(f"Stop = {stop}")

# https://stackoverflow.com/questions/23816546/how-many-processes-should-i-run-in-parallel
def best_draft_itertools(num_players):
    # combo_num = math.comb(len(players), num_players)
    start = datetime.now()
    print(start)
    ret = (combinations(players, num_players))
    # for r in ret:
    #     r.append("heheheh")
    #     print(r)
    pos_map = {}
    print(f"Combos Received at {datetime.now()}...calculating points")
    ret_pts = {}
    # chunks = int(combo_num / 2)
    # manager = multiprocessing.Manager()
    # ret_ppg = manager.dict()
    
    # p1 = multiprocessing.Process(target=player_loop, args=(ret[0:chunks], 1))
    # p2 = multiprocessing.Process(target=player_loop, args=(ret[chunks-1:], 2))
    #chunks += chunks
    #p3 = multiprocessing.Process(target=player_loop, args=(ret[chunks-1:], 3))
    # chunks += chunks
    # p4 = multiprocessing.Process(target=player_loop, args=(ret[chunks-1:], 4))
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # global p1_ret, p2_ret
    # print(f"{len(p1_ret)}, {len(p2_ret)}")
    # ret_ppg = {**p1_ret, **p2_ret}
    # print(len(ret_ppg))
    # for k, v in ret_ppg.items():
    #     print(v)

    # Single process
    ret_ppg = {}
    for r in ret:
        if is_team_eligible(r, pos_map):
            ppg = 0
            # total = 0
            # print(r)
            ppg = get_team_ppg(r)
            # total = get_team_total(r)
            if ppg < PPG:
                continue
            ret_ppg[ppg] = r
            # ret_pts[total] = r
    
    print(f"Done collecting points information at {datetime.now()} ")

    # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    # sort by key
    ret_ppg = OrderedDict(sorted(ret_ppg.items(), reverse=True))
    # ret_pts = collections.OrderedDict(sorted(ret_pts.items(), reverse=True))
    i = 0
    print("PPG")
    for k, v in ret_ppg.items(): 
        if i == 1:
            break
        print(f"{i} : {k} : {v}")
        i += 1
    print("=============")
    # print("Total points")
    # i = 0
    # for k, v in ret_pts.items(): 
    #     if i == 30:
    #         break
    #     print(f"{i} : {k} : {v}")
    #     i += 1
    stop = datetime.now()
    print("=======")
    print(f"Start = {start}")
    print(f"Stop = {stop}")





if __name__ == "__main__":
    read_file("draft.csv")
    read_pts_file("2020_fantasy_pts.csv")
    # best_draft_itertools(PNUM)
    separate_hashes()
    ppg_rank()
    print(len(wrs))
    print(len(rbs))
    # for i in range(20, 100):

    best_positions_draft(wrs, 6, 80)


# 3 WR 47 and I get tyreek, stefon, will fuller at 59 ppg avg rank = 24.6
# 3 RBs spending 75 -> 150 ppg goes from 57 -> 67: 1 baller: Kamara, Montgomery, Gibson (rook)
# 4 WRs spending 50 -> 150 goes from 76-86 ppg: baller, journeyman/newcomer (fuller), newcomer (diggs), rook
# 2 QBs: newcomer, vet for $20.  48 ppg at $20 vs 52ppg at $99
# 1 TE: newcomer/unknown Darren Waller (17ppg) for $11 vs Travis Kelce (20.8ppg) for $45
# 3 qbs: rook, journeyman, avg vet: $3 for 63ppg.  $99 for 76 ppg.  $19 for 71ppg: newcomer, rook, vet
# 4rbs: $25: 60ppg, rook, rook, 2nd year, vet....$50: 64 ppg, kinda baller, 2nd year, vet, rook
# 4 wrs: spending $20 gets you 3 relative unknowns and a vet at 72ppg
# 6 wrs: spending $60 gets stud, newcomer, newcomer, rook, rook, rook OR stud, studly vet, newcomer, newcomer, rook, rook at 109ppg
# 6 rbs: spending $95 gets, stud, rook, 2nd year, vet, rook, rook OR instead of rooks, backups at 96ppg
# 6rbs: at $105 gets 101 ppg
# 6wrs: at $80 gets 114ppg


# 2021: 
# WR: 6 for 60
# baller: deebo, tyreek, kupp, davante, JJ, Diggs, DK, Godwin, Ridley
# in between: diontae Johnson
# newcomer: Renfrow, Waddle, Devonta? Rondale or Elijah Moore? Toney
# rook: metchie?

# RBS 6 for $95
# baller: can we get cmac for cheap? Ekeler, Najee
# vet: chubb, conner, Lenny, Jacobs, Singletary, Swift, Akers, Pollard, Montgomery??, Saquon??
# newcomer: javonte, michael carter jr, Elijah Mitchell, Rhamondre, Penny, Harris, helaire
# rook: watch draft

# Qbs: 20 for 2 or 3
# baller: Mahomes, Allen, Jackson, Murray, burrow, Stafford
# vet: Rodgers, Russ, Carr
# avg vet: Cousins, Jimmy G, Matt Ryan, Tua
# newcomer: Zach Wilson, Trevor Lawrence
# rook: trey, Malik
# bleh: Daniel Jones (brian daboll), goff


# TE:15
# baller: waller, kelce, kittle, Andrews
# avg: Hockenson, Fant, Henry, Gesicki
# newcomer: PITTS
# Pat Freiermuth
    



# PPG: superflex 2qb, 2rb, 4wr, 1te


