"""
Title: CometBot
Author: Brian Turza
"""
import sys
import csv
import time
from colorama import *

from sites.theStreets import TheStreets

"""
PATH = "C:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe"
driver = webdriver.PhantomJS(PATH)
"""

class CometBot(TheStreets):

    def __init__(self):
        self.PATH_Selenium = "C:/Program Files (x86)/chromedriver.exe"
        self.urls = [
            "https://www.thestreets.sk/online-raffle/", 
            "footlocker.en.uk",
            "supremenewyork.com"
        ]
        self.platforms = {
            'Nike' : [],
            'Footsites' : ['Footlocker', 'Kids Footlocker'], 
            'Supreme' : [],
        }
        self.shopList = [
            "The Streets",
            "Footlocker"
        ]
        self.commands = {
            'help' : 'returns list of all commands', 
            'order' : 'Orders from listed shops',
            'exit' : 'Quits the CometBot',
        }
    
    def display_logo(self) -> str:
        str = """
                .:'   _____                     _   ____        _   
            _.::'    / ____|                   | | |  _ \      | |  
  .-;;-.   (_.'     | |     ___  _ __ ___   ___| |_| |_) | ___ | |_ 
 / ;;;' \           | |    / _ \| '_ ` _ \ / _ \ __|  _ < / _ \| __|
|.  `:   |          | |___| (_) | | | | | |  __/ |_| |_) | (_) | |_ 
 \:   `;/            \_____\___/|_| |_| |_|\___|\__|____/ \___/ \__|   
  '-..-'
 #-----------------------------------------------------------------#
 |  Bot Version: v0.1 - preAlpha                                   |  
 |  Type help for list of commands                                 |       
 #-----------------------------------------------------------------#
"""
        return str
    
    def displayHelp(self) -> None:
        for command, explanation in self.commands.items():
            print(f"{command} - {explanation}")
    
    def handleArgs(self) -> None:
        arg_len = len(sys.argv)
        if arg_len < 2: return
            
        if sys.argv[1] in ["-h", "--help"]:
            self.displayHelp()


    def mainMenu(self) -> None:
        """
        This method handles the menu of this program.
        """
        inp = ""
        print(self.display_logo())
        self.handleArgs()
        while inp != "exit":
            inp = input(" $ -> ")
            if inp == "": continue

            if inp == "exit": quit()

            if inp == "help":
                self.displayHelp()

            elif inp == "order":
                print("----------------")
                print("Supported shops:")
                print("----------------")
                print("\n".join([f"{id + 1}. {shop}" for id, shop in enumerate(self.shopList)]))
                print("----------------")
                shop = input("Choose site [number]:")
                file_data = input("Enter csv file name with data, f. e. [filename].csv :")
                data = self.extractData(file_data)
                if data == "error": continue
                for row in data:
                    if shop in ["1", "1."]:
                        self.submitForm("thestreets", row)
                    elif shop in ["2", "2"]:
                        self.submitForm("footlocker", row)
            else:
                init(convert=True)
                print(f"{Fore.RED}Error, command '{inp}' was not found{Fore.WHITE}")
                
        
    def extractData(self, filename: str):
        """
        This method reads .csv file and extracts nested list of data 
        """
        result = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile, skipinitialspace=True)
                index = 0
                for row in reader:
                    if index > 0:
                        row.pop(0)
                        result.append(row)
                    index += 1
        except FileNotFoundError:
            init(convert=True)
            print(f"{Fore.RED}Error, file '{filename}' was not found{Fore.WHITE}")
            return "error"

        return result


    def submitForm(self, shop, rowData) -> None:
        """
            :shop

        """
        if shop == "thestreets":
            #self.raffleSelenium(1, rowData) # Input data represents each shop by id number - TheStreets - 1
            self.raffleRequests(1, rowData)

        elif shop == "footlocker":
            print("Footlocker resale botting - Comming soon!")
    
    def proxies(self):
        pass
    

if __name__ == "__main__":
    c = CometBot()
    c.mainMenu()
    driver.quit()
