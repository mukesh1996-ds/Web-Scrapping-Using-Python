from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
path = r"D:\Web-Scrapping-Using-Python\selenium\msedgedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Edge(service=service)
driver.get(website)


all_match_button = driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
all_match_button.click()

drop_down = Select(driver.find_element(By.ID, 'country'))
drop_down.select_by_visible_text("Spain")

time.sleep(10)

matches = driver.find_elements(By.TAG_NAME,'tr')
date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home_team.append(match.find_element(By.XPATH,'./td[2]').text)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)

driver.quit()

data = {
    "date":date,
    "home_team":home_team,
    "score":score,
    "away_team": away_team
}

df = pd.DataFrame(data)

print(df.head())

# Save it 

df.to_csv("football_data.csv",index=False)
