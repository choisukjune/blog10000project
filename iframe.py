from bs4 import BeautifulSoup
import requests
import urllib.request as req

# iframeurl="https://blog.naver.com/prologue/PrologueList.naver?blogId=troilos&noTrackingCode=true&directAccess=true"
url="https://blog.naver.com/troilos"
res= req.urlopen(url)
soup= BeautifulSoup(res,'html.parser')


iframe = soup.find("iframe")["src"]
print(iframe)

res= req.urlopen(iframe)
soup= BeautifulSoup(res,'html.parser')

print(soup)
# https://blog.naver.com/prologue/PrologueList.naver?blogId=troilos&noTrackingCode=true&directAccess=true