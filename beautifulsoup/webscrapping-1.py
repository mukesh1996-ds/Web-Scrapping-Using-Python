import requests
from bs4 import BeautifulSoup
root = "https://subslikescript.com"
website = f"{root}/movies"
result = requests.get(website)
content = result.text # to get the text 

soup = BeautifulSoup(content,"lxml")
# print(soup.prettify) # prettify is used to make html looks great

box = soup.find("article", class_="main-article")

links_list = []
for link in box.find_all("a",href=True):
    links_list.append(link["href"])

print(links_list)

for link in links_list:
    website = f"{root}/{link}"
    result = requests.get(website)
    content = result.text # to get the text 
    soup = BeautifulSoup(content,"lxml")
    box = soup.find("article", class_="main-article")
    title = box.find("h1").get_text()
    transcript = box.find("div",class_="full-script").get_text(strip=True,separator=" ")
    with open(f"{title}.txt", 'w',encoding='utf-8') as file:
        file.write(transcript)