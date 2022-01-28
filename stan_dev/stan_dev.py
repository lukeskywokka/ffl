import sqlite3
import time
import os
import math
from collections import OrderedDict

con = sqlite3.connect("wr.db")

def get_points(data):
    weekly_points = []
    for k, v in enumerate(data):
        if k == 0 or k == 1 or k == 20 or v == "-" or v == "BYE" or v == "OUT":
            continue
        val = float(v)
        weekly_points.append(val)
    #print(weekly_points)
    return weekly_points

# get mean
def get_mean(points):
    tot = 0
    for w in points:
        tot += w
    
    if len(points) == 0:
        return -1
    #print(f"total = {tot}")
    mean = tot / len(points)
    print(f"mean = {mean}")
    return mean

def sub_and_square(points, mean):
    squared_sub = []
    for w in points:
        sub = w - mean
        sub = sub * sub
        squared_sub.append(sub)
    #print(squared_sub)
    return squared_sub

with con:
    # data = con.execute("SELECT * FROM WR_WEEKLY WHERE name == 'cooper kupp'")
    data = con.execute("SELECT * FROM WR_WEEKLY")


std_hash = {}
avg_hash = {}
for k, v in enumerate(data):
    if k == 0:
        continue
    print(v)
    points = get_points(v)
    mean = get_mean(points)
    if mean == -1:
        continue
    avg_hash[v[1]] = mean
    sub = sub_and_square(points, mean)
    mean = get_mean(sub)
    final = math.sqrt(mean)
    print(final)
    std_hash[final] = v[1]
    #print("====")

# sort by key
ordered = OrderedDict(sorted(std_hash.items()))
dev_hash = {}
for k, v in ordered.items():
    print(f"{v} : {avg_hash[v] - k}")
    dev_hash[avg_hash[v] - k] = v


dev_hash = OrderedDict(sorted(dev_hash.items()))
for k, v in dev_hash.items():
    print(f"{v} : {k}")


# get mean of squared_sub
# sq_tot = 0
# for s in squared_sub:
#     sq_tot += s
# sq_mean = sq_tot / len(squared_sub)

# final = math.sqrt(sq_mean)
# print(final)



