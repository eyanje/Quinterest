from bs4 import BeautifulSoup
import urllib.request
import io

from PyPDF2 import PdfFileReader, PdfFileMerger

def read_tournament(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'})) as file:
        soup = BeautifulSoup(file, features='html.parser')
    cont = soup.find(id='content')
    try:
        a_links = cont.find_all('a', href=True)
    except AttributeError as e:
        a_links = None
        print(f'AttributeError on {url}: {e}')
    hrefs = tuple((a.text, a['href']) for a in a_links if a['href'].endswith('.pdf'))
    return hrefs

def read_home_hrefs():
    with urllib.request.urlopen(urllib.request.Request('https://www.historybowl.com/resources/study-guides-resources/', headers={'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'})) as file:
        soup = BeautifulSoup(file, features='html.parser')
    cont = soup.find(id='post-10053')
    ul = cont.find('ul')
    a_links = ul.find_all('a', href=True)
    hrefs = tuple((a.text, read_tournament(a['href'])) for a in a_links if 'Set' in a.text)

    return hrefs

def merge_pdfs():
    home_hrefs = read_home_hrefs()
    for tournament_name,tournament_links in home_hrefs:
        merger = PdfFileMerger()
        for qset_name, qset_link in tournament_links:
            with urllib.request.urlopen(urllib.request.Request(qset_link, headers={'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'})) as file:
                merger.append(PdfFileReader(io.BytesIO(file.read())))
        merger.write(f'{tournament_name}.pdf')

merge_pdfs()