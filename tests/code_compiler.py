import requests
from bs4 import BeautifulSoup
import json

url = 'https://learnqntm.com/ide/'

values = {
    'code': '''
def prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

x = 3727
print(prime(x))
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
