import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def extract_indeed_pages():
  indeed_result = requests.get(URL)
  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
  pagination = indeed_soup.find("div",{"class":"pagination"})
  links = pagination.find_all('a')
  spans = []
  for link in links[:-1]:
    spans.append(int(link.text))
  last_page = spans[-1] + 6
  return last_page

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page * LIMIT}")
    print(result.status_code)
  return jobs
  