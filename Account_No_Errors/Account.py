class Account:
    tradeValue= 0
    positionList=[None] *100
    netList=[None]*100
    netWorth=0
    
    #Initialization
    def __init__(self, currentPosition, price, shares, currentBalance, currentLong, currentShort, SorL):

        self.currentPosition= currentPosition
        self.price=price
        self.shares=shares
        self.currentBalance= currentBalance
        self.currentShort=currentShort
        self.currentLong=currentLong
        self.SorL=SorL



    #Simulates a buy order, resets short position
    def long(self):
        self.currentLong=self.shares+self.currentLong
        self.currentShort = 0
        self.currentBalance=int(self.currentBalance-(self.price *self.shares))
        return self.currentLong



    #Simulates sell order, resets long position, calcualtes money earned from buy and sell.
    def short(self):
        self.currentShort=self.currentLong
        self.currentLong = 0
        self.currentBalance=int(self.currentBalance+(self.price*self.shares))
        return self.currentShort



    #Returns the current free capital available to invest
    def balance(self):
        return self.currentBalance



    #Calculates the net value of all current assets and balance
    def netWorth(self):
        self.netWorth=self.currentBalance+(self.price*self.currentLong)
        print(self.currentBalance)
        return self.netWorth


    
    #Creates a list of the trades completed in order: Balance, Long Shares, Price, Net Worth
    def history(self):
        k=0
        self.netList[currentPosition]=self.netWorth
        valueList=["Position:",self.currentPosition,"Balance-->",self.currentBalance,"Shares held-->", self.currentLong,"Share value-->", self.price,"Net Worth-->", self.netWorth]
        self.positionList[self.currentPosition]=valueList
        while k <= self.currentPosition:
            print(self.positionList[k])
            k=k+1
        return self.positionList



    #Calculates some metric for the accuracy of the individuals decisions 
    def performance():
        pass
##        if SorL == "L":
##            if 
##        if SorL == "S":
##            
##        if SorL == "N":
    #Calculates several metrics for the accounts behavior 
    def statistics():
        pass



#TESTING
#Long or short?
i=0
bal= int(input("Enter the starting balance: "))
sha=0
clong=0
cshort=0

while i<100:
    pri= int(input("Enter the current price of the stock: "))
    LoS= input("Enter L or S for Long or Short. Enter N for neither: ")
    if LoS == "L":
        #This could be a fixed number based on our algorithm so that the only inputs are the original balance, the price of the stock, and Wether it is a long, short or hold.
        sha= int(input("How many shares will you be buying? "))
    if LoS == "S":
        sha= clong
    currentOrder=Account(i,pri,sha,bal, clong, cshort,LoS)
    if LoS == "L":
        clong=currentOrder.long()
    if LoS == "S":
        cshort=currentOrder.short()

    bal= currentOrder.balance()
    currentOrder.netWorth()
    currentOrder.history()


    i=i+1

        
