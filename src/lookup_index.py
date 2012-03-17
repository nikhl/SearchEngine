index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for each in index:
        if each[0] == keyword:
            return each[1]
    return []

print lookup(index,'udacity')