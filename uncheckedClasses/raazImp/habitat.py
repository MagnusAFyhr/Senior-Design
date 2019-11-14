import csv

class Habitat:
    def __init__(self):
        self.open = 1
        self.high = 1
        self.low = 1
        self.close = 1
        self.volume = 1
        self.currRow = 1
        self.step() #first step sets data point to line 0 of csv

    def print_test(self):
        print(self.open)
        print(self.high)
        print(self.low)
        print(self.close)
        print(self.volume)

    def step(self): #go to next line in csv and edit ohlcv
        with open('MSFT.csv', mode='r') as csvfile:
            readCSV = list(csv.reader(csvfile, delimiter=','))
            row = readCSV[self.currRow]
        self.open = row[1]
        self.high = row[2]
        self.low = row[3]
        self.close = row[4]


def main():
    habitat1 = Habitat()


if __name__ == "__main__":
    main()

