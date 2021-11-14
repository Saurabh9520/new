import requests
import io
import pandas as pd
from bs4 import BeautifulSoup
import re
# import cv2
from pytesseract import image_to_string
import time


drt_names = [
    {"DEBT RECOVERY APPELLATE TRIBUNAL - ALLAHABAD": ,
    "DEBT RECOVERY APPELLATE TRIBUNAL - CHENNAI": ,
    "DEBT RECOVERY APPELLATE TRIBUNAL - DELHI": ,
    "DEBT RECOVERY APPELLATE TRIBUNAL - KOLKATA": ,
    "DEBT RECOVERY APPELLATE TRIBUNAL - MUMBAI": ,
    "DEBTS RECOVERY TRIBUNAL AHMEDABAD(DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL AHMEDABAD(DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL ALLAHABAD": ,
    "DEBTS RECOVERY TRIBUNAL AURANGABAD": ,
    "DEBTS RECOVERY TRIBUNAL BANGALORE (DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL BANGALORE (DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL CHANDIGARH (DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL CHANDIGARH (DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL CHANDIGARH (DRT 3)": ,
    "DEBTS RECOVERY TRIBUNAL CHENNAI (DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL CHENNAI (DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL CHENNAI (DRT 3)": ,
    "DEBTS RECOVERY TRIBUNAL COIMBATORE": ,
    "DEBTS RECOVERY TRIBUNAL CUTTACK": ,
    "DEBTS RECOVERY TRIBUNAL DEHRADUN": ,
    "DEBTS RECOVERY TRIBUNAL DELHI(DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL DELHI(DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL DELHI(DRT 3)": ,
    "DEBTS RECOVERY TRIBUNAL ERNAKULAM(DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL ERNAKULAM(DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL GUWAHATI": ,
    "DEBTS RECOVERY TRIBUNAL HYDERABAD(DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL HYDERABAD(DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL JABALPUR": ,
    "DEBTS RECOVERY TRIBUNAL JAIPUR": ,
    "DEBTS RECOVERY TRIBUNAL KOLKATA(DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL KOLKATA(DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL KOLKATA(DRT 3)": ,
    "DEBTS RECOVERY TRIBUNAL LUCKNOW": ,
    "DEBTS RECOVERY TRIBUNAL MADURAI": ,
    "DEBTS RECOVERY TRIBUNAL MUMBAI (DRT 1)": ,
    "DEBTS RECOVERY TRIBUNAL MUMBAI (DRT 2)": ,
    "DEBTS RECOVERY TRIBUNAL MUMBAI (DRT 3)": ,
    "DEBTS RECOVERY TRIBUNAL NAGPUR": ,
    "DEBTS RECOVERY TRIBUNAL PATNA": ,
    "DEBTS RECOVERY TRIBUNAL PUNE": ,
    "DEBTS RECOVERY TRIBUNAL RANCHI": ,
    "DEBTS RECOVERY TRIBUNAL SILIGURI": ,
    "DEBTS RECOVERY TRIBUNAL VISHAKHAPATNAM"}

for index, item in enumerate(drt_names, start=1):
    print("{}: {}".format(index, item))

drt_name = drt_names[int(input("Enter Number for DRT Name which you want to select")) - 1]

print(drt_name)
party_name = input("Enter Party Name")

import json
from PIL import Image
# import pytesseract


s = requests.Session()

headers = { "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "keep-alive","Content-Length": "53","Content-Type": "application/x-www-form-urlencoded","Host": "drt.gov.in","Origin": "https://drt.gov.in","Referer": "https://drt.gov.in/front/page1_advocate.php","Sec-Fetch-Dest": "document","Sec-Fetch-Mode": "navigate","Sec-Fetch-Site": "same-origin","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0"}

# r = s.get("https://drt.gov.in/front/page1_advocate.php", headers = headers)

resp = s.get("https://drt.gov.in/front/captcha.php?_="+str(int(time.time())),headers = headers, stream=True)
file = open("sample_image.png", "wb")
file.write(resp.content)
file.close()
img = Image.open("sample_image.png")
captcha = image_to_string(img, config='--psm 6')

c = captcha.split('\n')[0]
print(c)

print("----",c)

data = {'schemaname': '103', 'name': party_name, 'answer': c.split('\n')[0], 'submit11': 'Search'}
print(data)

r = s.post("https://drt.gov.in/front/page1_advocate.php", headers = headers, data = data)

print(r.status_code, r.reason)
print("-----------------")
print(r.text)
print("--------------")
print(type(r.text))





bs = BeautifulSoup(r.text, 'html.parser')
# bs = BeautifulSoup(r.text, 'html.parser')
href = bs.find('tr').text
print("------------000000000")
print(href)
print("--------898989897879897")

table = bs.findAll('div',attrs={"class":"row"})
print("][][][][][][][]")
res=[]
# data=bs.findAll( "table", {"width":"550px"} )

# for table in data:
#     rows = table.findAll('tr')
#     print("---------lkokokol")
#     print(rows)
#     print("-=-=-=-=-=-=-=-")
#     df = pd.DataFrame([rows])
#     resultJSON = df.to_json(orient='records')
#     print(resultJSON)

import pdb
import re


for row in bs.select('table tr'):
    result = row.get_text(' - ', strip=True)
    df = pd.DataFrame([result])
    resultJSON = df.to_json(orient='records')
    print(resultJSON)


  
    
    

    print(row.contents)
    for td in row.select('td'):
        # pdb.set_trace()
        print (td.contents)
        left = "javascript:popsurety_detailreport('"
        right = '\');">'
        more_details = str(row)[str(row).index(left)+len(left):str(row).index(right)]
        # exit()
        print(more_details)
    
    # pdb.set_trace()
    # for i in row:
    #     tag = bs.findAll('a') #all "a" tag in a list
    #     print(tag)





    
    # for tr in rows:
    #     cell = [i.methods for i in tr.find_all('td')]
    #     df = pd.DataFrame([cell])
    #     resultJSON = df.to_json(orient='records')
    #     print(resultJSON)
        
#         for td in cols:
#             print("===",td.contents[0])
#             print(type(td.contents[0]))
#             res.append(td.contents[0])
# print("------------")

# soup = BeautifulSoup(r.text)
# table = soup.find('table')


# for row in table.findAll('tr')[1:250]:
#     col = row.findAll('td')
#     name = col[1].getText()
#     position = col[3].getText()
#     player = (name, position)
#     print ("|".join(player))

