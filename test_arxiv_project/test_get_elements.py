import unittest
import requests
from bs4 import BeautifulSoup


class GetContentTest(unittest.TestCase):
    # ==========논문들 확인이 가능한가==========
    def test_get_thesis(self):
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100", params={"query":"python"})
        soup = BeautifulSoup(arxiv.text,'html.parser')
        results = soup.find_all("li",{"class":"arxiv-result"})
        self.assertIsNotNone(results)
    
    # ==========논문에서 title 추출이 가능한가==========
    def test_get_title_in_thesis(self):
        # Given
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100",
                            params={"query":"python"})
        soup = BeautifulSoup(arxiv.text,'html.parser')
        # When
        results = soup.find_all("li",{"class":"arxiv-result"})
        titles = []
        for result in results:
            title = result.find("p",{"class":"title"}).text.strip()
            titles.append(title)
        # Then
        self.assertRegexpMatches('cij: A Python code for quasiharmonic thermoelasticity',titles)
    
    # ==========논문에서 저자들 추출이 가능한가==========
    def test_get_authors_in_thesis(self):
        # Given
        arxiv = requests.get("https://arxiv.org/search/?query=python&searchtype=title&size=100",
                            params={"query":"python"})
        soup = BeautifulSoup(arxiv.text,'html.parser')
        # When
        results = soup.find_all("li",{"class":"arxiv-result"})
        authors_list_total = []
        for result in results: # result = 논문 1개
            authors_list_thesis = []
            authors = result.find("p",{"class":"authors"}).find_all("a")  # authors = 논문 1개의 저자들
            for result1 in authors:
                author = result1.text # author = 저자들 중 1명
                authors_list_thesis.append(author) # author_list_thesis = 논문별 저자
            authors_list_total.append(authors_list_thesis) # author_list_total = 전체 저자
        #Than
        a = ['Taewon David Kim', 'Michael Richer', 'Gabriela Sánchez-Díaz',
            'Farnaz Heidar-Zadeh', 'Toon Verstraelen',
            'Ramón Alain Miranda-Quintana', 'Paul W. Ayers']
        self.assertIn(a , authors_list_total)

if __name__ == '__main__':
    unittest.main()