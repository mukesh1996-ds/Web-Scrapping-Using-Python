from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.edge.options import Options

options = Options()
options.headless=True
options.add_argument('window-size=1920x1080')

website = "https://www.audible.com/search"
path = r"D:\Web-Scrapping-Using-Python\selenium\msedgedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Edge(service=service,options=options)
driver.get(website)
#driver.maximize_window()

wait = WebDriverWait(driver, 10)
#container = driver.find_element(By.CLASS_NAME,"adbl-impression-container ")
container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "adbl-impression-container")))
products = container.find_elements(By.XPATH,'./li')

book_title= []
book_author = []
book_length = []


for product in products:
    book_title.append(product.find_element(By.XPATH,'.//h3[contains(@class,"bc-heading")]').text)
    book_author.append(product.find_element(By.XPATH,'.//li[contains(@class,"authorLabel")]').text)
    book_length.append(product.find_element(By.XPATH,'.//li[contains(@class,"runtimeLabel")]').text)
    
driver.quit()

data = {"title":book_title,
        "author":book_author,
        "time":book_length}

df = pd.DataFrame(data)


print(df.head())


df.to_csv("book.csv", index=False)

