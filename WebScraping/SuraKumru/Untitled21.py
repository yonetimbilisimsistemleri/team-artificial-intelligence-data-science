#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

browser= webdriver.Chrome()
browser.get("https://www.sikayetvar.com/")
browser.maximize_window()
time.sleep(2)


searchBar= browser.find_element(By.NAME,"brand")
searchBar.send_keys("Aras Kargo\n")
time.sleep(2)


username= browser.find_element(By.XPATH,('//*[@id="main-content"]/div[1]/div[2]/article[1]/header/div/div[1]/a'))
print(username.text)
time.sleep(2)


date= browser.find_element(By.XPATH,('//*[@id="main-content"]/div[1]/div[2]/article[1]/header/div/div[2]/div[2]'))
print(date.text)
time.sleep(2)
        
complaint_title= browser.find_element(By.XPATH,('//*[@id="main-content"]/div[1]/div[2]/article[1]/section/h2/a'))
print(complaint_title.text)
complaint_title.click()
time.sleep(2)


complaint= browser.find_element(By.XPATH,('//*[@id="main-content"]/section[2]/article/div[2]/div[2]'))
print(complaint.text)
time.sleep(2)


solution = browser.find_element(By.XPATH,('//*[@id="main-content"]/section[2]/article/div[3]/div[2]/div/p'))
print(solution.text)
time.sleep(2)


# In[ ]:




