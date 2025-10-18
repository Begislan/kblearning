import requests
from bs4 import BeautifulSoup

def newsOshsu():
    url='https://t.me/s/oshstateuni'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    data_img = soup.select('div div.tgme_widget_message_wrap div.js-widget_message div.tgme_widget_message_bubble a.tgme_widget_message_photo_wrap')
    images = []
    links = []
    for img_wrap in data_img:
        link = img_wrap['href']
        image_url = img_wrap['style'].split("('")[1].split("')")[0]
        images.append(image_url)
        links.append(link)
    arrAll = []
    for i in range (len(images)-1, -1, -1):
        if len(links) > i and len(images) > i:
            arrAll.append({
                'link':links[i] ,
                'img' : images[i]
                });


    return arrAll
newsOshsu()

def ITNews():
    url='https://t.me/s/IT_today_ru'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    data_img = soup.select('div div.tgme_widget_message_wrap div.js-widget_message div.tgme_widget_message_bubble a.tgme_widget_message_photo_wrap')
    images = []
    links = []
    for img_wrap in data_img:
        link = img_wrap['href']
        image_url = img_wrap['style'].split("('")[1].split("')")[0]
        images.append(image_url)
        links.append(link)
    arrAll = []
    for i in range (len(images)-1, -1, -1):
        if len(links) > i and len(images) > i:
            arrAll.append({
                'link':links[i] ,
                'img' : images[i]
                });


    return arrAll
ITNews()
















