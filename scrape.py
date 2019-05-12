from bs4 import BeautifulSoup
from requests import get
import pickle
import time

animu = []
page_num = 0
top_url = 'https://myanimelist.net/topanime.php?limit='
while page_num < 15651:
        page = str(page_num)
        response = get(top_url + page)

        if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                name = soup.find_all('a', class_='hoverinfo_trigger fl-l fs14 fw-b')

                for nam in name:
                        link = nam.attrs['href']
                        link_formatted = link.split('\n')[-1]
                        animu.append(link_formatted)

        else:
                print('ERROR on page: ', page, ' with response code ', response.status_code)
                break

        page_num = page_num + 50
        time.sleep(1)

with open('links.txt', 'wb') as db:
        pickle.dump(animu, db)



