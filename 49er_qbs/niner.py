



"""
Compare stats of notable 49er QBs
Maybe even calculate their fantasy stats
"""

headers = "Year,Age,Tm,Pos,No.,G,GS,QBrec,Cmp,Att,Cmp%,Yds,TD,TD%,Int,Int%,1D,Lng,Y/A,AY/A,Y/C,Y/G,Rate,Sk,Yds,Sk%,NY/A,ANY/A,4QC,GWD,AV,Awards"
montana_career_stats = "Career,Career,,,,192,164,117-47-0,3409,5391,63.2,40551,273,5.1,139,2.6,168,96,7.5,7.4,11.9,211.2,92.3,313,2095,5.5,6.74,6.60,26,28,166"
montana_post_stats = "Career,Career,,,23,23,16-7,460,734,62.7,5772,45,6.1,21,2.9,17,76,7.9,7.8,12.5,251.0,95.6,45,271,5.8,7.06,7.00,5,5"
montana_career_data = montana_career_stats.split(",")

young_career_stats = "Career,Career,,,,169,143,94-49-0,2667,4149,64.3,33124,232,5.6,107,2.6,848,97,8.0,7.9,12.4,196.0,96.8,358,2055,7.9,6.89,6.85,13,16,168"
young_career_data = young_career_stats.split(",")

garcia_career_stats = "Career,Career,,,,125,116,58-58-0,2264,3676,61.6,25537,161,4.4,83,2.3,1239,99,6.9,6.8,11.3,204.3,87.5,,181,947,4.7,6.38,6.24,11,17,104,"
garcia_career_data = garcia_career_stats.split(",")

smith_career_stats = "Career,Career,,,,174,167,99-67-1,3250,5193,62.6,35650,199,3.8,109,2.1,1697,80,6.9,6.7,11.0,204.9,86.9,,432,2463,7.7,5.90,5.74,19,23,120,"
smith_career_data = smith_career_stats.split(",")

kaepernick_career_stats = "Career,Career,,,,69,58,28-30-0,1011,1692,59.8,12271,72,4.3,30,1.8,574,80,7.3,7.3,12.1,177.8,88.9,,171,1060,9.2,6.02,6.07,7,7,49"
kaepernick_career_data = kaepernick_career_stats.split(",")

garoppolo_career_data = "Career,Career,,,,63,47,33-14-0,960,1418,67.7,11852,71,5,38,2.7,566,83,8.4,8.2,12.3,188.1,98.9,,105,720,6.9,7.31,7.12,10,10,40".split(",")


career_yards = {}
career_tds = {}
career_comp_pct = {}
career_record = {}
career_win_pct = {}
career_ints = {}
def populate_dicts(name, data):
    career_yards[name] = int(data[11])
    career_tds[name] = int(data[12])
    career_comp_pct[name] = float(data[10])
    career_record[name] = data[7]
    record = data[7].split("-")
    career_win_pct[name] = float(int(record[0]) / int(record[1]))
    career_ints[name] = int(data[14])


pg_yards = {}
pg_tds = {}
pg_ints = {}
def populate_per_game_dicts(name, data):
    pg_yards[name] = int(data[11])/int(data[6])
    pg_tds[name] = int(data[12])/int(data[6])
    pg_ints[name] = int(data[14])/int(data[6])


def print_data(stat_dict, stat_title):
    print(stat_title)
    stat_dict = {k: v for k, v in sorted(stat_dict.items(), reverse=True, key=lambda item: item[1])}
    for k, v in stat_dict.items():
        print(f"{k} : {v}")
    print("================")


populate_dicts("Montana", montana_career_data)
populate_dicts("Young", young_career_data)
populate_dicts("Garcia", garcia_career_data)
populate_dicts("Smith", smith_career_data)
populate_dicts("Kaepernick", kaepernick_career_data)
populate_dicts("Garoppolo", garoppolo_career_data)

populate_per_game_dicts("Montana", montana_career_data)
populate_per_game_dicts("Young", young_career_data)
populate_per_game_dicts("Garcia", garcia_career_data)
populate_per_game_dicts("Smith", smith_career_data)
populate_per_game_dicts("Kaepernick", kaepernick_career_data)
populate_per_game_dicts("Garoppolo", garoppolo_career_data)

print("REGULAR SEASON PASSING CAREER STATS")
print("CAREER YARDS")
career_yards = {k: v for k, v in sorted(career_yards.items(), reverse=True, key=lambda item: item[1])}
for k, v in career_yards.items():
    print(f"{k} : {v}")
print("================")

print("CAREER TDS")
career_tds = {k: v for k, v in sorted(career_tds.items(), reverse=True, key=lambda item: item[1])}
for k, v in career_tds.items():
    print(f"{k} : {v}")
print("================")

print("CAREER COMPLETION PERCENTAGE")
career_comp_pct = {k: v for k, v in sorted(career_comp_pct.items(), reverse=True, key=lambda item: item[1])}
for k, v in career_comp_pct.items():
    print(f"{k} : {v}")
print("================")

print("CAREER WIN PERCENTAGE")
career_win_pct = {k: v for k, v in sorted(career_win_pct.items(), reverse=True, key=lambda item: item[1])}
for k, v in career_win_pct.items():
    print(f"{k} : {v}")
print("================")

print("CAREER RECORD")
# career_yards = {k: v for k, v in sorted(career_yards.items(), reverse=True, key=lambda item: item[1])}
for k, v in career_record.items():
    print(f"{k} : {v}")
print("================")
print("")
print("======")
print("PER GAME STATS")
print("======")
print_data(pg_yards, "PASSING YARDS PER GAME")
print_data(pg_tds, "TDS PER GAME")
print_data(pg_ints, "INTS PER GAME")