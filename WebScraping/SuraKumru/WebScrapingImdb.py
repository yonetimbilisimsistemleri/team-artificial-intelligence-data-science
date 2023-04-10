#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import statistics

# Chrome tarayıcısını başlatın ve IMDB En İyi 250 sayfasına gidin
browser = webdriver.Chrome()
browser.get("https://www.imdb.com/chart/top/")
browser.maximize_window()

# Sayfanın yüklenmesini bekleyin
time.sleep(2)

# XPath kullanarak tüm film başlıklarını, puanlarını ve tarihlerini bulun ve listelerde saklayın
movie_titles = browser.find_elements(By.XPATH, '//td[@class="titleColumn"]/a')
movie_ratings = browser.find_elements(By.XPATH, '//td[@class="ratingColumn imdbRating"]/strong')
movie_years = browser.find_elements(By.XPATH, '//td[@class="titleColumn"]/span[@class="secondaryInfo"]')

# Film başlıklarını, puanlarını ve tarihlerini yazdırın
for i in range(len(movie_titles)):
    print(f"{movie_titles[i].text} ({movie_years[i].text.strip('()')}) - {movie_ratings[i].text}")
    

# Puanların mod, medyan, ortalama ve standart sapmasını hesaplayın
ratings = [float(rating.text) for rating in movie_ratings]
print("Mod: ", statistics.mode(ratings))
print("Medyan: ", statistics.median(ratings))
print("Ortalama: ", statistics.mean(ratings))
print("Standart Sapma: ", statistics.stdev(ratings))
print("En yüksek puan: ", max(ratings))
print("En düşük puan: ", min(ratings))

# Tarayıcıyı kapatın
browser.quit()


# In[ ]:




