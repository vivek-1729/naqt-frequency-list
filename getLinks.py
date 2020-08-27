from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests, pickle, os

def getLinks():
    parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
    for i in range(1,100):
        if os.path.exists('pdfs/' + str(i)):
            print(str(i),'already exists')
            continue
        resp = requests.get("https://quizbowlpackets.com/"+str(i))
        http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(resp.content, parser, from_encoding=encoding)

        links = []

        allLinks = soup.find_all('a', href=True)
        combined = [True if 'pdf' in link['href'] else False for link in allLinks]
        if not any(combined):
            print(str(i), 'doesn\'t exist')
            continue

        for link in allLinks:
            link = link['href']
            if 'Packet' in link:
                links.append(link)
        print(links)
        with open('pdfs/' + str(i),'wb') as file:
            pickle.dump(links, file)
getLinks()