import requests
from bs4 import BeautifulSoup

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):


    headline = article.h2.a.text
    print()
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch/?v={vid_id}'

        pass
    except Exception as e:
        yt_link = None

        raise e
    print(yt_link)


