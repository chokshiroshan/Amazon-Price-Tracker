import requests as rq
import bs4,smtplib,time

link = 'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXC7QS4/ref=sr_1_1?keywords=s10%2B&qid=1562436588&s=gateway&sr=8-1'

def checkPrice():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    data = rq.get(link,headers=headers)

    soup = bs4.BeautifulSoup(data.content,'lxml')

    title = soup.find('span',{'id':'productTitle'}).text.strip()

    price = soup.find('span', {'id': 'priceblock_ourprice'})
    if price == None:
        price = float(soup.find('span', {'id': 'priceblock_dealprice'}).text.strip().replace(",", '')[2:])
    else:
        price =float(price.text.strip().replace(",", '')[2:])

    return price,title

def sendEmail(title):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('roshan2722000@gmail.com','#####')
    subject = 'Price of {} is Changed!'.format(title)
    body = "Check Amazon Link : {}".format(link)
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'roshan2722000@gmail.com',
        'chokshiroshan@gmail.com',
        msg
    )
    print("Email has been sent!")

current,title = checkPrice()
# print(title)
while True:
    if current == checkPrice()[0]:
        sendEmail(title)
        current = checkPrice()
    time.sleep(21600)