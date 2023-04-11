import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os


url = "https://www.eksisozluk.com"
# arananKelime = input("aranan kelimeyi giriniz:")
# arananTarihBaşlangıcı = input("Başlangıç tarihini giriniz:")
arananKelime = "deprem"
arananTarihBaslangici = "06022023"
# webdriver'ı başlatma
driver = webdriver.ChromiumEdge()
# siteye ulaşma
driver.get(url)
time.sleep(5)
print("1")
filtreleme = driver.find_element(By.ID, 'a3-toggle')
filtreleme.click()
print("2")
driver.implicitly_wait(3)
arananKelimeKutusu = driver.find_element(By.ID, 'SearchForm_Keywords')
arananKelimeKutusu.click()
print("3")
arananKelimeKutusu.send_keys(arananKelime)
tarihAraligiBaslangicKutusu = driver.find_element(
    By.ID, 'SearchForm_When_From')
tarihAraligiBaslangicKutusu.send_keys(arananTarihBaslangici)
aramaButonu = driver.find_element(
    By.XPATH, '//*[@id="advanced-search-form"]/div[6]/button')
aramaButonu.click()
print("4")
time.sleep(15)
print("5")
# başlıklara tıklama
sozluk = {}
for i in range(1, 51):
    basliklar = driver.find_element(
        By.XPATH, f'//*[@id="partial-index"]/ul/li[{i}]')
    basliksplit = basliklar.text
    baslik = basliksplit.split("\n")
    baslik1=baslik[0]
    baslik2= baslik1.replace(" ","")

    klasor = r'C:\Users\Utku\Desktop\EksiSozluk'
    dosya_adi = f'{baslik2}.xlsx'
    dosya_yolu = os.path.join(klasor, dosya_adi)

    if os.path.exists(dosya_yolu):
        print("Dosya var.")
        continue
    else:
        print("Dosya yok.")
    print(baslik2)
    sozluk[baslik2] = []
    basliklar.click()
    time.sleep(5)

    # başlıkların sayısını bulma
    pagecountcontrols = driver.find_elements(
        By.CLASS_NAME, 'pager')
    sayfa = 0
    for pagecountcontrol in pagecountcontrols:
        sayfaSayisi = pagecountcontrol.find_element(By.CLASS_NAME, "last")
        # sayfa sayısını bulduk
        sayfa = int(sayfaSayisi.text)
        print("sayfa sayısı: "+str(sayfa))

    for i in range(2, sayfa+1):
        entrys = driver.find_elements(By.ID, "topic")
        for entry in entrys:
            # print(entry.text)
            metinElementi = entry.find_elements(By.CLASS_NAME, "content")
            for metinler in metinElementi:
                metin = metinler.text
                print(metin)
                sozluk[baslik2].append(metin)
        url = driver.current_url
        index = url.find("&p=")
        value = url[index + 3:]
        if "&p=" in url:
            url = url[:index + 3] + str(i)
            driver.get(url)
            print("if")
        else:
            url = url + "&p=" + str(i)
            driver.get(url)
            print("else")
        i += 1
        print("başlıklar:" + baslik2)
        print(url)
        dosya_adi = baslik2+".xlsx"

        time.sleep(1)
        df = pd.DataFrame(sozluk)
        df.to_excel(f'{baslik2}.xlsx', sheet_name="Sheet1", index=False)
        print(i)
    sozluk={}

        # if os.path.isfile(dosya_adi):
        #     print("Dosya mevcut.")
        #
        #     df = pd.DataFrame(sozluk)
        #     writer = pd.ExcelWriter(f'{baslik2}.xlsx', engine='openpyxl')
        #     writer.book = book
        #     df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
        # else:
        #     print("Dosya mevcut değil.")
        #     df = pd.DataFrame(sozluk)
        #     df.to_excel(f'{baslik2}.xlsx', index=False)
#######################################################################

# url = driver.current_url
# source = driver.page_source
# soup = BeautifulSoup(source, "html.parser")
# try:
#     page_count = len(soup.find("div", {"class": "clearfix sub-title-container"}).find(
#         "div", {"class": "pager"}).find_all("option"))
# except:
#     page_count = 1
# print(page_count)

# headers = {
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac os X 10_14_6) AppleMebkit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15"}
# for i in range(1, page_count + 1):
#     response = requests.get(url + "?p=" + str(i), headers=headers)
#     # print(url + "?p=" + str(i))
#     time.sleep(2)
#     soup = BeautifulSoup(response. content, "html.parser")
#     entry_divs = soup.find_all("div", {"class": "content"})
#     for entry in entry_divs:
#         print(entry.text)
#         footer = entry.findNext("footer")
#         author = footer.find_all("a")[1].text
#         print("yazar: " + author)
#         print("*"*100)

print("Anneee bitti")


# text = []
# authors = []

# headers = {
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac os X 10_14_6) AppleMebkit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15"}
# for i in tqdm(range(1, page_count + 1)):
#     response = requests.get(url + "?p=" + str(i), headers=headers)
#     #print(url + "?p=" + str(i))
#     time.sleep(2)
#     soup = BeautifulSoup(response. content, "html.parser")
#     entry_divs = soup.find_all("div", {"class": "content"})
#     for entry in entry_divs:
#         print(entry.text)
#         text.append(entry.text)
#         footer = entry.findNext("footer")
#         author = footer.find_all("a")[0].text
#         print("yazar: " + author)
#         authors.append(author)


# browser.close()
