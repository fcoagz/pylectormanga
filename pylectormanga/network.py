import requests
import cfscrape

def GET(url: str) -> requests.Response:
    scraper = cfscrape.create_scraper()
    response = scraper.get(url, timeout=10.0, allow_redirects=False)

    if response.status_code != requests.codes.ok:
        raise ValueError(f"Page connection error. The code status is not 200 to access the content: {response.status_code}")
    return response