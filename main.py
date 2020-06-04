import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100"
response = requests.get(url)


bs = BeautifulSoup(response.text, "html.parser")
get_list = bs.find_all("button", {"class": "chart-element__wrapper"})
billboard_rank = []

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
        "span", {"class": "chart-element__image"})["style"]
    print(get_albumcover)
    billboard_rank.append({"TITLE": get_title, "ARTIST": get_artist, "THIS WEEK": get_rank,
                           "LAST WEEK": get_last_rank[0], "PEAK": get_peak_rank[0], "DURATION": get_duration_rank[0]})
