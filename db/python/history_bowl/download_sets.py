from urllib.request import *
from bs4 import *
import re
import os, errno

def get_request(link):
    return Request(
        link, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
        }
    )

class Set:
    def __init__(self, set_type):
        self.set_type = set_type
        self.bee_links = list()
        self.bowl_links = list()
    def __str__(self):
        return f'Set {self.set_type}'
    __repr__ = __str__
    def add_links(self, links):
        for link in links:
            if 'BEE' in link.text.upper():
                self.bee_links.append(link)
            elif 'BOWL' in link.text.upper():
                self.bowl_links.append(link)
    def resolve_links(self, path):
        
        # Create necessary directories
        try:
            os.makedirs(f'{path}/Set {self.set_type}/bee')
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(f'{path}/Set {self.set_type}/bee'):
                pass
            else:
                raise
        try:
            os.makedirs(f'{path}/Set {self.set_type}/bowl')
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(f'{path}/Set {self.set_type}/bowl'):
                pass
            else:
                raise

        # Write out bee pdfs
        for bee_link in self.bee_links:
            # Read data
            with urlopen(get_request(bee_link['href'])) as pdf:
                data = pdf.read()
            # Extract filename from path
            end = bee_link['href'].split('/')[-1]
            # Write out
            with open(f'./{path}/Set {self.set_type}/bee/{end}', 'wb') as file:
                file.write(data)

        # Write out bowl pdfs
        for bowl_link in self.bowl_links:
            # Read data
            with urlopen(get_request(bowl_link['href'])) as pdf:
                data = pdf.read()
            # Extract filename from path
            end = bowl_link['href'].split('/')[-1]
            # Write out
            with open(f'./{path}/Set {self.set_type}/bowl/{end}', 'wb') as file:
                file.write(data)

def get_set_type(p):
    if 'Set' in p.text:
        if 'A' in p.text:
            return 'A'
        if 'B' in p.text:
            return 'B'
        if 'C' in p.text:
            return 'C'

def read_sets(name, link):
    print(f'Reading {name}')
    with urlopen(get_request(link)) as page:
        soup = BeautifulSoup(page, features="lxml")
    div = soup.find('div', class_='wprt-container bg-even-rows')

    sets = list()

    for p in div.find_all():
        set_type = get_set_type(p)
        if set_type != None and (len(sets) == 0 or sets[-1].set_type != set_type):
            sets.append(Set(set_type))
        
        if (len(sets) > 0):
            links = p.find_all('a')
            sets[-1].add_links(links)
        else:
            print(f'No sets: {p.text}')

    for s in sets:
        s.resolve_links(name)

def read_home():
    req = get_request('https://www.historybowl.com/resources/study-guides-resources/')
    with urlopen(req) as home:
        soup = BeautifulSoup(home, features="lxml")
    
    links = soup.find_all('a')
    links = list(filter(lambda link: 'Regional and State Tournament Question Sets' in link.text, links))
    
    #return links

    for link in links:
        read_sets(link.text, link['href'])


home_links = read_home()

