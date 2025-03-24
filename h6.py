!pip install requests
!pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = 'https://www.milligazete.com.tr/arsiv/2025-03-22'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
list = soup.find_all(name="div", attrs={"class": "f-cat f-item"})
for i in list:
    print('=====================================')
    # print(i)
    for b in i.findAll("ull", {"class": "list underline"}): 
        #print(b)
        for link in b.findAll('a'):  
            my_link = link.get('href')+"\n"
            print(my_link)
            newLink = "www.milligazete.com.tr{}".format(my_link)
            print(newLink)  
            with open('eren.txt', "a", encoding="utf-8") as file:  
                file.write(newLink)

def abc(sayfa_url):
    link_listesi = [ 
        "https://www.milligazete.com.tr/arsiv/2023-05-03",
        "https://www.milligazete.com.tr/arsiv/2022-04-02",
        "https://www.milligazete.com.tr/arsiv/2021-04-02",
        "https://www.milligazete.com.tr/arsiv/2020-04-02",
        "https://www.milligazete.com.tr/arsiv/2019-04-02"


    ]
for gun in link_listesi:
    link_olusturucu(gun) 
        
        
