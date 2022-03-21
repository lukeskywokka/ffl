from csv import reader
from matplotlib import pyplot as plt
from collections import defaultdict

plotxaway = defaultdict(list)
plotyaway = defaultdict(list)

plotxhome = defaultdict(list)
plotyhome = defaultdict(list)

footballx = defaultdict(list)
footbally = defaultdict(list)
#   0  1 2 3 4  5  6  7    8     9        10          11         12       13    14    15    16        17         18
# time,x,y,s,a,dis,o,dir,event,nflId,displayName,jerseyNumber,position,frameId,team,gameId,playId,playDirection,route


def read_file(filename):
    """
    Read cost file
    """
    the_file = open(filename)
    csvreader = reader(the_file)
    rows = []
    for k, row in enumerate(csvreader):

        print(row)
        if row[14] == "away":
            plotxaway[row[13]].append(float(row[1]))
            plotyaway[row[13]].append(float(row[2]))
        elif row[14] == "home":
            plotxhome[row[13]].append(float(row[1]))
            plotyhome[row[13]].append(float(row[2]))
        elif row[10] == "Football":
            footballx[row[13]].append(float(row[1]))
            footbally[row[13]].append(float(row[2]))
        
    the_file.close()

read_file("first_play.csv")

for k, v in plotyaway.items():
    plt.scatter(plotxhome[k], plotyhome[k], color="blue")
    plt.scatter(plotxaway[k], plotyaway[k], color="red")
    plt.scatter(footballx[k], footbally[k], color="brown")
    plt.pause(.0001)
plt.show()
   
  
# x = []
# y = []
  
# for i in range(100):
#     x.append(i)
#     y.append(i)
  
#     # Mention x and y limits to define their range
#     plt.xlim(0, 100)
#     plt.ylim(0, 100)
      
#     # Ploting graph
#     plt.plot(x, y, color = 'green')
#     plt.pause(0.01)
  
# plt.show()