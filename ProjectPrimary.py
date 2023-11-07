from unibit_api_v2.stock import StockPrice
from unibit_api_v2.news import StockNews
from unibit_api_v2.company import CompanyInfo
from datetime import date
from datetime import timedelta
import freecurrencyapi

def intro() -> None:
    print("Welcome to my CS361 project! Please login before options are given.\n")
    login()

def login() -> None:

    username = input("Please input your name.")

    print("Welcome, " + username + ".\n")
    mainMenu()
    goodbye()

def mainMenu() -> None:

    today = str(date.today())
    yesterday = str( date.today() - timedelta(days = 1) )
    yearAgo = str( date.today() - timedelta(weeks = 52) )

    sp = StockPrice(key = "HpiAtKLqJAb0e2c4LCn6E4Bf4IPT2QQ0")
    sn = StockNews(key = "HpiAtKLqJAb0e2c4LCn6E4Bf4IPT2QQ0")
    ci = CompanyInfo(key = "HpiAtKLqJAb0e2c4LCn6E4Bf4IPT2QQ0")
    curClient = freecurrencyapi.Client("fca_live_ouBN65YL6VZ3aGqyNoCYFAXOSw84IrHi3qneXr67")

    result = curClient.latest()
    cDict = result['data']
    rate = 1
    cName = "USD"

    while(True):
        displayMarketData()

        usrInp = input("1. Search for a stock. Selection done via input market tag. \n" +
        "2. Compare two stocks. Selection done via input market tag.\n" +
        "3. Favorite a stock. Selection done via input market tag.\n" +
        "4. Display a list of stocks sorted by value in descending order.\n" + 
        "5. Display a list of stocks sorted by volume in descending order.\n" +
        "6. Display a list of stocks sorted by percentage increase in descending order.\n" +
        "7. Display a list of stocks sorted by percentage decrease in descending order.\n" +
        "8. Display a list of stocks sorted by type.\n" +
        "9. Change the displayed currency to users selection.\n" +
        "10. Exit. \n")

        if( usrInp == "1" ):
            search(sp, sn, ci, today, yesterday, yearAgo, rate, cName)
        elif( usrInp == "2" ):
            compare(sp, sn, ci, rate)
        elif( usrInp == "3" ):
            favorite(sp, sn, ci, rate)
        elif( usrInp == "4" ):
            sortValue(sp, sn, ci, rate)
        elif( usrInp == "5" ):
            sortVolume(sp, sn, ci, rate)
        elif( usrInp == "6" ):
            sortPercentageInc(sp, sn, ci, rate)
        elif( usrInp == "7" ):
            sortPercentageDec(sp, sn, ci, rate)
        elif( usrInp == "8" ):
            sortType(sp, sn, ci, rate)
        elif( usrInp == "9" ):
            rate, cName = changeCurrency(sp, sn, ci, rate, cDict, cName)
        elif( usrInp == "10" ):
            break
        else:
            print("Invalid Input. Please try again.")

def search(sp, sn, ci, today, yesterday, yearAgo, rate, cName):
    #Work in Progress

    userTick = input("Enter the ticker of the company you intend to search for.\n")

    userSP = sp.getHistoricalStockPrice(ticker=[userTick], startDate=today, endDate=yesterday)
    userSN = sn.getStockNews(ticker=[userTick], startDate=today, endDate=yearAgo, startMinute="0:00:00", endMinute="23:59:59", genre="all", sector="all")
    userCI = ci.getCompanyProfile(ticker=[userTick])    

    compName = str(userCI['result_data'][userTick]['company_name'])
    compLoc = str(userCI['result_data'][userTick]['address'])
    compSector = str(userCI['result_data'][userTick]['sector'])
    compIndustry = str(userCI['result_data'][userTick]['industry'])
    compEmp = str(userCI['result_data'][userTick]['employee_number'])
    compDesc = str(userCI['result_data'][userTick]['company_description'])
    stockPrice = userSP['result_data'][userTick][0]['adj_close'] * rate

    print("\n\n\nCompany Name: " + compName + "\n\nCompany Location: " + compLoc + "\n\nCompany Sector: " + compSector + "\n\nCompany Industry: " + compIndustry 
        + "\n\nCompany Employee Count: " + compEmp + "\n\nCompany Description: " + compDesc)

    print("\n\nThe stock price for the selected stock at most recent close is: " + str(stockPrice) + " " + cName)

    print("\n\nThere have been: " + str(userSN['meta_data']['num_total_data_points']) + " articles written in the last year about " + compName)

    input("\nPress enter to return to main menu.")

def compare(sp, sn, ci):
    #Work in Progress
    return

def favorite(sp, sn, ci):
    #Work in Progress
    return

def sortValue(sp, sn, ci):
    #Work in Progress
    return

def sortVolume(sp, sn, ci):
    #Work in Progress
    return

def sortPercentageInc(sp, sn, ci):
    #Work in Progress
    return

def sortPercentageDec(sp, sn, ci):
    #Work in Progress
    return

def sortType(sp, sn, ci):
    #Work in Progress
    return

def changeCurrency(sp, sn, ci, rate, cDict, cName):
    #Work in Progress
    userInp = input("\nWhat currency would you like to view the program in?")

    if userInp in cDict:
        rate = cDict[userInp]
        cName = userInp
        print("\n Rate changed.")

        return (rate, cName)
    else:
        print("\n Input not recognized.")

    input("\n\nPress enter to return to main menu.")
    

def displayMarketData():
    for x in range(10):
        print("-----------------------Placeholder Data-----------------------\n")
              
def goodbye():
    print("Goodbye!\n")


intro()