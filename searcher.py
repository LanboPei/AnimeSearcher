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

Character language check
https://blog.csdn.net/max_r/article/details/30219035
'''

Bangumi = "http://bangumi.tv"
noRating = "N/A"


def search(name):
    '''
    Return the rating and page url of the searched anime on Bangumi.
    
    @param name: Name input as the anime to be searched.
    '''
    
    bgmName = name.replace(' ', '+') #Format in BGM searching url
    if not bgmName.encode('UTF-8').isalpha():
        bgmName = parseZH(bgmName)
    pageURL = "http://bangumi.tv/subject_search/{}?cat=2".format(bgmName)
    source = getSourceCode(pageURL) #Request source code
    return filtered(source, name)
        #Analyse source code to find most appropriate result, then return.


def parseZH(zhString):
    return urllib.parse.quote(zhString)


def getSourceCode(url):
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        return getSourceCode(url)


def filtered(source, name):
    '''
    Return the rating and page url of the most appropriate result among all the
    results listed in the search result page.
    
    @param source: source code in bytes form of the search result page.
    @param name: Name input as the anime to be searched.
    '''
    
    tree = etree.HTML(source)
    
    divs = tree.xpath('//div[@class="inner"]')
    if len(divs) <= 2:
        return None, None
    
    divs.pop(0)
    divs.pop(-1)
    
    dates = []
    links = []
    ratings = []
    for div in divs:
        title = div.xpath('h3/a/text()')[0]
        if div.xpath('boolean(h3/small)'):
            sub = div.xpath('h3/small/text()')[0]
        if not title.lower() in name.lower() and \
           not sub.lower() in name.lower():
            continue
        
        date = div.xpath('p[1]/text()')[0]
        dayi = date.find('日')
            #Find the index to save exact date info and strip all others.
            #Sometimes there is only year but no '日' character; strip the spaces
            #directly in this case.
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

    ind = dates.index(min(dates))
    return ratings[ind], Bangumi + links[ind]
