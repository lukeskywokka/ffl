# best play per team
# most in category
# most successful in category
# most ran run play per team
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
        
    


print("rank, team, attempts, yards, pct of plays")
get_most_in_category("right end", "re.csv")
get_most_in_category("right tackle", "rt.csv")
get_most_in_category("right guard", "rg.csv")
get_most_in_category("center", "c.csv")
get_most_in_category("left guard", "lg.csv")
get_most_in_category("left tackle", "lt.csv")
get_most_in_category("left end", "le.csv")
print("======")

populate_dict(["re.csv", "rt.csv", "rg.csv", "c.csv", "lg.csv", "lt.csv", "le.csv"])
most_attempted_play_per_team()