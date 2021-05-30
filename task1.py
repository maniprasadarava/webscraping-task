from bs4 import BeautifulSoup
import requests
import lxml

import pandas as pd

search_url = f'https://ejalshakti.gov.in/jjmreport/JJMVillage_Profile.aspx' # Replace this URL with yours

# HTTP GET requests
page = requests.get(search_url,verify=False)

# Checking if we successfully fetched the URL
if page.status_code == requests.codes.ok:
  print('Everything is cool!')
if page.status_code == requests.codes.ok:
      bs = BeautifulSoup(page.text, 'lxml')
      print(bs)
      list_all_cd = bs.findAll('div', class_='jjm-col l8 m8 s6 jjm-left-align jjm-padding-small')
      print(list_all_cd)
      print(len(list_all_cd))

# list_all_cd = bs.findAll('b', class_='jjm-col l8 m8 s6 jjm-left-align jjm-padding-small')
# print(list_all_cd)
# cd = list_all_cd[0]
# print(cd)
