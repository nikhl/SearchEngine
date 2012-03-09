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
        return 'nothing'  

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
    crawled = []
    crawled_with_depth = []
    for i in range(max_depth):
        crawled_with_depth.append(get_all_links(get_page(page)))
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                union(tocrawl, get_all_links(get_page(page)))
                crawled.append(page)
        print crawled_with_depth
        
    #return crawled
    

crawl_web("A",1)
