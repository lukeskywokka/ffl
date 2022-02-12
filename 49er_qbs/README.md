# Intro
What do the numbers say about 49er QBs of yesterday and today?"
    Below I have gathered the regular season and postseason stats of Montana, Young, Garcia, Smith, Kaepernick, and Garoppolo.
Using Python, I was able to sort and display the stats by using a print-to-markdown method...that's what you see in this README!
Shoutout to Pro Football Reference for all of the data! https://www.pro-football-reference.com/
For regular season and postseason, QBS are graded based on completion percentage, win percentage, 
    net TDs per game, fantasy points per game, net yards per game, game winning drives per game, 
    yards per catch, turnovers per game, sacks per game
6 points goes to the best in the category and 1 point goes to worst in the category
Young and Montana unfortunately do not have 1st down data until 1994 so I can't use that as a metric for the grade.  You'll see below that their 1st down data is skewed.
Montana did have 170 net 1st downs when he played for the chiefs.  In Young's best recorded year he had 243 net 1st downs.
## TL;DR
Montana is still the best! But there are definitely some interesting finds in the postseason stats
Is there a data point thats missing? Is my grade scale fair?  Please let me know and I'd be happy to look and see if I can tweak it!
# Data
## REGULAR SEASON CAREER STATS
### CAREER PASSING YARDS
Montana : 40551
Smith : 35650
Young : 33124
Garcia : 25537
Kaepernick : 12271
Garoppolo : 11852
### CAREER PASSING ATTEMPTS
Montana : 5391
Smith : 5193
Young : 4149
Garcia : 3676
Kaepernick : 1692
Garoppolo : 1418
### YARDS PER CATCH
Young : 12.4
Garoppolo : 12.3
Kaepernick : 12.1
Montana : 11.9
Garcia : 11.3
Smith : 11.0
### CAREER PASSING TDS
Montana : 273
Young : 232
Smith : 199
Garcia : 161
Kaepernick : 72
Garoppolo : 71
### CAREER COMPLETION PERCENTAGE
Garoppolo : 67.7
Young : 64.3
Montana : 63.2
Smith : 62.6
Garcia : 61.6
Kaepernick : 59.8
### CAREER WIN PERCENTAGE
Montana : 2.4893617021276597
Garoppolo : 2.357142857142857
Young : 1.9183673469387754
Smith : 1.4776119402985075
Garcia : 1.0
Kaepernick : 0.9333333333333333
### CAREER RECORD
Montana : 117-47-0
Young : 94-49-0
Garcia : 58-58-0
Smith : 99-67-1
Kaepernick : 28-30-0
Garoppolo : 33-14-0
### CAREER GWD
Montana : 28
Smith : 23
Garcia : 17
Young : 16
Garoppolo : 10
Kaepernick : 7
### CAREER RATING
Garoppolo : 98.9
Young : 96.8
Montana : 92.3
Kaepernick : 88.9
Garcia : 87.5
Smith : 86.9
## REGULAR SEASON PER GAME STATS
### PASSING YARDS PER GAME
Garoppolo : 252.17021276595744
Montana : 247.2621951219512
Young : 231.63636363636363
Garcia : 220.14655172413794
Smith : 213.47305389221557
Kaepernick : 211.56896551724137
### PASSING ATTEMPTS PER GAME
Montana : 32.8719512195122
Garcia : 31.689655172413794
Smith : 31.095808383233532
Garoppolo : 30.170212765957448
Kaepernick : 29.17241379310345
Young : 29.013986013986013
### PASSING TDS PER GAME
Montana : 1.6646341463414633
Young : 1.6223776223776223
Garoppolo : 1.5106382978723405
Garcia : 1.3879310344827587
Kaepernick : 1.2413793103448276
Smith : 1.1916167664670658
### RUSHING YARDS PER GAME
Kaepernick : 39.6551724137931
Young : 29.643356643356643
Garcia : 18.448275862068964
Smith : 15.592814371257486
Montana : 10.21951219512195
Garoppolo : 4.085106382978723
### GAME WINNING DRIVES PER GAME
Garoppolo : 0.2127659574468085
Montana : 0.17073170731707318
Garcia : 0.14655172413793102
Smith : 0.1377245508982036
Kaepernick : 0.1206896551724138
Young : 0.11188811188811189
### FPTS PER GAME (using superflex rules)
Young : 16.320699300699303
Montana : 14.900243902439026
Garcia : 14.23689655172414
Kaepernick : 13.997241379310344
Garoppolo : 12.98468085106383
Smith : 11.253892215568863
### INTS PER GAME
Montana : 0.8475609756097561
Garoppolo : 0.8085106382978723
Young : 0.7482517482517482
Garcia : 0.7155172413793104
Smith : 0.6526946107784432
Kaepernick : 0.5172413793103449
### SACKS PER GAME
Kaepernick : 2.9482758620689653
Smith : 2.586826347305389
Young : 2.5034965034965033
Garoppolo : 2.234042553191489
Montana : 1.9085365853658536
Garcia : 1.5603448275862069
## REGULAR SEASON NET PER GAME (net meaning rushing/passing or fumble/int
### NET YARDS PER GAME
Young : 261.27972027972027
Montana : 257.4817073170732
Garoppolo : 256.25531914893617
Kaepernick : 251.22413793103448
Garcia : 238.5948275862069
Smith : 229.06586826347305
### NET TDS PER GAME
Young : 1.9230769230769231
Montana : 1.7865853658536586
Garoppolo : 1.6170212765957446
Garcia : 1.6120689655172413
Kaepernick : 1.4655172413793103
Smith : 1.281437125748503
### NET TURNOVERS PER GAME
Garoppolo : 1.3829787234042554
Garcia : 1.2327586206896552
Young : 1.2237762237762237
Montana : 1.170731707317073
Kaepernick : 1.1551724137931034
Smith : 1.1077844311377245
### NET FIRST DOWNS PER GAME
Garoppolo : 12.893617021276595
Garcia : 12.155172413793103
Kaepernick : 11.96551724137931
Smith : 11.167664670658683
Young : 6.811188811188811
Montana : 1.0365853658536586
### QB PER GAME REGULAR SEASON GRADE
Montana : 42
Young : 40
Garoppolo : 37
Garcia : 27
Kaepernick : 22
Smith : 21
## POSTSEASON PER GAME STATS
### PASSING YARDS PER GAME
Montana : 250.95652173913044
Smith : 249.28571428571428
Young : 237.57142857142858
Kaepernick : 229.0
Garcia : 226.16666666666666
Garoppolo : 160.33333333333334
### PASSING TDS PER GAME
Smith : 2.0
Montana : 1.9565217391304348
Young : 1.4285714285714286
Garcia : 1.1666666666666667
Kaepernick : 1.1666666666666667
Garoppolo : 0.6666666666666666
### INTS PER GAME
Garcia : 1.1666666666666667
Garoppolo : 1.0
Young : 0.9285714285714286
Montana : 0.9130434782608695
Kaepernick : 0.8333333333333334
Smith : 0.2857142857142857
### SACKS PER GAME
Smith : 2.5714285714285716
Montana : 1.9565217391304348
Young : 1.8571428571428572
Kaepernick : 1.8333333333333333
Garcia : 1.6666666666666667
Garoppolo : 1.3333333333333333
### COMPLETION PERCENTAGE
Montana : 62.7
Young : 62.0
Smith : 61.7
Garoppolo : 60.6
Garcia : 58.1
Kaepernick : 58.0
### WIN PERCENTAGE
Montana : 2.2857142857142856
Kaepernick : 2.0
Garoppolo : 2.0
Young : 1.3333333333333333
Garcia : 0.5
Smith : 0.4
### GAME WINNING DRIVES PER GAME
Garcia : 0.3333333333333333
Kaepernick : 0.3333333333333333
Montana : 0.21739130434782608
Garoppolo : 0.16666666666666666
Smith : 0.14285714285714285
Young : 0.07142857142857142
### YARDS PER CATCH
Kaepernick : 14.6
Montana : 12.5
Garoppolo : 12.0
Young : 11.4
Smith : 11.2
Garcia : 10.8
## POSTSEASON NET PER GAME STATS
### NET YARDS PER GAME
Kaepernick : 313.5
Smith : 280.7142857142857
Young : 280.0
Montana : 264.60869565217394
Garcia : 240.83333333333334
Garoppolo : 161.33333333333334
### NET FIRST DOWNS PER GAME
Kaepernick : 15.0
Smith : 13.285714285714286
Garcia : 12.666666666666666
Garoppolo : 9.5
Young : 9.214285714285714
Montana : 0.7391304347826086
### NET TDS PER GAME
Smith : 2.142857142857143
Montana : 2.0434782608695654
Young : 2.0
Kaepernick : 1.8333333333333333
Garcia : 1.3333333333333333
Garoppolo : 0.6666666666666666
### NET TURNOVERS PER GAME
Garcia : 2.1666666666666665
Young : 1.5714285714285714
Kaepernick : 1.5
Montana : 1.2173913043478262
Garoppolo : 1.0
Smith : 0.7142857142857143
### QB PER GAME POSTSEASON GRADE
Montana : 36
Kaepernick : 33
Smith : 29
Garoppolo : 28
Young : 27
Garcia : 22
### QB PER GAME TOTAL (REGULAR SEASON + POSTSEASON) GRADE
Montana : 78
Young : 67
Garoppolo : 65
Kaepernick : 55
Smith : 50
Garcia : 49
