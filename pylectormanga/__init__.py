from bs4 import BeautifulSoup
from dataclasses import asdict
from .lectormanga import PyLectorManga

from .network import GET
from .model import DetailsSimpleManga
from .page import LECTORMANGA

def search(manga: str) -> list:
    response = GET(LECTORMANGA + manga.replace(' ', '+'))
    soup = BeautifulSoup(response.content, "html.parser")

    section_results = soup.find('div', 'col-12 col-lg-8 col-xl-9')
    results = []

    if not section_results.find('h2', 'display-5'):
        for result in section_results.find_all('div', 'col-6 col-md-3 col-lg-3 mt-2'):
            title = result.find('div', 'card-header p-1 text-light text-truncate').find('a')['title']
            url = result.find('div', 'card-header p-1 text-light text-truncate').find('a')['href']
            image = result.find('div', 'card-body p-0').find('img')['src']
            classification = str(result.find('div', 'card-footer p-0 px-2 text-center').find('span', 'float-left').text).strip()
            type = result.find('div', 'card-footer p-0 px-2 text-center').find('span', 'float-right').text

            if not classification:
                classification = None

            data = DetailsSimpleManga(title, image, classification, type, url)
            results.append(asdict(data))

        return results
    else:
        return results
    
__all__ = ['search', 'PyLectorManga']