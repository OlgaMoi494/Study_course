from bs4 import BeautifulSoup
import requests
import json

def scrap_page(soup_obj, quotes_lst):
        quote_elements = soup_obj.find_all('div', class_='quote')
        for element in quote_elements:
            text = element.find('span', class_='text').text.strip('“”')
            author = element.find('small', class_='author').text
            tags = element.find('div', class_='tags').find_all('a', class_='tag')
            tags_els = []
            for tags_el in tags:
                tags_els.append(tags_el.text)
            quotes_lst.append(
                {
                    'text': text,
                    'author': author,
                    'tags': tags_els
                }
            )


def parse_logic(url_str: str) -> list:
    
    quotes = []

    page = requests.get(url_str)
    soup = BeautifulSoup(page.text, 'html.parser')
    scrap_page(soup_obj=soup, quotes_lst=quotes)
    next_page = soup.find('li', class_='next')

    while next_page:
        next_page_relative_url = next_page.find('a', href=True)['href']
        page = requests.get(url_str + next_page_relative_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        scrap_page(soup_obj=soup, quotes_lst=quotes)
        next_page = soup.find('li', class_='next')
    print(quotes)
    with open('results/data_loaded.json', 'w') as write_file:
        json.dump(quotes, write_file)
