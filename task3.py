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
      list_all_cd = bs.findAll('div', class_='jjm-col l12 m12 s12 jjm-light-gray jjm-center jjm-small jjm-text-black')
      cd = list_all_cd[0]
      print(cd)
      village = cd.find('span', class_='jjm-medium')
      print(village.text)
      

