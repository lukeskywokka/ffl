# best play per team
# most in category
# most successful in category
# most efficient run team
# most efficient run type per team
# most popular play per team


import csv
from collections import defaultdict


def get_most_in_category(runtype, filename):
    print(f"Most runs towards {runtype}")
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    for k, row in enumerate(csvreader):
        if k == 0:
            continue
        if row:
            row = row[0].split("\t")
        print(row)
        print("==")
        the_file.close()
        break





run_plays = defaultdict(list)
run_types = {}
run_types["le.csv"] = "Left End"
run_types["lt.csv"] = "Left Tackle"
run_types["lg.csv"] = "Left Guard"
run_types["c.csv"]  = "Center"
run_types["rg.csv"] = "Right Guard"
run_types["rt.csv"] = "Right Tackle"
run_types["re.csv"] = "Right End"

def populate_dict(files):
    for f in files:
        the_file = open(f)
        csvreader = csv.reader(the_file)
        header = next(csvreader)
        for k, row in enumerate(csvreader):
            if k == 0:
                continue
            if row:
                row = row[0].split("\t")
                run_plays[row[1]].append(row + [run_types[f]])
        the_file.close()
    
    
def get_team_plays(team):
    plays = run_plays[team]
    for p in plays:
        ypc = int(p[3]) / int(p[2])
        p = [ypc] + p
        print(p)


def get_all_team_plays():
    print("## All Team Running Plays")
    print("TEAM, YPC, ATTEMPTS RANK, TEAM, ATT, YARDS, PERCENT OF TOTAL PLAYS, RUN TYPE")
    for k, plays in run_plays.items():
        print(k)
        for p in plays:
            ypc = int(p[3]) / int(p[2])
            p = [ypc] + p
            print(p)
        print("---")
    


def most_attempted_play_per_team():
    print(f"Most attempted run type per team")
    print("rank, team, attempts, yards, pct of plays, run type")
    for k, v in run_plays.items():
        great = [0, 0, "0", 0, 0]
        for i in v:
            if i[2] > great[2]:
                great = i
        print(great)
        print("===")


def most_efficient_run_play_per_team():
    print(f"## Most efficient run type per team")
    print("TEAM, YPC, ATTEMPTS RANK, TEAM, ATT, YARDS, PERCENT OF TOTAL PLAYS, RUN TYPE")
    ypc_hash = {}
    for k, v in run_plays.items():
        great = []
        great_check = 0
        for i in v:
            ypc = int(i[3]) / int(i[2])
            if ypc > great_check:
                great_check = ypc
                great = i
        ypc_hash[great[1]] = [great_check, great]
        # print(f"{great[1]} : {great_check} : {great[5]}")
        # print("===")
    
    ypc_hash = dict(sorted(ypc_hash.items(), reverse=True, key=lambda item: item[1]))
    for k, v in ypc_hash.items():
        print(f"{k} : {v}")

    

def most_efficient_run_team():
    print("## Most efficient run team")
    print("TEAM, YPC, ATT, YARDS")
    eff_hash = {}
    for k, v in run_plays.items():
        att = 0
        yds = 0
        for i in v:
            att += int(i[2])
            yds += int(i[3])
        
        eff_hash[k] = [yds / att, att, yds]
        # print(f"{great[1]} : {great_check} : {great[5]}")
        # print("===")
    
    eff_hash = dict(sorted(eff_hash.items(), reverse=True, key=lambda item: item[1]))
    for k, v in eff_hash.items():
        print(f"{k} : {v}")
        
    

print("# Plays and their efficiency")
print("""Below I have compield the data for: """)
print("- most efficient run team: ie most yards per carry (ypc)")
print("- most efficient run type per team")
print("- all run plays per team")
print("<br />")
print("Eventually I will get to the passing plays.")
print("---")
# 
# print("rank, team, attempts, yards, pct of plays")
# get_most_in_category("right end", "re.csv")
# get_most_in_category("right tackle", "rt.csv")
# get_most_in_category("right guard", "rg.csv")
# get_most_in_category("center", "c.csv")
# get_most_in_category("left guard", "lg.csv")
# get_most_in_category("left tackle", "lt.csv")
# get_most_in_category("left end", "le.csv")
# print("======")

populate_dict(["re.csv", "rt.csv", "rg.csv", "c.csv", "lg.csv", "lt.csv", "le.csv"])
print("---")
most_efficient_run_team()
print("---")
most_efficient_run_play_per_team()
print("---")
get_all_team_plays()
print("---")