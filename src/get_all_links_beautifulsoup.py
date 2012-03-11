import urllib
from BeautifulSoup import BeautifulSoup

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""



soup = BeautifulSoup(get_page("http://www.google.com"))

links = []

for link in soup.findAll('a'): # find all links
    links.append(link['href'])

print links