from dataclasses import dataclass

@dataclass
class DetailsSimpleManga:
    title: str 
    image: str
    classification: str
    type: str
    url: str

@dataclass
class DetailsManga:
    title: str
    image: str
    description: str
    date: str
    type: str
    genre: list

@dataclass
class DetailsChapters:
    title: str
    chapter_number: str
    editor: str
    date: str
    url: str

@dataclass
class LectorManga:
    chapters: list