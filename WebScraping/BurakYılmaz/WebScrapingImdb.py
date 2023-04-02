from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import statistics

service=Service(executable_path="C:\\Users\\burak\\Desktop\\enjoy\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://m.imdb.com/chart/top//")
driver.maximize_window()
time.sleep(3)

page_title = driver.find_element(By.CLASS_NAME,"header-gray")
print(page_title.text)
time.sleep(3)

movie_titles = driver.find_elements(By.XPATH,'//h4')
movie_ratings = driver.find_elements(By.CLASS_NAME,'imdb-rating')
#movie_years = driver.find_elements(By.CLASS_NAME, 'unbold')


for i in range(len(movie_titles)):
    print(f"{movie_titles[i].text} - {movie_ratings[i].text} ")

ratings = [float(rating.text.replace(',', '.')) for rating in movie_ratings]

print(f"Mod: {statistics.mode(ratings)}")
print(f"Medyan: {statistics.median(ratings)}")
print(f"Standart Sapma: {statistics.stdev(ratings)}")
print(f"Ortalama: {statistics.mean(ratings)}")
print(f"En Yüksek Puan: {max(ratings)}")
print(f"En Düşük Puan: {min(ratings)}")