import sqlite3
import time
import os
import math


con = sqlite3.connect("wr.db")

with con:
    data = con.execute("SELECT * FROM WR_WEEKLY WHERE name == 'cooper kupp'")

readable_data = []
for row in data:
    print(row)
    readable_data.append(row)
    

weekly_points = []
for k, v in enumerate(readable_data[0]):
    if k == 0 or k == 1 or k == 20 or v == "-" or v == "BYE":
        continue
    val = float(v)
    weekly_points.append(val)
print(weekly_points)

# get mean
tot = 0
for w in weekly_points:
    tot += w
print(f"total = {tot}")
mean = tot / len(weekly_points)
print(f"mean = {mean}")

squared_sub = []
for w in weekly_points:
    sub = w - mean
    sub = sub * sub
    squared_sub.append(sub)
print(squared_sub)


# get mean of squared_sub
sq_tot = 0
for s in squared_sub:
    sq_tot += s
sq_mean = sq_tot / len(squared_sub)

final = math.sqrt(sq_mean)
print(final)



