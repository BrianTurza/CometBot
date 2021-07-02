class TheStreets:

    def raffleSelenium(self, id, userData):
            """ Sumbits TheStreets.sk form using selenium

            This method will submit shuffled item with given csv data.
            """
            from selenium import webdriver
            
            driver = webdriver.Chrome(self.PATH_Selenium)
            driver.get(self.urls[id - 1]) # list indexing starts at 0 not 1
            name = driver.find_element_by_id("name")
            street = driver.find_element_by_id("street")
            email = driver.find_element_by_id("yourEmail")
            city = driver.find_element_by_id("city")
            phone = driver.find_element_by_id("phone")
            psc = driver.find_element_by_id("psc")
            check_conditions = driver.find_element_by_name("agreed_personal_info_tiny_contact_form")
            
            name.send_keys(userData[0])
            street.send_keys(userData[1])
            email.send_keys(userData[2])
            city.send_keys(userData[3])
            phone.send_keys(userData[4])
            psc.send_keys(userData[5])
            driver.execute_script("arguments[0].click();", check_conditions)
            driver.find_element_by_id("m1_wrapper").click()
            driver.find_element_by_name("submit").click()

    def raffleRequests(self, id, userData):
        import requests
        from bs4 import BeautifulSoup

        url = self.urls[id - 1]
        values = {
            'name': userData[0],
            'street': userData[1],
            'yourEmail': userData[2],
            'city': userData[3],
            'phone': userData[4],
            'psc': userData[5]


        }
        r = requests.post(url, data=values)
        print(values)
        soup = BeautifulSoup(r.text, 'html.parser')

        for br in soup('br'):
            br.replace_with('\n')
        print("-", r)
