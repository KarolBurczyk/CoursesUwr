from bs4 import BeautifulSoup
import urllib.request
import re

visited = {}

url = 'https://ii.uni.wroc.pl/'


def crawl(start_page, distance, action):
    try:
        response = urllib.request.urlopen(start_page)
    except urllib.error.URLError:
        print('URL Error')
        return
    except urllib.error.HTTPError:
        print('HTTP Error')
        return
    except:
        print('Unknown Error')
        return
        
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    visited[start_page] = True
    try:
        res = action(html.decode('utf-8'))
    except UnicodeDecodeError:
        res = 'Failed to decode'
    yield (start_page, res)
    if distance > 0:
        for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
            if link.get('href') not in visited:
                yield from crawl(link.get('href'), distance - 1, action)


for url, wynik in crawl(url, 2, lambda tekst: 'Python' in tekst):
    print(f'{url}: {wynik}')