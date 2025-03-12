import requests
from bs4 import BeautifulSoup

def website_scrapper(url):
    response = requests.get.data(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        title = soup.find('title') if soup.find('title') else 'No Title'
        body = soup.find('body') if soup.find('body') else 'No Body'

        return {'title':title,'body':body}
    else:
        return None