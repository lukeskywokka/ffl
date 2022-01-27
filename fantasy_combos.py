from typing import NamedTuple
import csv

# site link: https://www.fantasypros.com/nfl/stats/dst.php?scoring=PPR&range=custom&start_week=15&end_week=17


player_hash = {
    "Stefon Diggs": {"pos": "WR", "team": "Bills", "ppr_pts": 262.4, "pos_rank": 7, "overall_rank": 23}
}

print(player_hash)
print(player_hash["Stefon Diggs"])

luke_team_17 = ["Tyler Huntley (BAL)", "Najee Harris (PIT)", "Ronald Jones II (TB)", "Stefon Diggs (BUF)", "A.J. Brown (TEN)", "Mark Andrews (BAL)", "Sony Michel (LAR)", "Trey Lance (SF)", "Bears", "Greg Joseph (MIN)"]
luke_team_16 = ["Kirk Cousins (MIN)", "Najee Harris (PIT)", "Jeff Wilson Jr. (SF)", "Stefon Diggs (BUF)", "A.J. Brown (TEN)", "Mark Andrews (BAL)", "Russell Gage (ATL)", "Devante Parker (MIA)", "Broncos", "Greg Joseph (MIN)"]
luke_team_15 = ["Kirk Cousins (MIN)", "Najee Harris (PIT)", "Jeff Wilson Jr. (SF)", "Stefon Diggs (BUF)", "Devante Parker (MIA)", "Mark Andrews (BAL)", "Rashaad Penny (SEA)", "Terry McLaurin (WAS)", "Broncos", "Greg Joseph (MIN)"]
evan_team = ["Josh Allen (BUF)", "Austin Ekeler (LAC)", "Rex Burkhead (HOU)", "Hunter Renfrow (LV)", "Keenan Allen (LAC)", "Tyler Higbee (LAR)", "Michael Pittman Jr. (IND)", "Matthew Stafford (LAR)", "Tampa Bay", "Daniel Carlson (LV)"]
moderna_team = ["Joe Burrow (CIN)", "Dalvin Cook (MIN)", "Dare Ogunbowale (JAC)", "Cooper Kupp (LAR)", "Justin Jefferson (MIN)", "Zach Ertz (ARI)", "Jaylen Waddle (MIA)", "Jaret Patterson (WAS)", "Tua Tagovailoa (MIA)", "Bears", "Chris Boswell (PIT)"]
nina_team = ["Aaron Rodgers (GB)", "Tee Higgins (CIN)", "Brandin Cooks (HOU)", "Josh Jacobs (LV)", "Jonathan Taylor (IND)", "George Kittle (SF)", "Rashaad Penny (SEA)", "Bears", "Brandon McManus (DEN)"]
luke_what_if = ["Taysom Hill (NO)", "Najee Harris (PIT)", "Rashaad Penny (SEA)", "Stefon Diggs (BUF)", "A.J. Brown (TEN)", "Mark Andrews (BAL)", "Sony Michel (LAR)", "Trey Lance (SF)", "Bears", "Greg Joseph (MIN)"]
all_teams = []

for p in luke_team:
    all_teams.append(p)

for p in evan_team:
    all_teams.append(p)

for p in moderna_team:
    all_teams.append(p)

for p in nina_team:
    all_teams.append(p)

for p in luke_what_if:
    all_teams.append(p)

print(all_teams)

def read_file(filename, team):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        for p in team:
            if p in row and row not in rows:
                rows.append(row)
    for r in rows:
        print(r)
    the_file.close()
    print ("=============================")
    return rows

week17qb = read_file("", luke_team_17)




# QBs
qb_15_thru_17_file = open("weeks_15_thru_17_FantasyPros_Fantasy_Football_Statistics_QB.csv")
csvreader = csv.reader(qb_15_thru_17_file)
header = next(csvreader)
print(header)
qb_week_15_thru_17_rows = []
for row in csvreader:
    for p in all_teams:
        if p in row and row not in qb_week_15_thru_17_rows:
            qb_week_15_thru_17_rows.append(row)
for r in qb_week_15_thru_17_rows:
    print(r)
qb_15_thru_17_file.close()
print ("=============================")

# RBs
rb_15_thru_17_file = open("weeks_15_thru_17_FantasyPros_Fantasy_Football_Statistics_RB.csv")
csvreader = csv.reader(rb_15_thru_17_file)
header = next(csvreader)
print(header)
rb_week_15_thru_17_rows = []
for row in csvreader:
    for p in all_teams:
        if p in row and row not in rb_week_15_thru_17_rows:
            rb_week_15_thru_17_rows.append(row)
for r in rb_week_15_thru_17_rows:
    print(r)
rb_15_thru_17_file.close()
print("=========================")

# WRs
wr_15_thru_17_file = open("weeks_15_thru_17_FantasyPros_Fantasy_Football_Statistics_WR.csv")
csvreader = csv.reader(wr_15_thru_17_file)
header = next(csvreader)
print(header)
wr_week_15_thru_17_rows = []
for row in csvreader:
    for p in all_teams:
        if p in row and row not in wr_week_15_thru_17_rows:
            wr_week_15_thru_17_rows.append(row)
for r in wr_week_15_thru_17_rows:
    print(r)
wr_15_thru_17_file.close()
print ("=============================")

# TEs
te_15_thru_17_file = open("weeks_15_thru_17_FantasyPros_Fantasy_Football_Statistics_TE.csv")
csvreader = csv.reader(te_15_thru_17_file)
header = next(csvreader)
print(header)
te_week_15_thru_17_rows = []
for row in csvreader:
    for p in all_teams:
        if p in row and row not in te_week_15_thru_17_rows:
            te_week_15_thru_17_rows.append(row)
for r in te_week_15_thru_17_rows:
    print(r)
te_15_thru_17_file.close()
print ("=============================")

# Ks
k_15_thru_17_file = open("weeks_15_thru_17_FantasyPros_Fantasy_Football_Statistics_K.csv")
csvreader = csv.reader(k_15_thru_17_file)
header = next(csvreader)
print(header)
k_week_15_thru_17_rows = []
for row in csvreader:
    for p in all_teams:
        if p in row and row not in k_week_15_thru_17_rows:
            k_week_15_thru_17_rows.append(row)
for r in k_week_15_thru_17_rows:
    print(r)
k_15_thru_17_file.close()
print ("=============================")

# DSTs
dst_15_thru_17_file = open("weeks_15_thru_17_FantasyPros_Fantasy_Football_Statistics_DST.csv")
csvreader = csv.reader(dst_15_thru_17_file)
header = next(csvreader)
print(header)
dst_week_15_thru_17_rows = []
for row in csvreader:
    for p in all_teams:
        if len(row) > 1 and p in row[1] and row not in dst_week_15_thru_17_rows:
            dst_week_15_thru_17_rows.append(row)
for r in dst_week_15_thru_17_rows:
    print(r)
dst_15_thru_17_file.close()
print ("=============================")

all_rows = qb_week_15_thru_17_rows + rb_week_15_thru_17_rows + wr_week_15_thru_17_rows + te_week_15_thru_17_rows + k_week_15_thru_17_rows + dst_week_15_thru_17_rows
#print(all_rows)

print("======")
print("Luke's 15-17 rating:")
luke_sum_player_ranking = 0
for p in all_rows:
    if p[1] in luke_team:
        luke_sum_player_ranking += int(p[0])
luke_avg_rating = luke_sum_player_ranking / len(luke_team)
print(luke_sum_player_ranking)
print(luke_avg_rating)
print("==============")

print("Evan's 15-17 rating")
evan_sum_player_ranking = 0
for p in all_rows:
    if p[1] in evan_team:
        evan_sum_player_ranking += int(p[0])
evan_avg_rating = evan_sum_player_ranking / len(evan_team)
print(evan_sum_player_ranking)
print(evan_avg_rating)
print("===============")

print("Moderna's 15-17 rating")
moderna_sum_player_ranking = 0
for p in all_rows:
    if p[1] in moderna_team:
        moderna_sum_player_ranking += int(p[0])
moderna_avg_rating = moderna_sum_player_ranking / len(moderna_team)
print(moderna_sum_player_ranking)
print(moderna_avg_rating)
print("===============")

print("Nina's 15-17 rating")
nina_sum_player_ranking = 0
for p in all_rows:
    if p[1] in nina_team:
        nina_sum_player_ranking += int(p[0])
nina_avg_rating = nina_sum_player_ranking / len(nina_team)
print(nina_sum_player_ranking)
print(nina_avg_rating)
print("===============")

print("Luke's what-if rating")
lwi_sum_player_ranking = 0
for p in all_rows:
    if p[1] in luke_what_if:
        lwi_sum_player_ranking += int(p[0])
lwi_avg_rating = lwi_sum_player_ranking / len(luke_what_if)
print(lwi_sum_player_ranking)
print(lwi_avg_rating)
print("===============")



r = ["a"]
b = ["b"]
print(r + b)

