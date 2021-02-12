# import required files and modules

import requests
from bs4 import BeautifulSoup
import smtplib
import xlsxwriter
import xlrd
import time
import matplotlib.pyplot as plt
import datetime

# url of target webpage
URL = 'https://www.amazon.in/Logitech-Hyperion-Ultra-Gaming-Mouse/dp/B00NFD0ETQ/ref=sr_1_7?dchild=1&keywords=logitech+mouse&qid=1607449308&sr=8-7'

# set the headers and user string
# my user agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

# function to check if the price has dropped
def check_price():

    # send a request to fetch HTML of the page
    page = requests.get(URL, headers=headers)

    # create the soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    try:
        title = soup.find(id="productTitle").get_text()
        # this price is in string format in the HTML page
        price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
    except AttributeError:
        print("Sorry, Try Again!")

    #converting the string amount to float
    converted_price = float(price)

    # using strip to remove extra spaces in the title
    print(title.strip())
    
    print('Amazon Price',converted_price)

    if(converted_price > 600):
        send_mail()

# function that sends an email if the prices fell down
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('tmail9571@gmail.com', 'mzrozrnfycmbhxho')

    subject = 'Price Fell Down'
    body = "Check the amazon link https://www.amazon.in/Logitech-Hyperion-Ultra-Gaming-Mouse/dp/B00NFD0ETQ/ref=sr_1_7?dchild=1&keywords=logitech+mouse&qid=1607449308&sr=8-7 "

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'tmail9571@gmail.com',
        'pradeepmahato1999@gmail.com',
        msg
    )
    #print a message to check if the email has been sent
    print('Email has been sent Succesfully')
    # quit the server
    server.quit()

def comp_price():
    
    # url of target webpage
    URL = 'https://www.flipkart.com/logitech-g402-wired-optical-gaming-mouse/p/itmf370faef36925?pid=ACCFPUEYAARTVRQT&lid=LSTACCFPUEYAARTVRQTINEVDL&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=bf33fede-3c7e-4ce5-a7da-2a714c2c3b8a.ACCFPUEYAARTVRQT.SEARCH&ppt=sp&ppn=sp&ssid=8gbu8hg3c00000001606265123775&qH=36980628a9eb87eb'

    # set the headers and user string
    # my user agent
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

    # send a request to fetch HTML of the page
    page = requests.get(URL, headers=headers)

    # create the soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    # this price is in string format in the HTML page
    price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()

    # converting the string amount to float
    converted_price = float(price)
    print('Flipkart Price',converted_price)
    
def record_data():
    # creating file workbook and worksheet
    outWorkbook = xlsxwriter.Workbook("D:\\Knowledge & Learn\\Programs\\Price Monitoring Application\\out.xlsx")
    outSheet = outWorkbook.add_worksheet()

    # declare data
    timer=0
    date1=[]
    price1=[]

    # loop that allows the program to regularly check for prices
    while(timer<5):
        n = datetime.datetime.now()
        dt = n.strftime("%H:%M:%S")
        date1.append(dt)
        new_price=price1value()
        price1.append(new_price)
        timer+=1
        time.sleep(1)

    # write headers
    outSheet.write("A1","Date")
    outSheet.write("A2","Price")

    # write data to the file.
    for item in range(len(date1)):
        outSheet.write(item+1,0,date1[item-1])
        outSheet.write(item+1,1,price1[item-1])

    outWorkbook.close()
    print("Price recorded succesfully!")

# this function returns price value foe xlsx file
def price1value():
    # url of target webpage
    URL = 'https://www.amazon.in/Logitech-Hyperion-Ultra-Gaming-Mouse/dp/B00NFD0ETQ/ref=sr_1_7?dchild=1&keywords=logitech+mouse&qid=1607449308&sr=8-7'

    # set the headers and user string
    # my user agent
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

    # send a request to fetch HTML of the page
    page = requests.get(URL, headers=headers)

    # create the soup object
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
    except AttributeError:
        print("Sorry, Try Again!")

    # converting the string amount to float
    converted_price = float(price)

    return converted_price


check_price()
comp_price()
#record_data()
#future_pre()