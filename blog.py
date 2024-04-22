from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()

driver.get("https://blog.naver.com/joinjaang")
driver.implicitly_wait(3)

"""
By.ID	태그의 id값으로 추출
By.NAME	태그의 name값으로 추출
By.XPATH	태그의 경로로 추출
By.LINK_TEXT	링크 텍스트값으로 추출
By.PARTIAL_LINK_TEXT	링크 텍스트의 자식 텍스트 값을 추출
By.TAG_NAME	태그 이름으로 추출
By.CLASS_NAME	태그의 클래스명으로 추출
By.CSS_SELECTOR	css선택자로 추출
"""

time.sleep(1)

driver.switch_to.frame("mainFrame")

time.sleep(1)
driver.find_element(By.ID,'toplistSpanBlind').click()
time.sleep(1)

driver.find_element(By.XPATH,f'//*[@id="listCountToggle"]/i[1]').click()
#//*[@id="listCountToggle"]/i[1]
time.sleep(1)

driver.find_element(By.XPATH,f'//*[@id="changeListCount"]/a[5]').click()
time.sleep(1)
# driver.find_element(By.NAME,"query").send_keys(Keys.ENTER)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

titles = soup.select("#listTopForm > table > tbody > tr")

print( len( titles ) )

list3 = []

# f = open('test.txt','w')
for title in titles:
    list = title.select_one('td.title > div > span > a')["href"]
    subject = title.select_one('td.title > div > span > a').text
    
    # f.write(subject + '-----' +list + "\n" )
    list2 = ''.join(list.split())
    # print( list )
    item = {}
    item["subject"] = subject + ""
    b = list.split("?")[1].split("&")
    for c in b:
        e = c.split("=")
        item[ e[0] ] = e[1]
    list3.append(item)
with open("test.json", 'w',encoding='utf-8') as outfile:
    json.dump(list3, outfile,sort_keys=True, indent=4,ensure_ascii=False)

# f.close()
# list4_sr = pd.Series(list3)
# print(list4_sr)


# for i in range(1, 3):
#     req = driver.page_source
#     soup = BeautifulSoup(req, 'html.parser')
#     titles = soup.select("#main-area > div:nth-child(5) > table > tbody > tr")
#     # #main-area > div.article-board.result-board.m-tcol-c > table > tbody
    
#     # print('------------------------')

#     # print(titles)
#     # print('------------------------')

#     print('----' + str(i) + ' 번째 페이지 -----')
#     list3 = []

#     for title in titles:
#         list = title.select_one(' td.td_article > div.board-list > div > a')["href"]
#         list2 = ''.join(list.split())
#         list3.append(list2)

#     list4_sr = pd.Series(list3)
#     print(list4_sr)

#     # for a in range(1, 3):
#         # driver.find_element_by_xpath(f'//*[@id="main-area"]/div[5]/table/tbody/tr[{a}]/td[1]/div[2]/div/a').click()
#         # time.sleep(3)
#         # driver.back()
#         # time.sleep(2)
#         # driver.switch_to.frame("cafe_main")
#     if i<2:
#         driver.find_element(By.XPATH,f'//*[@id="main-area"]/div[7]/a[{i}+1]').click()