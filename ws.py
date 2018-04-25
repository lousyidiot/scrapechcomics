from bs4 import BeautifulSoup
import requests
import webbrowser
import datetime

today = datetime.datetime.now()

source = requests.get('http://www.gocomics.com/calvinandhobbes/2018/04/25').text

weather_html=BeautifulSoup(source,'lxml')
comic = weather_html.find('a',class_="js-item-comic-link")
comic = comic.img
comic = comic['src']
webbrowser.open(comic)

