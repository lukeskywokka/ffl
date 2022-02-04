from csv import reader
from bs4 import BeautifulSoup
from re import sub
# import requests
from collections import OrderedDict, defaultdict
import sys
from datetime import datetime
from itertools import combinations

# https://wolfsports.com/fantasy-football/2021-fantasy-football-mock-draft-2-0-12-team-superflex-ppr/
# import numpy
# import multiprocessing
# import math
# n = len(sys.argv)
# print("Total arguments passed:", n)
 
# # Arguments passed
# print("\nName of Python script:", sys.argv[0])
 
# print("\nArguments passed:", end = " ")
# for i in range(1, n):
#     print(sys.argv[i], end = " ")

# PNUM = int(sys.argv[1])
# QBNUM = int(sys.argv[2])
# RBNUM = int(sys.argv[3])
# WRNUM = int(sys.argv[4])
# TENUM = int(sys.argv[5])



# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# data = https://www.pro-football-reference.com/years/2020/fantasy.htm


# pypy python: https://doc.pypy.org/en/latest/install.html
# symlinked to pypi
# downloaded to ~/luke/PYPI

pts_hash = {}
ppg_hash = {}
pos_hash = {}

# rank by ppg
rank_hash = {}
players = []
def read_file(filename):
    """
    Get player names from CSV downloaded from fantasypros
    """
    the_file = open(filename)
    csvreader = reader(the_file)
    # header = next(csvreader)
    # print(header)
    #players = []
    
    for row in csvreader:
        if row[2] != "QB" and row[2] != "RB" and row[2] != "WR" and row[2] != "TE":
            continue
        # print(row)
        rank = int(row[0])

        name = row[1].split(" ")
        fname = name[0]
        lname = name[1]
        suffix = ""
        if name[2] != 'Q' or name[2] != '':
            suffix = " " + name[2]

        fullname = fname + " " + lname + suffix
        if fullname[-1] == " ":
            fullname = fullname[:-1]
        players.append(fullname)
        ppg_hash[fullname] = float(row[-2])
        pts_hash[fullname] = float(row[-1])
        pos_hash[fullname] = (row[2])
        rank_hash[fullname] = rank
    the_file.close()
    # print(pts_hash)
    # print ("=============================")
    # print(ppg_hash)
    # print("===")
    # print(pos_hash)
    # print("=================")
    # print(players)

drafted_players = []
draft_hash = defaultdict(list)
def read_draft_file(filename):
    the_file = open(filename)
    csvreader = reader(the_file)
    draft_round = 0
    k = 0
    for row in (csvreader):
        if row:
            k += 1
            if k % 12 == 1:
                draft_round += 1
            draft_hash[draft_round].append(row[2][1:])
    # print(draft_hash)

first_pick = [1, 24, 25, 48, 49, 72, 73, 96, 97, 120, 121, 144, 145, 168, 169]

def gen_picks(num):
    i = 1
    picks = []
    while i < 169:
        # print("===")
        for j in range(1, 13):
            if j == num:
                picks.append(i)
            i += 1
            
        # print(i)
        k = 12
        while k > 0:
            if k == num:
                picks.append(i)
            i += 1
            k -= 1
        # print(i)
    # print(picks)
    return picks



def make_team_from_picks(numbers):
    draft = []
    play_pos = defaultdict(int)
    pts = 0
    i = 0
    rank = 0
    for num in numbers:
        draft.append(players[num - 1])
        rank += rank_hash[players[num - 1]]
        pts += ppg_hash[players[num - 1]]
        if i == 8:
            print(pts)
        i += 1
    print(f"{pts}: {rank / len(numbers)} : {draft}")

    for p in draft:
        pos = pos_hash[p]
        play_pos[pos] += 1
    print(play_pos)


    
def best_picks_per_round():
    maxx = -1
    pts = 0
    maxx_players = []
    pos_hash["NONE"] = "NONE"
    qbs = 2
    for k, v in draft_hash.items():
        maxx = -1
        maxx_player = "NONE"
        print(v)
        for p in v:
            if p in ppg_hash and ppg_hash[p] > maxx:
                if pos_hash[p] == "QB" and qbs == 0:
                    continue
                maxx = ppg_hash[p]
                maxx_player = p
        
        pts += maxx
        maxx_players.append(maxx_player)
        if pos_hash[maxx_player] == "QB":
            qbs -= 1
    
    print(pts)
    print(maxx_players)
    print(qbs)

if __name__ == "__main__":
    read_file("formatted_2021_stats.csv")
    read_draft_file("snake_draft.txt")
    # best_picks_per_round()
    # make_team_from_picks(first_pick)
    for i in range(1, 13):
        print(i)
        picks = gen_picks(i)
        make_team_from_picks(picks)
        print("=====")




# 1
# 144.29999999999998
# 195.49999999999997: 86.78571428571429 : ['Cooper Kupp', "Ja'Marr Chase", 'Najee Harris', 'Carson Wentz', 'Jimmy Garoppolo', 'Michael Pittman Jr.', 'DJ Moore', 'Christian Kirk', 'Rashaad Penny', 'Jarvis Landry', 'Sterling Shepard', 'Brandon Aiyuk', 'Cole Beasley', 'Devontae Booker']
# defaultdict(<class 'int'>, {'WR': 9, 'RB': 3, 'QB': 2})
# 
# 4th/5th round QBS = Jimmy G, Carr, Wentz
# 1, 2, 3 go for studs.  If you want top dollar TE it needs to be in rounds 3 or 4
# maybe round 6 TE for PITTS or Freiermuth