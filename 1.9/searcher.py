# -*- coding: GBK -*-
import urllib.request
#import requests
from lxml import etree ##for opening URL
from dhs import *

'''
Python crawler intro
https://www.zhihu.com/question/20899988

XPath
https://www.tutorialspoint.com/xpath/xpath_operators.htm
https://www.cnblogs.com/lei0213/p/7506130.html
https://stackoverflow.com/questions/5350666/xpath-or-operator-for-different-nodes
https://stackoverflow.com/questions/3317018/xpath-check-for-non-existing-node
https://msdn.microsoft.com/en-us/library/ms256086(v=vs.110).aspx
'''

Bangumi = "http://bangumi.tv"
noRating = "N/A"



def search(namewords):
    name = ''
    if len(namewords) == 1:
        name = namewords[0]
    else:
        for w in namewords:
            name += w
            name += '+'
        name = name[:-1]
    pageURL = "http://bangumi.tv/subject_search/{}?cat=2".format(name)
#    resource = requests.get(pageURL).text
    resource = getSourceCode(pageURL)
    tree = etree.HTML(resource)
    
    divs = tree.xpath('//div[@class="inner"]')
    divs.pop(0)
    divs.pop(-1)
    
    dates = []
    links = []
    ratings = []
    for div in divs:
        title = div.xpath('h3/a/text()')[0]
        if div.xpath('boolean(h3/small)'):
            sub = div.xpath('h3/small/text()')[0]
        if not nameMatch(title, namewords) and not nameMatch(sub, namewords):
            continue
        
        date = div.xpath('p[1]/text()')[0]
        dayi = date.find('日')
        # Find the index to save exact date info and strip all others. Sometimes
        # there is only year but no '日' character; strip the spaces directly in
        # this case
        if dayi == -1:
            date = date.strip()
        else:
            date = date[:dayi + 1].strip()
        dates.append(date)
        
        link = div.xpath('h3/a/@href')[0]
        links.append(link)
        
        if div.xpath('boolean(p[2]/small)'):
            rating = div.xpath('p[2]/small/text()')[0]
            ratings.append(rating)
        else:
            ratings.append(noRating)
    
    #t1 = divs[1].xpath('h3/a/text()')
    #b1 = divs[5].xpath('boolean(span)')
    #b2 = divs[6].xpath('boolean(span)')
    #b3 = divs[7].xpath('boolean(p[1])')
    #b4 = divs[7].xpath('boolean(p[2])')
    #b5 = divs[8].xpath('boolean(p[1])')
    #b6 = divs[8].xpath('boolean(p[2])')
    ##ps = tree.xpath('//p[parent::div]')
    ##pst = tree.xpath('//p[@]/text()')

    #titles = tree.xpath('//h3/a/text()')
    
    #dates = tree.xpath('//p[@class="info tip"]/text()')
    #for i in range(len(dates)):
        #date = dates[i]
        #dates[i] = date[:date.find('日') + 1].strip()

    #links = tree.xpath('//h3/a/@href')

    #ratings = tree.xpath('//small[@class="fade"]/text()')

    #removeInds = []
    #for i in range(len(titles)):
        #if not nameMatch(titles[i], namewords):
            #removeInds.append(i)
    #for i in range(len(removeInds)):
        #removeInds[i] = removeInds[i] - i
    #for ind in removeInds:
        #dates.pop(ind)
        #links.pop(ind)
        #ratings.pop(ind)

    ind = dates.index(min(dates))
    return ratings[ind], Bangumi + links[ind]
    
#    sc = urllib.request.urlopen(URL).read().decode()

#    sc, URL = getURL(sc)
#    Rating = getRating(sc)
    
#    return Rating, URL

##    return "7.2", "http://bangumi.tv/subject/9781"



def getSourceCode(url):
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        return getSourceCode(url)



def nameMatch(t, words):
    '''
    Return a "matched" that represents if every keyword searched in 
    keyword list "words" exists in title "t".
    
    Keywords have been parsed before being sent to this searcher module, so only
    parse the title got from the web here. Set a flag to True first, and then 
    check every word: if any word is found not matching, terminate the check and
    return False.
    '''
    t = parseZH(t)
    matched = True
    for w in words:
        if w.lower() not in t.lower():
            matched = False
            break
    return matched

def getURL(sourceCode):
    i = sourceCode.find("/subject/")
    sc = sourceCode[i:]
    i = sc.find("\"")
    return sc, Bangumi + sc[:i]


def getRating(sourceCode):
    i = sourceCode.find("fade")
    if i == -1:
        return '   '
    i += 6
    return sourceCode[i:i+3]






##search("gosick")
