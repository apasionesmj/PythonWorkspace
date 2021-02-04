import unittest
import requests
from bs4 import BeautifulSoup


class ConnectTest(unittest.TestCase):
    # ==========arxiv에서 파이썬으로 검색한 페이지 접속이 가능한가==========
    def test_connect(self):
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100")
        soup = BeautifulSoup(arxiv.text,'html.parser')
        assert arxiv.status_code == 200
    
    # ==========파라미터를 가지고 arxiv에 접속이 가능한가==========
    def test_connect_param(self):
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100", params={"query":"python"})
        soup = BeautifulSoup(arxiv.text,'html.parser')
        title_in_article = soup.find("span",{"class":"mathjax"})
        assert arxiv.status_code == 200 and "python" in title_in_article
    
    # ==========페이지를 가지고 오는가==========
    def test_get_pages(self):
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100", params={"query":"python"})
        soup = BeautifulSoup(arxiv.text,'html.parser')
        pagination = soup.find("nav",{"class":"pagination"})
        links = pagination.find_all('li')
        pages = []
        for link in links:
            pages.append(int(link.find("a").string[:1]))
        max_page = pages[-1]
        assert max_page > 0

if __name__ == '__main__':
    unittest.main()