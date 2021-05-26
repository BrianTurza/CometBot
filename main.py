"""
Title: CometBot
Author: Brian Turza
"""
import csv
import time

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
            "footlocker.en.uk"
        ]
        self.commands = {
            'help' : 'returns list of all commands', 
            'order' : 'Orders from listed shops',
            'exit' : 'Quits the CometBot',
        }
    
    def display_logo(self):
        str = """
                .:'   _____                     _   ____        _   
            _.::'    / ____|                   | | |  _ \      | |  
  .-;;-.   (_.'     | |     ___  _ __ ___   ___| |_| |_) | ___ | |_ 
 / ;;;' \           | |    / _ \| '_ ` _ \ / _ \ __|  _ < / _ \| __|
|.  `:   |          | |___| (_) | | | | | |  __/ |_| |_) | (_) | |_ 
 \:   `;/            \_____\___/|_| |_| |_|\___|\__|____/ \___/ \__|   
  '-..-'
 # ----------------------------------------------------------------#
 |  Bot Version: v0.1 - preAlpha                                   |  
 |  Type help() for list of commands                               |       
 # ----------------------------------------------------------------#
"""
        return str

    def mainMenu(self):
        inp = ""
        print(self.display_logo())
        while inp != "exit":
            inp = input(" ~$ ")
            if inp == "help":
                for command, explanation in self.commands.items():
                    print(f"{command} - {explanation}")
            elif inp == "order":
                print("1. TheStreets.sk")
                shop = input("Choose site [number]:")
                file_data = input("Enter cvs file name with data, f. e. [filename].csv :")
                if shop == "1.":
                    data = self.extractData(file_data) 
                    for row in data:
                        self.submitForm("thestreets", row)
                        time.sleep(1)
        
    def extractData(self, filename):
        result = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            index = 0
            for row in reader:
                if index > 0:
                    row.pop(0)
                    result.append(row)
                index += 1

            return result


    def submitForm(self, shop, rowData):
        """
            :shop

        """
        if shop == "thestreets":
            #self.raffleSelenium(1, rowData) # Input data represents each shop by id number - TheStreets - 1
            self.raffleRequests(1, rowData)

        elif shop == "footlocker":
            print("Footlocker resale botting - Comming soon!")
    

if __name__ == "__main__":
    CometBot().mainMenu()
    driver.quit()
