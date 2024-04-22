from bs4 import BeautifulSoup
import requests
import urllib.request as req

iframeurl="https://blog.naver.com/prologue/PrologueList.naver?blogId=troilos&noTrackingCode=true&directAccess=true"
url="https://blog.naver.com/prologue/PrologueList.naver?blogId=topjoys&noTrackingCode=true&directAccess=true"
res= req.urlopen(url)
soup= BeautifulSoup(res,'html.parser')

# if soup.find("dl", attrs={"class":"p_post_top"}):
dl = soup.find_all('li','p_title')
# titles = dl.select('dd > ul')
for item in dl:
    print(item.find("a").get_text())
    print(item.find("a")['href'])
# print(dl)
# 