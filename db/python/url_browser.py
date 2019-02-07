# In memoriam

import io
import urllib.request

from bs4 import BeautifulSoup
class Tournament:
    name = ''
    subject = ''
    year = 0
    difficulty = 'HS'

    def __init__(self, name, year, subject, difficulty):
        self.name = name
        try:
            self.year = int(year[-4:])
        except TypeError:
            self.year = int(year)
        except ValueError:
            self.year = None

        self.subject = subject

        difficulty = difficulty.upper()
        if (difficulty == 'MIDDLE SCHOOL'):
            self.difficulty = 'MS'
        elif (difficulty == 'HIGH SCHOOL'):
            self.difficulty = 'HS'
        else:
            self.difficulty = difficulty
    
    def __str__(self):
        return f'{self.name}, {self.year}, ({self.difficulty})'

def load_base_page():
    with urllib.request.urlopen('http://quizbowlpackets.com/') as file:
        soup = BeautifulSoup(file, 'html.parser')
        link_list = soup.findAll('ul')[5].findAll('a')
        #link_list = soup.div.div.contents[11].contents[9].contents[1].contents[13]
        links = [(a.text, 'http://quizbowlpackets.com/' + a['href']) for a in link_list]
        return links
        # div div [2] [1] [1] ul
            # iterate over li span a

def load_details(link):
    """Returns a tournament object containing the details of a tournament"""
    # Loads details about a tournament
    with urllib.request.urlopen(link) as file:
        soup = BeautifulSoup(file, 'html.parser')
        try:
            header = soup.div.div.contents[11].contents[9].contents[1]
        except IndexError:
            header = soup.div.div.contents[11].contents[3].div
        
        name = header.h2.text

        difficulty = header.contents[5].contents[1].strip()

        # Separate year and name
        try:
            year = int(name.split(' ')[0])
            name = ' '.join(name.split(' ')[1:])
        except IndexError:
            year = header.contents[7].text[-4:]

        data = Tournament(
            name,
            year,
            'Sample Subject',
            difficulty
        )

        return data

def load_tournament_links(link):
    with urllib.request.urlopen(link) as file:
        soup = BeautifulSoup(file, 'html.parser')
        link_list = soup.findAll('ul')[2].findAll('a')
        links = [(a.text, a['href']) for a in link_list]
        return links
