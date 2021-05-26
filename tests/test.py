import requests
from bs4 import BeautifulSoup

url = "https://learnqntm.com/login"

username = "test"
password = "test"

response = requests.get(url, auth=(username, password), verify=False)

# Getting the text of the page from the response data       
page = BeautifulSoup(response.text)

# Finding the text contained in a specific element, for instance, the 
# textarea element that contains the area where you would write a forum post
txt = page.find('input', name="username").string

# Finding the value of a specific attribute with name = "version" and 
# extracting the contents of the value attribute
tag = page.find('input', attrs = {'name':'version'})
ver = tag['value']

# Changing the text to whatever you want
txt = "Your text here, this will be what is written to the textarea for the post"

# construct the POST request
form_data = {
    'save' : 'Submit changes'
    'text' : txt
} 

post = requests.post(url,auth=(username, password),data=form_data,verify=False)