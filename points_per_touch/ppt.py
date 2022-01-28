import csv
import sys

# TDOD: draft ranking
# pts per completion for QBs
# avg rank for drafted players
# avg ppg for drafted players

# most dominant drafted team standard PPR: 
# sixth pick
# 1.JT, 2.Kupp, 3.Andrews, 4.Josh Allen, 
# 5.Ja'Marr Chase, 6.Lenny, 7.Deebo, 8.Brandin Cooks
# 9. Michael Carter Jr/Dillon/Mooney., 10. James Conner, 11. Cordarrelle, 12. Michael Pittman Jr.
# 13. Hunter Renfrow, 14. Cowboys D, 15. Nick Folk
jt = 360.6
kupp = 412.9
Andrews = 284.6
Allen = 378.72
Chase = 300
Lenny = 255.6
Deebo = 310
Cooks = 226.2
Carter = 152.5
Conner = 230.4
Cordarrelle = 232.4
Pitt = 218.2
Renfrow = 242.2
Cowboys = 180
Folk = 164

stud_team_total_points = jt + kupp + Andrews + Allen + Chase + Lenny + Deebo + Cooks + Carter + Conner + Cordarrelle + Pitt + Renfrow + Cowboys + Folk
print(stud_team_total_points)
starters = jt + kupp + Andrews + Allen + Chase + Lenny + Deebo + Cowboys + Folk
print(starters)
print(f"points per week = {starters/16}")

# John's Superflex superteam: qb, 2rb, 2wr, te, wt, wrt, wrt, qwrt, d, k
superflex_john = ["Jonathan Taylor", "Najee Harris", "Justin Jefferson", "Matthew Stafford", "Cooper Kupp", "Kirk Cousins", "Ja'Marr Chase", "Deebo Samuel", "Mark Andrews", "Jaylen Waddle", ]

#sys.exit(1)



CMAC_ppt_2019 = 1.169
MT_ppt_2019 = 2.497
TYREEK_ppt_2017 = 2.6
TYREEK_ppt_2018 = 3.009
TYREEK_ppt_2019 = 2.85
TYREEK_ppt_2020 = 3.289

def read_file(filename):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    ppt_hash = {}
    for row in csvreader:
        #print(row)
        if len(row) > 2 and int(row[2]) != 0 and int(row[3]) >= 50:
            ppt = float(row[14])/(int(row[2]) + int(row[9]))
            ppt_hash[row[1]] = ppt
            #print(ppt)
        #print("====")
    the_file.close()
    print ("=============================")
    return ppt_hash

def read_rb_file(filename):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    ppt_hash = {}
    for row in csvreader:
        #print(row)
        if len(row) > 2 and int(row[2]) != 0:
            res = row[3].replace(",", "")
            if int(res) > 200:
                ppt = float(row[15])/(int(row[2]) + int(row[8]))
                ppt_hash[row[1]] = ppt
                #print(ppt)
        #print("====")
    the_file.close()
    print ("=============================")
    return ppt_hash

def read_qb_file(filename):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    ppt_hash = {}
    for row in csvreader:
        #print(row)
        if len(row) > 2 and int(row[2]) != 0:
            ppt = float(row[15])/(int(row[2]) + int(row[10]))
            ppt_hash[row[1]] = ppt
            #print(ppt)
        #print("====")
    the_file.close()
    print ("=============================")
    return ppt_hash

def read_te_file(filename):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    ppt_hash = {}
    for row in csvreader:
        #print(row)
        if len(row) > 2 and int(row[2]) != 0 and int(row[3]) > 20:
            ppt = float(row[14])/(int(row[2]) + int(row[9]))
            ppt_hash[row[1]] = ppt
            #print(ppt)
        #print("====")
    the_file.close()
    print ("=============================")
    return ppt_hash


wr_hash = read_file("wr_full_year.csv")
rb_hash = read_rb_file("rb_full_year.csv")
qb_hash = read_qb_file("qb_full_year.csv")
te_hash = read_te_file("te_full_year.csv")
print(qb_hash)
# print(rb_hash)
# print(wr_hash)


# WRs
ret = sorted(wr_hash.items(), key=lambda x: x[1], reverse=True)
i = 1
for r in ret:
    print(f"{i}: {r}")
    i += 1
print("====")
print("====")

# RBs
ret = sorted(rb_hash.items(), key=lambda x: x[1], reverse=True)
i = 1
for r in ret:
    print(f"{i}: {r}")
    i += 1
print("====")
print("====")

# QBs
ret = sorted(qb_hash.items(), key=lambda x: x[1], reverse=True)
i = 1
for r in ret:
    print(f"{i}: {r}")
    i += 1
print("====")
print("====")

# TEs
ret = sorted(te_hash.items(), key=lambda x: x[1], reverse=True)
i = 1
for r in ret:
    print(f"{i}: {r}")
    i += 1
print("====")
print("====")






# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# print(x)
