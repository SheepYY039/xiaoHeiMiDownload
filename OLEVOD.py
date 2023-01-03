import re
from typing import Any

import requests
from bs4 import BeautifulSoup, ResultSet

from Show import Show, Source
from fake_useragent import UserAgent
import cloudscraper

ua = UserAgent()


def search_olevod(query: str) -> [Show]:
    search_url: str = f"https://www.olevod.com/index.php/vod/search.html?wd={query}&submit="
    scraper = cloudscraper.create_scraper(delay=10, browser={ 'custom': 'ScraperBot/1.0', })
    search_result_page = scraper.get(search_url).content
    query_result_soup: BeautifulSoup = BeautifulSoup(search_result_page, 'html.parser')
    query_results: ResultSet[Any] = query_result_soup.find_all('li', attrs={ 'class': 'searchlist_item' })
    result_list = []
    result_index: int = 1

    for result in query_results:
        show = Show(result, Source.OLEVOD)
        result_list.append(show)
    return result_list