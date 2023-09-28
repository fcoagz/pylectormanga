from bs4 import BeautifulSoup
from dataclasses import asdict

from .network import GET
from .model import DetailsChapters, DetailsManga, LectorManga

class PyLectorManga:
    def __init__(self, url) -> None:
        response = GET(url)
        self.soup = BeautifulSoup(response.content, "html.parser")

    def get_manga_information(self) -> dict[str, str]:
        details_section = self.soup.find('div', 'col-12')
        
        image = details_section.find('div', 'col-12 col-sm-3 text-center').find('img')['src']
        title, date = details_section.find('div', 'col-12 col-sm-9').find('h1').getText('\n', strip=True).split('\n')
        # status = details_section.find('div', 'col-12 col-sm-9').find('span', 'status-publishing').text
        type = details_section.find('div', 'col-12 col-sm-9').find('span', 'text-manga').text
        genre = [genre.text for genre in details_section.find_all('a', 'badge badge-primary badge-pill py-2 px-2 my-1')]
        description = details_section.find('div', 'col-12 mt-2').find('p').text
        
        data = DetailsManga(title, image, description, date, type, genre)

        return asdict(data)
    
    def get_all_the_chapters(self) -> list:
        chapter_section = self.soup.find('div', id='chapters')
        
        title = [title.find('h4')['title'] for title in chapter_section.find_all('div', 'col-10 col-md-11')]
        chapter_number = [number.split(' ')[1] for number in title]
    
        information_extra = []
        for editors in chapter_section.find_all('li', 'list-group-item'):
            # credits = editors.find('div', 'col-12 col-sm-12 col-md-4 text-truncate').text
            # if 'Buitres Scan' in credits:
            information_extra.append(editors)
        
        editor = [str(editor.find('div', 'col-12 col-sm-12 col-md-4 text-truncate').text).strip() for editor in information_extra]
        date = [str(date.find('span', 'badge badge-primary p-2').text).strip() for date in information_extra]
        url = [url.find('div', 'col-6 col-sm-2 text-right').find('a')['href'] for url in information_extra]

        chapters = []
        for t, num, ed, d, u in zip(title, chapter_number, editor, date, url):
            chapter = DetailsChapters(t, num, ed, d, u)
            chapters.append(asdict(chapter))

        return chapters
    
    def get_one_chapter(self, chapter_number: str): # download: bool = False, filename: str = None):
        chapters = self.get_all_the_chapters()

        for chapter in chapters:
            if chapter_number == str(chapter['chapter_number']):
                return chapter
            else:
                return None
                # 
                # response = GET(chapter['url'])
                # soup = BeautifulSoup(response.content, "html.parser")

                # section_image = soup.find_all('div', id='main-container')
                # image = [image.find('div', 'viewer-image-container').find('img')['src'] for image in section_image]
                
                # return image