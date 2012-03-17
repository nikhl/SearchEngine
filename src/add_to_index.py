# Data structure to store the url along with their keywords
index = []


    
# procedure for adding a new keyword,url pair to index
def add_to_index(index,keyword,url):
    for each in index:
        if each[0] == keyword:
            urls = each[1]
            if url not in urls:
                urls.append(url)
            return
    new_keyword = [keyword,[url]]
    index.append(new_keyword)
        

def add_page_to_index(index,url,content):
    words = content.split();
    for each in words:
        add_to_index(index,each,url)

# Testing

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
add_page_to_index(index,"http://nikhil.com","Nikhil Tej Lingutla Venkata Nikhil")

print index
