import requests
from bs4 import BeautifulSoup


def extractResult(html):

  title = html.find("h3", {"class": "ipQwMb"}).string

  pressName = html.find("div", {"class": "QmrVtf"}).find("a").string

  link = html.find("a")["href"]

  return {"title": title, "pressName": pressName, "link": link}



def extractResults(URL):
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  results = soup.find("div", {"class": "ajwQHc"}).find("div", {"class": "lBwEZb"}).find_all("div", {"class": "NiLAwe"})

  results = results[0:50]

  fake_Db = []

  for result in results:

    oneInfo = extractResult(result)

    fake_Db.append(oneInfo)

  return fake_Db


def getResults():
  URL = [
    "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFp4WkRNU0FtdHZLQUFQAQ?hl=ko&gl=KR&ceid=KR%3Ako",
    "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako",
    "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako",
    "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako",
    "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"
    ]

  DB = [0, 0, 0, 0, 0]

  for num in range(5):
    print(f"Scrapping News Pages {num+1}...")
    DB[num] = extractResults(URL[num])

  return DB