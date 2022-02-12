"""
Compare stats of notable 49er QBs
Maybe even calculate their fantasy stats
"""

print("# Intro")
print('''What do the numbers say about 49er QBs of yesterday and today?"
    Below I have gathered the regular season and postseason stats of Montana, Young, Garcia, Smith, Kaepernick, and Garoppolo.<br /><br />'''
)
print("Using Python, I was able to sort and display the stats by using a print-to-markdown method...that's what you see in this README!")
print('''For regular season and postseason, QBS are graded based on completion percentage, win percentage, 
    net TDs per game, fantasy points per game, net yards per game, game winning drives per game, 
    yards per catch, turnovers per game, sacks per game'''
)
print("6 points goes to the best in the category and 1 point goes to worst in the category")
print("Young and Montana unfortunately do not have 1st down data until 1994 so I can't use that as a metric for the grade.  You'll see below that their 1st down data is skewed.")
print("Montana did have 170 net 1st downs when he played for the chiefs.  In Young's best recorded year he had 243 net 1st downs.")
print("<br /><br />")
print("Shoutout to Pro Football Reference for all of the data! https://www.pro-football-reference.com/.")
print("## TL;DR")
print("Montana is still the best! But there are definitely some interesting finds in the postseason stats")
print("Garoppolo fell off a cliff in the postseason and Kaepernick really came alive in his two postseason runs.")
print("Is there a data point thats missing? Is my grade scale fair?  Please let me know and I'd be happy to look and see if I can tweak it!")
print("# Data")

headers = "Year,Age,Tm,Pos,No.,G,GS,QBrec,Cmp,Att,Cmp%,Yds,TD,TD%,Int,Int%,1D,Lng,Y/A,AY/A,Y/C,Y/G,Rate,Sk,Yds,Sk%,NY/A,ANY/A,4QC,GWD,AV,Awards"
montana_career_data = "Career,Career,,,,192,164,117-47-0,3409,5391,63.2,40551,273,5.1,139,2.6,168,96,7.5,7.4,11.9,211.2,92.3,313,2095,5.5,6.74,6.60,26,28,166".split(",")
montana_rushing_career_data = "Career,Career,,,,192,164,457,1676,20,2,21,3.7,8.7,2.4,,,,,,,,,,,,457,3.7,1676,20,53".split(",")
montana_post_data = "Career,Career,,,23,23,16-7,460,734,62.7,5772,45,6.1,21,2.9,17,76,7.9,7.8,12.5,251.0,95.6,45,271,5.8,7.06,7.00,5,5".split(",")
montana_rushing_post_data = "Career,Career,,,23,23,63,314,2,0,53,5.0,13.7,2.7,,,,,,,,,,,,63,5.0,314,2,7".split(",")


young_career_data = "Career,Career,,,,169,143,94-49-0,2667,4149,64.3,33124,232,5.6,107,2.6,848,97,8.0,7.9,12.4,196.0,96.8,358,2055,7.9,6.89,6.85,13,16,168".split(",")
young_rushing_career_data = "Career,Career,,,,169,143,722,4239,43,126,49,5.9,25.1,4.3,2,2,2,1.0,0,0,6,0.0,0.0,100%,1.0,724,5.9,4241,43,68".split(",")
young_post_data = "Career,Career,,,22,14,8-6,292,471,62,3326,20,4.2,13,2.8,104,51,7.1,6.7,11.4,151.2,85.8,26,128,5.2,6.43,6.06,1,1".split(",")
young_rushing_post_data = "Career,Career,,,22,14,96,594,8,25,42,6.2,27.0,4.4,0,0,2,,0,0,2,0.0,0.1,100%,1.0,96,6.2,596,8,9".split(",")

garcia_career_data = "Career,Career,,,,125,116,58-58-0,2264,3676,61.6,25537,161,4.4,83,2.3,1239,99,6.9,6.8,11.3,204.3,87.5,,181,947,4.7,6.38,6.24,11,17,104".split(",")
garcia_rushing_career_data = "Career,Career,,,,125,116,468,2140,26,171,33,4.6,17.1,3.7,1,1,6,6.0,0,0,6,0.0,0.0,100.0%,6.0,469,4.6,2146,26,60".split(",")
garcia_post_data = "Career,Career,,,6,6,2-4,126,217,58.1,1357,7,3.2,7,3.2,68,76,6.3,5.4,10.8,226.2,73.8,10,69,4.4,5.67,4.90,1,2".split(",")
garcia_rushing_post_data = "Career,Career,,,6,6,18,88,1,8,14,4.9,14.7,3.0,,,,,,,,,,,,18,4.9,88,1,6".split(",")

smith_career_data = "Career,Career,,,,174,167,99-67-1,3250,5193,62.6,35650,199,3.8,109,2.1,1697,80,6.9,6.7,11.0,204.9,86.9,,432,2463,7.7,5.90,5.74,19,23,120".split(",")
smith_rushing_career_data = "Career,Career,,,,174,167,580,2604,15,168,70,4.5,15.0,3.3,3,3,-7,-2.3,0,0,3,0.0,0.0,100.0%,-2.3,583,4.5,2597,15,76".split(",")
smith_post_data = "Career,Career,,,7,7,2-5,156,253,61.7,1745,14,5.5,2,0.8,78,79,6.9,7.6,11.2,249.3,97.4,18,102,6.6,6.06,6.76,1,1".split(",")
smith_rushing_post_data = "Career,Career,,,7,7,35,220,1,15,28,6.3,31.4,5.0,,,,,,,,,,,,35,6.3,220,1,3".split(",")

kaepernick_career_data = "Career,Career,,,,69,58,28-30-0,1011,1692,59.8,12271,72,4.3,30,1.8,574,80,7.3,7.3,12.1,177.8,88.9,,171,1060,9.2,6.02,6.07,7,7,49".split(",")
kaepernick_rushing_career_data = "Career,Career,,,,69,58,375,2300,13,120,90,6.1,33.3,5.4,,,,,,,,,,,,375,6.1,2300,13,37".split(",")
kaepernick_post_data = "Career,Career,,,6,6,4-2,94,162,58,1374,7,4.3,5,3.1,66,45,8.5,8.0,14.6,229.0,87.3,11,58,6.4,7.61,7.12,2,2".split(",")
kaepernick_rushing_post_data = "Career,Career,,,6,6,51,507,4,24,58,9.9,84.5,8.5,,,,,,,,,,,,51,9.9,507,4,4".split(",")

garoppolo_career_data = "Career,Career,,,,63,47,33-14-0,960,1418,67.7,11852,71,5,38,2.7,566,83,8.4,8.2,12.3,188.1,98.9,,105,720,6.9,7.31,7.12,10,10,40".split(",")
garoppolo_rushing_career_data = "Career,Career,,,,63,47,142,192,5,40,13,1.4,3.0,2.3,2,2,-3,-1.5,0,0,3,0.0,0.0,100.0%,-1.5,144,1.3,189,5,27".split(",")
garoppolo_post_data = "Career,Career,,,7,6,4-2,80,132,60.6,962,4,3,6,4.5,55,44,7.3,5.8,12.0,137.4,74.1,8,51,5.7,6.51,5.15,0,1".split(",")
garoppolo_rushing_post_data = "Career,Career,,,7,6,12,6,0,2,4,0.5,0.9,1.7,,,,,,,,,,,,12,0.5,6,0,0".split(",")

career_yards = {}
career_tds = {}
career_comp_pct = {}
career_record = {}
career_win_pct = {}
career_ints = {}
career_sacks = {}
career_rating = {}
career_gwd = {}
career_rushing_yds = {}
career_rushing_tds = {}
career_fumbles = {}
career_ypc = {}
career_ypr = {}
career_att = {}
career_ypc = {}
def populate_dicts(name, data):
    career_yards[name] = int(data[11])
    career_tds[name] = int(data[12])
    career_comp_pct[name] = float(data[10])
    career_record[name] = data[7]
    record = data[7].split("-")
    career_win_pct[name] = float(int(record[0]) / int(record[1]))
    career_ints[name] = int(data[14])
    career_gwd[name] = int(data[-2])
    career_rating[name] = float(data[22])
    career_att[name] = int(data[9])
    career_ypc[name] = float(data[20])


post_pg_yards = {}
post_pg_tds = {}
post_pg_ints = {}
post_pg_fum = {}
post_pg_rush_tds = {}
post_pg_rush_yds = {}
post_pg_net_yds = {}
post_pg_net_tds = {}
post_pg_net_tos = {}
post_pg_sacks = {}
post_pg_fpts = {}
post_pg_net_1st = {}
post_win_pct = {}
post_comp_pct = {}
post_pg_gwd = {}
qb_grade_post = {}
post_pg_att = {}
post_ypc = {}
def populate_post_per_game_dicts(name, pdata, rdata):
    qb_grade_post[name] = 0
    post_pg_yards[name] = float(int(pdata[10])/int(pdata[5]))
    post_pg_tds[name] = float(int(pdata[11])/int(pdata[5]))
    post_pg_ints[name] = float(int(pdata[13])/int(pdata[5]))
    post_pg_rush_tds[name] = float(int(rdata[8]) / int(pdata[5]))
    post_pg_rush_yds[name] = float(int(rdata[7]) / int(pdata[5]))
    post_pg_fum[name] = float(int(rdata[-1])/int(pdata[5]))
    post_pg_att[name] = float(int(pdata[8])/int(pdata[5]))
    post_ypc[name] = float(pdata[19])

    post_pg_net_yds[name] = float((int(pdata[10]) + int(rdata[7])) / int(pdata[5]))
    post_pg_net_tds[name] = float((int(pdata[11]) + int(rdata[8])) / int(pdata[5]))
    post_pg_net_tos[name] = float((int(pdata[13]) + int(rdata[-1])) / int(pdata[5]))
    post_pg_net_1st[name] = float((int(pdata[15]) + int(rdata[9])) / int(pdata[5]))
    post_pg_sacks[name] = float(int(pdata[22]) / int(pdata[5]))
    post_pg_gwd[name] = float(int(pdata[-1]) / int(pdata[5]))


    post_record = pdata[6].split("-")
    post_win_pct[name] = float(int(post_record[0]) / int(post_record[1]))
    post_comp_pct[name] = float(pdata[9])
    



qb_grade_career = {}
pg_yards = {}
pg_tds = {}
pg_ints = {}
pg_fum = {}
pg_rush_tds = {}
pg_rush_yds = {}
pg_net_yds = {}
pg_net_tds = {}
pg_net_tos = {}
pg_net_1st = {}
pg_sacks = {}
pg_fpts = {}
pg_1st = {}
pg_gwd = {}
pg_att = {}
def populate_per_game_dicts(name, pdata, rdata):
    pg_fpts[name] = 0
    qb_grade_career[name] = 0
    pg_yards[name] = float(int(pdata[11])/int(pdata[6]))
    pg_tds[name] = float(int(pdata[12])/int(pdata[6]))
    pg_ints[name] = float(int(pdata[14])/int(pdata[6]))
    pg_rush_tds[name] = float(int(rdata[9]) / int(pdata[6]))
    pg_rush_yds[name] = float(int(rdata[8]) / int(pdata[6]))
    pg_fum[name] = float(int(rdata[-1])/int(pdata[6]))
    pg_gwd[name] = float(int(pdata[-2])/int(pdata[6]))
    pg_att[name] = float(int(pdata[9])/int(pdata[6]))

    pg_net_yds[name] = float((int(pdata[11]) + int(rdata[8])) / int(pdata[6]))
    pg_net_tds[name] = float((int(pdata[12]) + int(rdata[9])) / int(pdata[6]))
    pg_net_tos[name] = float((int(pdata[14]) + int(rdata[-1])) / int(pdata[6]))
    pg_net_1st[name] = float((int(pdata[16]) + int(rdata[10])) / int(pdata[6]))
    
    if name == "Montana" or name == "Young":
        pg_sacks[name] = float(int(pdata[23]) / int(pdata[6]))
    else:
        pg_sacks[name] = float(int(pdata[24]) / int(pdata[6]))

    pg_fpts[name] += float(pg_tds[name] * 4)
    pg_fpts[name] += float(pg_rush_tds[name] * 6)
    pg_fpts[name] += float(pg_yards[name] / 25)
    pg_fpts[name] += float(pg_rush_yds[name] / 10)
    pg_fpts[name] += float(pg_ints[name] * -1)
    pg_fpts[name] += float(pg_sacks[name] * -1)
    pg_fpts[name] += float(pg_fum[name] * -2)




def print_data(stat_dict, stat_title):
    print(f"### {stat_title}")
    stat_dict = {k: v for k, v in sorted(stat_dict.items(), reverse=True, key=lambda item: item[1])}
    for k, v in stat_dict.items():
        print(f"{k} : {v}<br />")

def print_negative_data(stat_dict, stat_title, qb_grade):
    print(f"### {stat_title}")
    stat_dict = {k: v for k, v in sorted(stat_dict.items(), reverse=True, key=lambda item: item[1])}
    vals = 1
    for k, v in stat_dict.items():
        qb_grade[k] += vals
        vals += 1
        print(f"{k} : {v}<br />")

def print_positive_data(stat_dict, stat_title, qb_grade):
    print(f"### {stat_title}")
    stat_dict = {k: v for k, v in sorted(stat_dict.items(), reverse=True, key=lambda item: item[1])}
    vals = 6
    prev_val = -99
    for k, v in stat_dict.items():
        qb_grade[k] += vals
        if prev_val != v:
            vals -= 1
        prev_val = v
        print(f"{k} : {v}<br />")


populate_dicts("Montana", montana_career_data)
populate_dicts("Young", young_career_data)
populate_dicts("Garcia", garcia_career_data)
populate_dicts("Smith", smith_career_data)
populate_dicts("Kaepernick", kaepernick_career_data)
populate_dicts("Garoppolo", garoppolo_career_data)

populate_per_game_dicts("Montana", montana_career_data, montana_rushing_career_data)
populate_per_game_dicts("Young", young_career_data, young_rushing_career_data)
populate_per_game_dicts("Garcia", garcia_career_data, garcia_rushing_career_data)
populate_per_game_dicts("Smith", smith_career_data, smith_rushing_career_data)
populate_per_game_dicts("Kaepernick", kaepernick_career_data, kaepernick_rushing_career_data)
populate_per_game_dicts("Garoppolo", garoppolo_career_data, garoppolo_rushing_career_data)

populate_post_per_game_dicts("Montana", montana_post_data, montana_rushing_post_data)
populate_post_per_game_dicts("Young", young_post_data, young_rushing_post_data)
populate_post_per_game_dicts("Garcia", garcia_post_data, garcia_rushing_post_data)
populate_post_per_game_dicts("Smith", smith_post_data, smith_rushing_post_data)
populate_post_per_game_dicts("Kaepernick", kaepernick_post_data, kaepernick_rushing_post_data)
populate_post_per_game_dicts("Garoppolo", garoppolo_post_data, garoppolo_rushing_post_data)

print("## REGULAR SEASON CAREER STATS")
print("### CAREER PASSING YARDS")
career_yards = {k: v for k, v in sorted(career_yards.items(), reverse=True, key=lambda item: item[1])}
for k, v in career_yards.items():
    print(f"{k} : {v}<br />")

print_data(career_att, "CAREER PASSING ATTEMPTS")
print_positive_data(career_ypc, "YARDS PER CATCH", qb_grade_career)
print("### CAREER PASSING TDS")
career_tds = {k: v for k, v in sorted(career_tds.items(), reverse=True, key=lambda item: item[1])}
for k, v in career_tds.items():
    print(f"{k} : {v}<br />")

print_positive_data(career_comp_pct, "CAREER COMPLETION PERCENTAGE", qb_grade_career)
print_positive_data(career_win_pct, "CAREER WIN PERCENTAGE", qb_grade_career)

print("### CAREER RECORD")
for k, v in career_record.items():
    print(f"{k} : {v}<br />")

print_data(career_gwd, "CAREER GWD")
print_data(career_rating, "CAREER RATING")

print("## REGULAR SEASON PER GAME STATS")
print_data(pg_yards, "PASSING YARDS PER GAME")
print_data(pg_att, "PASSING ATTEMPTS PER GAME")
print_data(pg_tds, "PASSING TDS PER GAME")
print_data(pg_rush_yds, "RUSHING YARDS PER GAME")
print_positive_data(pg_gwd, "GAME WINNING DRIVES PER GAME", qb_grade_career)
print_positive_data(pg_fpts, "FPTS PER GAME (using superflex rules)", qb_grade_career)
print_data(pg_ints, "INTS PER GAME")
print_negative_data(pg_sacks, "SACKS PER GAME", qb_grade_career)

print("## REGULAR SEASON NET PER GAME (net meaning rushing/passing or fumble/int)")
print_positive_data(pg_net_yds, "NET YARDS PER GAME", qb_grade_career)
print_positive_data(pg_net_tds, "NET TDS PER GAME", qb_grade_career)
print_negative_data(pg_net_tos, "NET TURNOVERS PER GAME", qb_grade_career)
print_data(pg_net_1st, "NET FIRST DOWNS PER GAME")
print_data(qb_grade_career, "QB PER GAME REGULAR SEASON GRADE")
print("## POSTSEASON PER GAME STATS")
print_data(post_pg_yards, "PASSING YARDS PER GAME")
print_data(post_pg_tds, "PASSING TDS PER GAME")
print_data(post_pg_ints, "INTS PER GAME")
print_negative_data(post_pg_sacks, "SACKS PER GAME", qb_grade_post)
print_positive_data(post_comp_pct, "COMPLETION PERCENTAGE", qb_grade_post)
print_positive_data(post_win_pct, "WIN PERCENTAGE", qb_grade_post)
print_positive_data(post_pg_gwd, "GAME WINNING DRIVES PER GAME", qb_grade_post)
print_positive_data(post_ypc, "YARDS PER CATCH", qb_grade_post)
print("## POSTSEASON NET PER GAME STATS")
print_positive_data(post_pg_net_yds, "NET YARDS PER GAME", qb_grade_post)
print_data(post_pg_net_1st, "NET FIRST DOWNS PER GAME")
print_positive_data(post_pg_net_tds, "NET TDS PER GAME", qb_grade_post)
print_negative_data(post_pg_net_tos, "NET TURNOVERS PER GAME", qb_grade_post)

print_data(qb_grade_post, "QB PER GAME POSTSEASON GRADE")
qb_grade_total = {}
for k, v in qb_grade_career.items():
    qb_grade_total[k] = qb_grade_post[k] + qb_grade_career[k]
print_data(qb_grade_total, "QB PER GAME TOTAL (REGULAR SEASON + POSTSEASON) GRADE")