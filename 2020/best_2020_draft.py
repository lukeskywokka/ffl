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
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

PNUM = int(sys.argv[1])
QBNUM = int(sys.argv[2])
RBNUM = int(sys.argv[3])
WRNUM = int(sys.argv[4])
TENUM = int(sys.argv[5])



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
    # print(header)
    rows = []
    for k, row in enumerate(csvreader):
        # regex for removing parentheses with team name
        # print(row[1])
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
    the_file.close()
    print ("=============================")

pts_hash = {}
rank_hash = {}
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
        #print(row)
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
            rank_hash[ret] = int(row[0])
            # print(ppg_hash[ret])
        except ValueError:
            #print("No data for player")
            continue
        if ret in cost_hash:
            pass
            #print(f"{ret} = {row[27]} : {cost_hash[ret]}")
    the_file.close()

def is_player_eligible(p, pos_map):
    if p not in pos_hash:
        return False
    elif update_pos_map(pos_map, pos_hash[p]):
        return True
    else:
        return False

def n_length_combo(lst, n, pos_map):
    #print("top")
    #print(lst)
    if n == 0:
        #print("n == 0")
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
        
        m = lst[i]
        # print(m)
        if not is_player_eligible(m, pos_map):
            continue
        remLst = lst[i + 1:]
        # print(remLst)
         
        for k, p in enumerate(n_length_combo(remLst, n-1, pos_map)):
            l.append([m]+p)
            if len(l[k]) == n:
                reset_pos_map(pos_map)
            #print(f"in loop: {k} : {l}")
    #print(f"returning: {l}")      
    return l


def reset_pos_map(pos_map):
    pos_map["QB"] = QBNUM
    # pos_map["RB"] = RBNUM
    # pos_map["WR"] = WRNUM
    # pos_map["TE"] = TENUM

def update_pos_map(pos_map, pos):
    if pos in pos_map and pos_map[pos] == 0:
        return False
    elif pos in pos_map:
        pos_map[pos] -= 1
        return True
    else:
        return True

def is_team_eligible(team, pos_map):
    money = 200
    reset_pos_map(pos_map)
    for p in team:
        money = money - cost_hash[p]
        if update_pos_map(pos_map, pos_hash[p]):
            continue
        elif money < 0:
            return False
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
            if ppg < 145:
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
        if i == 50:
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


def combos(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)



if __name__ == "__main__":
    read_file("draft.csv")
    read_pts_file("2020_fantasy_pts.csv")
    best_draft_itertools(PNUM)
    some_players = ["Kupp", "Deebo", "tyreek", "chase"]


# PPG: superflex 2qb, 2rb, 4wr, 1te


