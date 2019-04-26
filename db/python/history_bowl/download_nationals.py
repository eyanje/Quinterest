from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
import re
import errno

def get_request(link):
    return Request(
        link, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
        }
    )

def make_path(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

class NationalSet:
    def __init__(self, link):
        self.name = link.text
        self.url = link['href']

        if 'BEE' in self.name.upper():  
            self.set_type =  'Bee'
        elif 'BOWL' in self.name.upper():
            self.set_type =  'Bowl'
        else:
            self.set_type = 'Other'

    def download(self, base):
        # Read data from online
        with urlopen(get_request(self.url)) as file:
            data = file.read()

        file_name = self.url.split('/')[-1]
        
        path = f'{base}/{self.set_type}/{file_name}'
        with open(path, 'wb') as file:
            file.write(data)

class NationalTournament:
    def __init__(self, link):
        self.name = link.text
        self.url = link['href']
        self.nsets = list()
        self.has_other = False

        self.load()
    def load(self):
        with urlopen(get_request(self.url)) as page:
            soup = BeautifulSoup(page, features='lxml')
        div = soup.find('div', class_='wprt-container bg-even-rows')
        
        links = div.find_all('a', href=True)
        links = list(filter(lambda link: '.' in link['href'].strip().split('/')[-1], links))

        for element in links:
            self.nsets.append(NationalSet(element))
            if (self.nsets[-1].set_type == 'Other'):
                self.has_other = True
    
    def download(self, base):
        print(f'Downloading {self.name}')

        base = f'{base}/{self.name}'
        make_path(base)
        make_path(f'{base}/Bee')
        make_path(f'{base}/Bowl')
        if self.has_other:
            make_path(f'{base}/Other')
        for nset in self.nsets:
            nset.download(base)
    
def load_home():
    with urlopen(get_request('https://www.historybowl.com/resources/study-guides-resources/')) as home:
        soup = BeautifulSoup(home, features='lxml')
    links = soup.find_all('a', text=re.compile('.*Nationals Question Sets.*'), href=True)

    tournaments = list()

    for link in links:
        tournament = NationalTournament(link)
        tournament.download('./Nationals')

load_home()