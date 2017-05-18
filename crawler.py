import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'referer': 'https://www.forbes.com/billionaires/list/'
}

for year in range(1997, 2018):
    year = str(year)
    print(year + ' billionaires!')
    res = requests.get('https://www.forbes.com/ajax/list/data?year=' + year +'&uri=billionaires&type=person', headers=headers)
    time.sleep(3)
    data = res.text
    with open('./static/raw_data/' + year +'.json', 'w') as f:
        f.write(res.text)
