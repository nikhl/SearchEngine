# get_page() procedure for getting the contents os webpage as a string

import urllib
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""


# procedure for finding and returning the next url from the passing page parameter
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# procedure for finding the union of two lists
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
    return p


# given a seed page, it will return all the links in that page
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


# for crawling the web, constrained on the maximum different pages crawled
def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if len(crawled) < max_pages :            
            if page not in crawled:
                union(tocrawl, get_all_links(get_page(page)))
                crawled.append(page)
    return crawled


# Running the program with given seed pagec and max_pages
print crawl_web("http://xkcd.com/353",10)

