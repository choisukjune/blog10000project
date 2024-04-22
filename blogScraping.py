from bs4 import BeautifulSoup
import requests
import urllib.request as req

def get_blog_contents(blogId, postId):
    # iframeurl="https://blog.naver.com/prologue/PrologueList.naver?blogId=troilos&noTrackingCode=true&directAccess=true"
    url="https://blog.naver.com/PostView.naver?blogId=" + blogId + "&logNo=" + postId + ""
    res= req.urlopen(url)
    soup= BeautifulSoup(res,'html.parser')

    if soup.find("div", attrs={"class":"se-main-container"}):
        text = soup.find("div", attrs={"class":"se-main-container"}).get_text()
        text = text.replace("\n","") #공백 제거
        #print(text)    
        return text
    return "error"
# https://blog.naver.com/PostView.naver?blogId=joinjaang&logNo=223415514985&categoryNo=44&parentCategoryNo=&from=thumbnailList

result = get_blog_contents( "happy_krx", "223419272947" )
# /topjoys/223421692918
print( result )