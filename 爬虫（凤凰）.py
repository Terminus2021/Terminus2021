import requests
import bs4
response = requests.get("http://news.ifeng.com").text
soup = bs4.BeautifulSoup(response,"html.parser").find_all(name = "div",class_="lunbo-1_Y0ffLY")
for da in soup:
    d = da.find_all(name = "a")
    dic1 = {
        d[0].text,
        d[1].text,
        d[2].text,
        d[3].text,
        d[4].text,
        d[5].text}
    print("\n")
    for key in dic1:
        print("凤凰网即时新闻：",key)
        
