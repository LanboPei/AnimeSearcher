import urllib.request

Bangumi = "http://bangumi.tv"



def search(name):
    URL = "http://bangumi.tv/subject_search/{}?cat=2".format(name)
    sc = urllib.request.urlopen(URL).read().decode()

    sc, URL = getURL(sc)
    Rating = getRating(sc)
    
    return Rating, URL

##    return "7.2", "http://bangumi.tv/subject/9781"

def getURL(sourceCode):
    i = sourceCode.find("/subject/")
    sc = sourceCode[i:]
    i = sc.find("\"")
    return sc, Bangumi + sc[:i]


def getRating(sourceCode):
    i = sourceCode.find("fade") + 6
    return sourceCode[i:i+3]






##search("gosick")
