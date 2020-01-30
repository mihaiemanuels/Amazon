import requests
from bs4 import BeautifulSoup
import smtplib


url = "https://www.amazon.de/dp/B07SRXGBPH/ref=dp_cerb_1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
def check_price():
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id = 'productTitle').get_text()
    print(title.strip())

    price = soup.find(id = 'price_inside_buybox').get_text()

    print(price)
    print(type(price))
    price1 = price.replace(',', '.')
    print(price1)

    converted_price = float(price1[0:14])
    print(converted_price)

    if (converted_price < 799):
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.google.com", 587)
    server.ehlo()
    setver.starttls()
    server.ehlo()
    
    server.login("mihaiemanuels@gmail.com", 'fgsohzexockalnpm')
    body = 'Check out this link:' \
           'https://www.amazon.de/dp/B07SRXGBPH/ref=dp_cerb_1'

    mesage = f"Subject:  {subject}/n/n{body}"

    server.sendmail(mihaiemanuels@gmail.com, mihaiemanuels@yahoo.com, mesage)

    print ("Email has been sent !")
    server.quit()

check_price()
