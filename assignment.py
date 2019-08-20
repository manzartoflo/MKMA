#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:53:04 2019

@author: manzars
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from urllib.parse import urljoin

url = "https://www.mkma.org/members/list.htm"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
links_soup = soup.findAll('a')
links = []
for link in links_soup[31:-2]:
    try:
        links.append(urljoin(url, link.attrs['href']))
    except:
        pass
count = 0
number = []
name = []
email = []
website = []
names = []
for link in links:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'lxml')
    try:
        name = soup.findAll('h1')[0].text.replace('\n', '')
        datas = soup.findAll('td')
        datas = datas[2::3]
        web = ''
        em = ''
        num = []
        for data in datas:
            try:
                if("www" in data.font.text.replace('\n', '').replace('\t', '')):
                    web = data.font.text.replace('\n', '').replace('\t', '')
            except:
                pass
        
        for data in datas:
            try:
                if("@" in data.font.text.replace('\n', '').replace('\t', '')):
                    em = data.font.text.replace('\n', '').replace('\t', '')
            except:
                pass
            
        for data in datas:
            try:
                if(not any(x.isalpha() for x in data.font.text.replace('\n', '').replace('\t', '').replace('\xa0', ''))):
                    num.append(data.font.text.replace('\n', '').replace('\t', ''))
            except:
                pass
        number.append(num)
            
        if(web == ''):
            web = 'NaN'
        if(em == ''):
            em = 'NaN'
        website.append(web)
        email.append(em)
        names.append(name)
        #print(web)
        #print(email)
        print(num)
        
        
    except:
        pass
    count += 1



number_dub = []
for data in number:
    dub = []
    for x in data:
        if(len(x) >= 11):
            dub.append(x)
    number_dub.append(dub)
    
number_dub2 = []
for data in number_dub:
    if(len(data) > 2):
        data.pop()
    number_dub2.append(data)

nums = []
faxs = []

for data in number_dub2:
    num = 'NaN'
    fax = 'NaN'
    if(len(data) == 0):
        nums.append(num)
        faxs.append(fax)
    elif(len(data) == 1):
        nums.append(data[0])
        faxs.append(fax)
    else:
        nums.append(data[0])
        faxs.append(data[1])

header = 'Company Name, Telephone, Fax, Email, Website\n'
file = open('assignment.csv', 'w')
file.write(header)
for i in range(155):
    file.write(names[i].replace(',', '') + ', ' + nums[i].replace(',', ' | ') + ', ' + faxs[i].replace(',', ' | ') + ', ' + email[i].replace(',', '') + ', ' + website[i].replace(',', '') + '\n')
file.close()        







