import unittest
import requests
from bs4 import BeautifulSoup

arxiv = requests.get("https://arxiv.org/search/")

class ConnectTest(unittest.TestCase):
    # arxiv 홈페이지에 접속이 되는지
    def test_connect(self):
        self.assertEqual(200,requests.get("https://arxiv.org/search/").status_code)
        soup = BeautifulSoup(requests.get("https://arxiv.org/search/").text,'html.parser')

    # arxiv 홈페이지에서 파라미터를 가지고 접속이 되는지
    def test_connect_param(self):
        arxiv_param = requests.get('https://arxiv.org/search/',params={'?query':'python'})
        soup = BeautifulSoup(arxiv_param.text,'html.parser')
        self.assertEqual(200,arxiv_param.status_code)
        self.assertIn('python', soup.find("",{"class":"search-hit"}))
        # self.assertIn('python', soup)

        #.find("h1",{"class":"mathjax"}))
    # def test_connect_param(self):
    #     self.result = requests.get("https://arxiv.org/search/?query=python&searchtype=all&size=100")
    #     self.soup = BeautifulSoup(self.result.text,'html.parser')
    #     assert self.result.status_code == 200 and 'python' in self.soup.find('h1',{'class':'title'})

    # def test_get_pages
# def test_get_pages(TestCase):
#     result = requests.get("https://arxiv.org/",params={'?query':'python','searchtype':'title'})
#     soup = BeautifulSoup(result.text,'html.parser')
#     last_page = soup.find("ul",{"class":"pagination-list"})
#     max_page = int(last_page.text)
#     print(last_page)
#     TestCase.fail()
#     assert max_page > 0

if __name__ == '__main__':
    unittest.main()

    # div.level-left > h1