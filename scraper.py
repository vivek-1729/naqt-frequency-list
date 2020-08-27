from bs4 import BeautifulSoup
import urllib, pickle
def getLists(url):
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html)
    labels = soup.findAll("i", {"class":"label"}) #Note: Span instead of i for volcanoes
    data=[str(b.string) for b in labels]
    lists = soup.findAll("li")
    allVals = []
    firstVals = []
    for i in lists:
        if len(firstVals) != 0:
            allVals.append(firstVals)
        firstVals = []
        b = str(i)
        if 'label' in b:
            val = b
            val = val.split('<span class="ygk-term">')[1:]
            for j in val:
                new = j.split('<')[0]
                firstVals.append(new)
    # print(allVals)
    print(data)
    with open('allvals','wb') as file:
        pickle.dump(allVals,file)
    with open('data','wb') as file:
        pickle.dump(data,file)
getLists('https://www.naqt.com/you-gotta-know/american-plays.html')