import requests
from bs4 import BeautifulSoup

search = input("Search: " )

url = requests.get("https://steamcommunity.com/market/search?appid=730&q=" + search)
soup = BeautifulSoup(url.content, "html.parser")
for i in range(1) : 

    name = soup.find("span", id="result_0_name").text
    price = soup.find("span", class_="normal_price").text
    amount = soup.find("span", class_="market_listing_num_listings_qty").text

    print(name + " " + price + "(Amount: " + amount + ")")