# crawling the web starting from seed page with max_depth parameter

"""
A points to B, C, D
B points to H, I
C points to G
D points to E, F
I points to J, K
E points to M
K points to L
I believe it should return the following (and got that result when running my program:

outputs should be following for the above specified inputs

max_depth=0: A
max_depth=1: A,B,C,D
max_depth=2: A,B,C,D,E,F,G,H,I
max_depth=3: A,B,C,D,E,F,G,H,I,J,K,M
max_depth=4: A,B,C,D,E,F,G,H,I,J,K,M,L

def get_page(url):
    if url == "A":
        return '<a href="B">B</a> <a href="C">C</a><a href="D">D</a>'
    elif url == "B":
        return '<a href="H">H</a> <a href="I">I</a>'
    elif url == "C":
        return '<a href="G">G</a>'
    elif url == "D":
        return '<a href="E">E</a> <a href="F">F</a>'
    elif url == "E":
        return '<a href="M">M</a>'
    elif url == "F":
        return 'emptiness'
    elif url == "G":
        return 'emptiness'
    elif url == "H":
        return 'emptiness'
    elif url == "I":
        return '<a href="J">J</a> <a href="K">K</a>'
    elif url == "J":
        return 'nothing'
    elif url == "K":
        return '<a href="L">L</a>'
    elif url == "L":
        return 'nothing'
    elif url == "M":
        return 'nothing'  """
        
import urllib
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
    return p


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawl_with_depth = []
    
    # appending depth '0' urls to crawl_with_depth which is nothing but seed page
    crawl_with_depth.append(tocrawl)
    
    for i in range(max_depth):
        crawled = []
        
        # crawling all the urls in tocrawl and store them in crawled
        for each in tocrawl:
            crawled = union(crawled,get_all_links(get_page(each)))
            
        # storing the urls with the list index as their depth    
        crawl_with_depth.append(crawled)
        # setting the currently retrieved urls to "tocrawl" for the next crawl
        tocrawl = crawl_with_depth[i+1]
    
    # appending all the ursl upto given depth and returning
    final_urls = []
    for i in range(max_depth+1):
        final_urls = union(final_urls,crawl_with_depth[i])
    return final_urls
    
    

print crawl_web("http://xkcd.com/353",1)
