import requests
from bs4 import BeautifulSoup


def operate(incoming):
    soup = BeautifulSoup(incoming, 'html.parser')
    return soup


def depaginate(page=1, res=''):
    while True:
        current = requests.get(f'https://quotes.toscrape.com/page/{page}').content.decode('utf-8')
        check = operate(current)
        complete = check.find('li', class_='next')
        res = res + current
        page += 1
        if not complete:
            break


    soup = operate(res)
    founded = soup.find_all('div', class_='quote')
    return founded


def collect(data):
    collected_data = {}
    for item in data:
        tags = []
        quote = item.text.split('\n')[1]
        link_autor = "https://quotes.toscrape.com/"+item.find('a').get('href')
        author = item.find('small', class_="author").text
        more = requests.get(link_autor).content.decode('utf-8')
        soup_d = BeautifulSoup(more, 'html.parser')
        descr = soup_d.find('div', class_='author-description')
        descr_text = descr.text.replace('\'', '').replace('\n', '').strip()

        autor_tags = item.find_all('a', class_='tag')
        for line in autor_tags:
            tag = line.text
            tags.append(tag)
        collected_data[quote] = {
                'author': author,
                'link': link_autor,
                'description': descr_text,
                'tags': tags
            }

    return collected_data


if __name__ == '__main__':
    founded = depaginate()
    collect(founded)
