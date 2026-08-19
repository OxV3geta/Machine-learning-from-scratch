'''
Real world Example:: Multhithreding for I/O-bounds Tasks
Scenario : Web Scraping
Web Scaping oftern involves making numerous network requests to fetch
web pages.These task are I/O-bound beacuase they spend a lot of time waiting for responses
from servers. Multithreding can significantly improve the performance by allowing multiptle
web pages to be fetched concurrently.
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.geeksforgeeks.org/system-design/system-design-tutorial/',
    
    'https://www.geeksforgeeks.org/machine-learning/machine-learning/',
    
    'https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/'
]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.get_text())} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

# print(fetch_url(urls))
    
print("All web pages fetched!")