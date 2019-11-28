from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('https://gall.dcinside.com/mgallery/board/lists/?id=aoegame')

soup = BeautifulSoup(html, "lxml")

stop = 0

link = soup.find_all("a", { "class" : "icon_txt_n"})

