import time
from selenium import webdriver
import webbrowser
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


baslik = "iphone"
# baslik = input("aranan değer: ")
url = "https://www.sikayetvar.com/sikayetler"
browser = webdriver.ChromiumEdge()

time.sleep(4)
browser.get(url)
print("url açıldı")
input_area = browser.find_element(By.ID, "text-autocomplete")
print("arama butonu bulundu")
browser.maximize_window()
print("tam ekran yapıldı")

input_area.send_keys(baslik)
print("arama yerine key gönderildi")
button = browser.find_element(
    By.XPATH, "//*[@id='header-autocomplete']/button")
print("button bulundu")
button.click()
print("butona tıklandı")
time.sleep(4)

url = browser.current_url
source = browser.page_source
soup = BeautifulSoup(source, "html.parser")
print("url,source,soup atandı")
print(url)
# //*[@id="main-content"]/div[1]/div[2]/article[7]/section
# //*[@id="main-content"]/div[1]/div[2]/article[8]/section
page_count = soup.find("div", {"class": "pagination-wrap"}).find(
    "ul", {"class": "pagination ga-v ga-c"}).find_all("li")[6].get_text(strip=True)
# eğer son sayfa numarasının yeri sabit olsaydı buradan yapabilirdik
# sayfa = browser.find_element(By.XPATH,"//*[@id='main-content']/div[1]/div[2]/div[9]/ul/li[7]")
sayfa = int(page_count)
print("sayfa sayısı:", sayfa)

for page in range(2, sayfa+1):

    print(url + "?p=" + str(page))

    time.sleep(3)
    # response = requests.get(url + baslik + "?page=" + str(page))
    browser.get(url + "?page=" + str(page))
    articles = browser.find_elements(By.TAG_NAME, "article")
    for article in articles:
        sections = article.find_elements(By.TAG_NAME, "section")
        for section in sections:
            a_element = section.find_element(By.TAG_NAME, "a")
            aText = a_element.text
            p_element = section.find_element(By.TAG_NAME, "p")
            pText = p_element.text
            print("Başlık: ", aText)
            print(
                "*******************************************************************************")
            # section içindeki p etiketindeki metni al

            print("Şikayet: ", pText)
            print(
                "*******************************************************************************")
    page += 1

# https://www.sikayetvar.com/iphone?page=5
print("6")
# browser.close()
