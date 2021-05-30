from bs4 import BeautifulSoup
import requests
import csv

search_url = f'https://ejalshakti.gov.in/jjmreport/JJMVillage_Profile.aspx'
page =requests.get(search_url,verify=False)

soup =BeautifulSoup(page.content,'html.parser')

# print(soup.text)

village = soup.findAll('div',class_="jjm-col l8 m8 s6 jjm-left-align jjm-padding-small")
print(village)


