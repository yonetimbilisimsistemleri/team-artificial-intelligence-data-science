from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service=Service(executable_path="C:\\Users\\burak\\Desktop\\enjoy\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.mgm.gov.tr/")
driver.maximize_window()
time.sleep(2)

user_input = str(input("Hava durumunu öğrenmek istediğiniz il, ilçe veya havalimanı ismini giriniz: \n "))
search_bar = driver.find_element(By.ID, "txtsearch")
search_bar.send_keys(user_input)
time.sleep(2)

ActionChains(driver).move_to_element(search_bar).click().perform()
ActionChains(driver).send_keys(Keys.DOWN).perform()
ActionChains(driver).send_keys(Keys.RETURN).perform()
time.sleep(2)

location = driver.find_element(By.XPATH,"//*[@id='siteBody']/section[1]/div/div[2]/div[2]/h3[1]/ziko")
print("Konum:"),print(location.text) 

date = driver.find_element(By.CLASS_NAME,"ng-binding")
print("Tarih:"),print(date.text) 

weather = driver.find_element(By.XPATH,"//*[@id='siteBody']/section[1]/div/div[2]/div[2]/div/p")
print("Hava Durumu:"),print(weather.text)

degree = driver.find_element(By.CLASS_NAME,"pull-left")
print("Sıcaklık derecesi:"),print(degree.text)

moisture = driver.find_element(By.XPATH,"//*[@id='siteBody']/section[1]/div/div[2]/div[2]/div/h3/span[2]/div/span[3]")
print("Havadaki Nem:"),print(moisture.text)

wind = driver.find_element(By.CLASS_NAME,"rHizDeger")
print("Rüzgar(km/sa):"),print(wind.text)

atmospheric_pressure = driver.find_element(By.XPATH,"//*[@id='siteBody']/section[1]/div/div[2]/div[2]/div/h3/span[2]/div/span[1]/span[2]") 
print("Atmosferik Basınç:"),print(atmospheric_pressure.text)

print("****************** BEŞ GÜNLÜK HAVA TAHMİNİ ******************")

first_day = driver.find_element(By.XPATH,"//*[@id='t1']/div/div[1]/div[1]")
print("Birinci Gün:"),print(first_day.text)
time.sleep(2)

guess_w1 = driver.find_element(By.XPATH,"//*[@id='t1']/div/div[1]/div[3]")
guess_d1_min = driver.find_element(By.XPATH,"//*[@id='t1']/div/div[1]/div[4]")
guess_d1_max = driver.find_element(By.XPATH,"//*[@id='t1']/div/div[1]/div[5]")

print("Hava Tahmini:"),print(guess_w1.text)
print("Max Sıcaklık Derecesi Tahmini"),print(guess_d1_max.text)
print("Min Sıcaklık Derecesi Tahmini"),print(guess_d1_min.text)
time.sleep(2)
print("------------------------------------")

second_day = driver.find_element(By.XPATH,"//*[@id='t2']/div/div[1]/div[1]")
print("İkinci Gün:"),print(second_day.text)

guess_w2 = driver.find_element(By.XPATH,"//*[@id='t2']/div/div[1]/div[3]")
guess_d2_min = driver.find_element(By.XPATH,"//*[@id='t2']/div/div[1]/div[4]")
guess_d2_max = driver.find_element(By.XPATH,"//*[@id='t2']/div/div[1]/div[5]")

print("Hava Tahmini:"),print(guess_w2.text)
print("Max Sıcaklık Derecesi Tahmini"),print(guess_d2_max.text)
print("Min Sıcaklık Derecesi Tahmini"),print(guess_d2_min.text)
time.sleep(2)

print("------------------------------------")

third_day = driver.find_element(By.XPATH,"//*[@id='t3']/div/div[1]/div[1]")
print("Üçüncü Gün:"),print(third_day.text)

guess_w3 = driver.find_element(By.XPATH,"//*[@id='t3']/div/div[1]/div[3]")
guess_d3_min = driver.find_element(By.XPATH,"//*[@id='t3']/div/div[1]/div[4]")
guess_d3_max = driver.find_element(By.XPATH,"//*[@id='t3']/div/div[1]/div[5]")

print("Hava Tahmini:"),print(guess_w3.text)
print("Max Sıcaklık Derecesi Tahmini"),print(guess_d3_max.text)
print("Min Sıcaklık Derecesi Tahmini"),print(guess_d3_min.text)
time.sleep(2)

print("------------------------------------")

fourth_day = driver.find_element(By.XPATH,"//*[@id='t4']/div/div[1]/div[1]")
print("Dördüncü Gün:"),print(fourth_day.text)

guess_w4 = driver.find_element(By.XPATH,"//*[@id='t4']/div/div[1]/div[3]")
guess_d4_min = driver.find_element(By.XPATH,"//*[@id='t4']/div/div[1]/div[4]")
guess_d4_max = driver.find_element(By.XPATH,"//*[@id='t4']/div/div[1]/div[5]")

print("Hava Tahmini:"),print(guess_w4.text)
print("Max Sıcaklık Derecesi Tahmini"),print(guess_d4_max.text)
print("Min Sıcaklık Derecesi Tahmini"),print(guess_d4_min.text)
time.sleep(2)

print("------------------------------------")

fifth_day = driver.find_element(By.XPATH,"//*[@id='t5']/div/div[1]/div[1]")
print("Beşinci Gün:"),print(fourth_day.text)

guess_w4 = driver.find_element(By.XPATH,"//*[@id='t5']/div/div[1]/div[3]")
guess_d4_min = driver.find_element(By.XPATH,"//*[@id='t5']/div/div[1]/div[4]")
guess_d4_max = driver.find_element(By.XPATH,"//*[@id='t5']/div/div[1]/div[5]")

print("Hava Tahmini:"),print(guess_w4.text)
print("Max Sıcaklık Derecesi Tahmini"),print(guess_d4_max.text)
print("Min Sıcaklık Derecesi Tahmini"),print(guess_d4_min.text)
time.sleep(2)

driver.quit()