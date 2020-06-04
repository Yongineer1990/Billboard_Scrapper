import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome(
    "/Users/yong_macbook/devtool/chromedriver")  # chrome driver 경로 지정
driver.implicitly_wait(3)  # 암묵적으로 웹 자원 로드를 위해 3초 대기

url = "https://www.billboard.com/charts/hot-100"
driver.get(url)

csv_filename = "Billboard_Top100.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("Title", "Artist", "This Week",
                     "Last Week", "Peak", "Duration", "Album Cover"))

body = driver.find_element_by_css_selector("body")
for i in range(20):  # 성능이 느려지면 입력이 전달안되는 버그가 있음 (기준값 15)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

html = driver.page_source
bs = BeautifulSoup(html, "html.parser")
get_list = bs.find_all("button", {"class": "chart-element__wrapper"})


for list in get_list:
    get_title = list.find(
        "span", {"class": "chart-element__information__song"}).text
    get_artist = list.find(
        "span", {"class": "chart-element__information__artist"}).text
    get_rank = list.find("span", {"class": "chart-element__rank__number"}).text
    get_last_rank = list.find(
        "span", {"class": "text--last"}).text.split(" ")  # Last Rank Split
    get_peak_rank = list.find(
        "span", {"class": "text--peak"}).text.split(" ")  # Peak Rank Split
    get_duration_rank = list.find(
        "span", {"class": "text--week"}).text.split(" ")  # Duration Rank Split
    get_albumcover = list.find(
        "span", {"class": "chart-element__image"})["style"]  # Need Slice [23:-3]
    csv_writer.writerow((get_title, get_artist, get_rank,
                         get_last_rank[0], get_peak_rank[0], get_duration_rank[0], get_albumcover[23:-3]))
