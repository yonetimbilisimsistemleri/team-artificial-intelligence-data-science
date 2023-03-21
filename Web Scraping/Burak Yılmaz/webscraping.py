from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver_service = Service(executable_path="C:\\Users\\burak\\Desktop\\enjoy\\chromedriver.exe")
driver= webdriver.Chrome(service=driver_service)


driver.get("https://www.sikayetvar.com/")
driver.maximize_window()
time.sleep(3)
searchbar=driver.find_element(By.NAME,"brand")
searchbar.send_keys("aras kargo\n")
time.sleep(3)

print("Şikayet Sayısı ") 
complaintNo= driver.find_element(By.XPATH,("//*[@id='main-wrapper']/main/div/div/div[2]/div[2]/div/div[2]/div[1]/strong"))
print(complaintNo.text)
time.sleep(2)
          
solutionNo=driver.find_element(By.XPATH,("//*[@id='main-wrapper']/main/div/div/div[2]/div[2]/div/div[2]/div[2]/a/strong"))
print("Çözüm Sayısı") 
print(solutionNo.text)
time.sleep(2)

for i in range(1,6):
    print(f"Şikayet {i} Bilgileri:")
    userName = driver.find_element(By.XPATH,f'//*[@id="main-content"]/div[1]/div[2]/article[{i}]/header/div/div[1]/a')
    print("Kullanıcı Adı") 
    print(userName.text) 
    time.sleep(2)

    textDate = driver.find_element(By.XPATH,f'//*[@id="main-content"]/div[1]/div[2]/article[{i}]/header/div/div[2]/div[2]')
    print('Tarih') 
    print(textDate.text)
    time.sleep(2)
    
    print(f"Şikayet {i}")
    print("Sorun")
    
    complaint_title= driver.find_element(By.XPATH,f'//*[@id="main-content"]/div[1]/div[2]/article[{i}]/section/h2/a')
    print(complaint_title.text)
    complaint_title.click()

    complaint1 = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/article/div[2]/div[2]')
    print(complaint1.text)
    time.sleep(2)

    solution1 = driver.find_element(By.XPATH,'//*[@id="main-content"]/section[2]/article/div[3]/div[2]/div/p')
    print("Çözüm")
    print(solution1.text)
    time.sleep(2)
    
    driver.back()
    time.sleep(2)

