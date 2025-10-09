import requests

from bs4 import BeautifulSoup

sahifa = 'https://cbu.uz/uz/'
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="exchange__item_value")
print(news[1].text)


link = "https://obhavo.uz/urgench"
sorov = requests.get(link)

soup = BeautifulSoup(sorov.text, "html.parser")

malumot = soup.find_all(class_="current-forecast")
print(f"Urganch shaxri  uchun ob havo malumoti :\n{malumot[0].text.strip()}")

link = "https://www.timeanddate.com/worldclock/uzbekistan/tashkent"
sorov = requests.get(link)

soup = BeautifulSoup(sorov.text, "html.parser")

malumot = soup.find_all(class_="h1")
print(f"Toshkent vaqti bilan soat.\n{malumot[0].text.strip()}")


