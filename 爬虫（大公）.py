import requests
import bs4
response = requests.get("http://www.takungpao.com").text
soup = bs4.BeautifulSoup(response,"html.parser").find_all(name = "div",class_="swiper-slide")
for da in soup:
    d = da.find_all(name = "a")
    dic1 = {
        d[0].text,
        d[1].text,
                }
    print("\n")
    for key in dic1:
        print(key)
