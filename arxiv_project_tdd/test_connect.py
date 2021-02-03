import unittest
import requests
from bs4 import BeautifulSoup


class ConnectTest(unittest.TestCase):

    def test_connect(self):
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100")
        soup = BeautifulSoup(arxiv.text,'html.parser')
        assert arxiv.status_code == 200

    def test_connect_param(self):
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100", params={"query":"python"})
        soup = BeautifulSoup(arxiv.text,'html.parser')
        title = soup.find("span",{"class":"mathjax"})
        assert arxiv.status_code == 200 and "python" in title

    def test_get_pages(self):
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100", params={"query":"python"})
        soup = BeautifulSoup(arxiv.text,'html.parser')
        pagination = soup.find("nav",{"class":"pagination"})
        links = pagination.find_all('li')
        pages = []
        for link in links:
            pages.append(link.find("li").string)
        print(pages)



if __name__ == '__main__':
    unittest.main()

    #main-container > div.level.is-marginless > div.level-left > h1 > span