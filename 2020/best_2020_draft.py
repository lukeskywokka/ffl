import csv


def read_file(filename):
    the_file = open(filename)
    csvreader = csv.reader(the_file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        print(row)
    the_file.close()
    print ("=============================")


read_file("draft.csv")


URL = "https://fantasydata.com/nfl/fantasy-football-leaders?season=2020&seasontype=1&scope=1&subscope=1&scoringsystem=2&startweek=1&endweek=1&aggregatescope=1&range=1"