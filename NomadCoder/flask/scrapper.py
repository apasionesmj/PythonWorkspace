import requests
from bs4 import BeautifulSoup

def get_last_page(url): #최종페이지 가져오기
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True) # 맨 마지막 페이지는 -1, 그 전 페이지는 -2
    return int(last_page)

def extract_job(html):
    title = html.find("h2").find("a")["title"]
    # unpacking value -----> 이미 요소가 몇개인지 정확하게 알고 있을때 가능. company, location
    # # recursive=False 더 이상 깊게 들어가지 않도록.
    # 현재 h3 안에 span이 두가지가 있기 때문에 company, location 같은 unpacking value 사용하기
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\r").strip("\n")
    job_id = html['data-jobid']
    return{
        'title':title, 
        'company':company, 
        'location':location, 
        'apply_link':f"https://stackoverflow.com/jobs/{job_id}"
        }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page : {page}")
        result = requests.get(f"{url}&pg={page + 1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}&sort=i"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs 