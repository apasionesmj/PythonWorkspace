import requests
from bs4 import BeautifulSoup

LIMIT = 100
URL=f"https://arxiv.org/search/?query=python&searchtype=title&size={LIMIT}"

def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    # 페이지 추출하기
    pagination = soup.find("nav",{"class":"pagination"})
    links = pagination.find_all('li')
    pages = []
    for link in links:
        pages.append(int(link.find('a').string[:1])) # 'a'에 \n 이 붙어있어서 [:1]로 자름
    max_page = pages[-1] # 마지막 페이지는 pages 안에서 제일 뒤에 있는 페이지
    return max_page

def extract_scholar(last_page):
    scholar = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("li",{"class":"arxiv-result"})
    for result in results:
        title = result.find("p",{"class":"title"}).text.strip()
        authors = result.find_all("p",{"class":"authors"})
        dic = {title : [authors]}


        for result1 in authors:
            result2 = result1.find_all("a")
            for author in result2:
                print("[title] : " +title+ "   [authors] : " +author.text)
    # for result1 in results:
    #     authors = result1.find_all("p",{"class":"authors"})
    #     for result2 in authors:
    #         author = result2.find_all("a")
    #         for realauthor in author:
    #             print(realauthor.text)


    return scholar
