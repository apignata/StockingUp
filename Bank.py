import random
from tabulate import tabulate
import pyautogui


class BankAccount():

    def __setinfo(self, firstName, pin, balance = 7500, credit = 7500, stock = None ):
        self.fName = firstName
        self.balance = balance
        self.cred = credit
        self.pin = pin
        if stock is None:
            self.stock = []
        else:
            self.stock = stock

    def newUser(self, bal = 7500, cred = 7500, stock = None):
        self.fName = input('Please enter your name: ')
        self.pin = input('Please enter 2 digit pin: ')
        self.balance = bal
        self.cred = cred
        if stock is None:
            self.stock = []
        else:
            self.stock = stock

        while (len(self.pin)) != 2:
                print("Your pin is invalid.")
                self.pin = input('Please enter 2 digit pin: ')

    def addStockToAccount(self, stockname, BankAccount):
        self.stock.append(stockname)
        printInfo(BankAccount)

class Stock():
    def set(self, name, value, random, dividend, boughtPrice):
        self.name = name
        self.value = value
        self.random = random
        self.div = dividend
        self.boughtPrice = boughtPrice


def printInfo(BankAccount):
    print('\n'+BankAccount.fName)
    print("Balance: ${:,.0f}".format(BankAccount.balance))
    print("Credit: ${:,.0f}".format(BankAccount.cred)+ '\n')
    test1 = []
    test2 = []
    test3 = []
    for w in range(len(BankAccount.stock)):
        test1.append(BankAccount.stock[w].name)
        test2.append("${:,.0f}".format(BankAccount.stock[w].div))
        test3.append("${:,.0f}".format(BankAccount.stock[w].boughtPrice))

    table = zip(test1, test2, test3)
    print(tabulate(table, headers=['Stocks', 'Current Price', 'Price'], floatfmt=".0f", tablefmt='orgtbl'))


def printStocks():
    test1 = []
    test2 = []
    test3 = []
    for k, v in stockList.items():
        test1.append(k)
        test2.append("${:,.0f}".format(v.value))
        test3.append("${:,.0f}".format(v.div))

    table = zip(test1, test2, test3)
    print(tabulate(table, headers=['Stock Name', 'Value', 'Cost/Share'], floatfmt=".0f", tablefmt='orgtbl'))

def withdraw(amount, BankAccount):
    if (amount-1) >= (BankAccount.balance + BankAccount.cred):
        print("You can not withdraw over your limit.")
        return -1
    else:
        BankAccount.balance -= amount
        BankAccount.cred = (BankAccount.cred - amount)
        return BankAccount.balance

def deposit(amount, BankAccount):
    BankAccount.balance += amount
    BankAccount.cred = ((amount + BankAccount.cred) ** 1.002)
    return BankAccount.balance

def randomizeStock():
    for k, v in stockList.items():
        rand = random.uniform(.4, 2.1)
        div = random.random()
        v.value = rand*(v.value*.93)
        v.div = (div*v.value*.3)

def removeStockToAccount(stockname, BankAccount):
    BankAccount.stock.remove(stockname)
    printInfo(BankAccount)

def CreateStocks():
    for init in range(1, 13):
        init = Stock()
        temp = random.choice(['Red ', 'Blue ', 'Green ', 'Black ', 'Orange ', 'Yellow ', 'White ', 'Purple '])
        temp2 = random.choice(['Ant', 'Bear', 'Cat', 'Dog', 'Falcon',
                               'Snake', 'Tiger', 'Lion', 'Turtle', 'Zebra'])
        name = str(temp + temp2)
        rand = random.uniform(.3, 2)
        val = random.randint(15000, 75000)
        div = random.random()

        init.set(name, val, rand, (div*val*.3), div)

        if init.name not in stockList:
            stockList[init.name] = init

i = 1
userList = {}
stockList = {}

CreateStocks()

while True:
    userIn = input("\nWelcome to Stocking Up\n===============================\nn: \t To register as a new user.\nv: \t To view your balance.\nl: \t To view stock list.\nb: \t To buy a stock.\ns: \t To sell a stock.\n" )
    if userIn == 'n':
        a = 'a' + str(i)
        a = BankAccount()
        a.newUser()
        if (a.pin not in userList):
            userList[a.pin] = a
        i+=1

    elif userIn == 'v':
        tempPin = input('Please enter your PIN to view your account.')
        p = 0
        for k, v in userList.items():
            if k == tempPin:
                printInfo(v)
                p = 1

        if p == 0:
            print("Pin not found")
    elif userIn == 'l':
        printStocks()
    elif userIn == 'b':
        printStocks()

        bank = ''

        tempPin = input('Please enter your PIN.')
        p = 0
        for k, v in userList.items():
            if k == tempPin:
                bank = v
                p = 1
                break
        if p == 0:
            print("Pin not found")
        else:
            printInfo(bank)
            uIn = input("Type the name of the stock you would like to buy or type exit: ")
            for k, v in stockList.items():
                if uIn == v.name:
                    test = withdraw(v.div, bank)
                    if test != -1:
                        v.boughtPrice = v.div
                        bank.addStockToAccount(v, bank)
                        randomizeStock()
                        break

    elif userIn == 's':
        printStocks()

        bank = ''

        tempPin = input('Please enter your PIN.')
        p = 0
        for k, v in userList.items():
            if k == tempPin:
                bank = v
                p = 1

        if p == 0:
            print("Pin not found")
        else:
            printInfo(bank)
            uIn = input("Type the name of the stock you would like to sell or type exit: ")
            y = 0
            yes = False
            for k, v in stockList.items():
                if uIn == v.name:
                    for z, x in userList.items():
                        for w in range(len(x.stock)):
                            place = x.stock[w].name

                            if uIn == place and x.pin == bank.pin: #x.stock[y].name:
                                deposit(v.div, bank)
                                removeStockToAccount(v, bank)
                                randomizeStock()
                                yes = True
                                break

            if yes == False:
                print("You do not own this stock")

    else:
        print("Please enter a correct value.")


#High Priority
#===============================================
#Buy price seperate for each account, 2 of 1 stock
#negative credit crashes when turns into -j

#Error message when trying to buy a stock that doesnt exist


#Features
#================================================
#Turn Base, minutes?
#past turn changes +, -
#if stock dips below a certain value sell all and replace from market
#random events
    #each person gains random stock
    #Rainy Day
    #Boom
    #color or animal change
    #Give or take away money/credit from each player

#win condition (sells all stock displays results)
#gui
#server
#up and down arrow keys instead of typing name
#stock name prefix











