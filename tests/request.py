import requests
from bs4 import BeautifulSoup
import json

url = 'https://learnqntm.com/ide/'

values = {
    'code': '''
print(5 * 2 + 1)
'''
}
r = requests.post(url, data=values)

soup = BeautifulSoup(r.text, 'html.parser')

for br in soup('br'):
    br.replace_with('\n')

spans = soup.find("span", class_="output") 
print(spans.text)
location_data = {"output": spans.text}
print(json.dumps(location_data))
