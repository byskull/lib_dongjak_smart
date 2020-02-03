# -*- coding: euc-kr -*-

from bs4 import BeautifulSoup
import telepot
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

reload(sys)
sys.setdefaultencoding('euc-kr')

f1 = open("dongjak_20200203.txt","wt")

browser = webdriver.Firefox()
#browser.get('http://210.99.187.108:8088/EZ-950SL_Web/mainPage/SI_searchbookindex_Service.jsp')
browser.get('http://210.99.187.108:8088/EZ-950SL_Web/mainPage/SI_searchbookindex.jsp')

Select(browser.find_element_by_name('no')).select_by_value("2")

browser.find_element_by_xpath("//img[contains(@onclick,\"SearchALL()\")]").click()

time.sleep(1)

for i in range(1,34) :
    if i > 10 and i % 10 == 1 :
        browser.find_element_by_xpath("//img[contains(@onclick,\"PageMove('%i')\")]"%i).click()
    else :
        browser.find_element_by_xpath("//a[contains(@onclick,\"PageMove('%i')\")]"%i).click()
    
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source, "html.parser")	
    trs =  soup.find_all("tr",{"onmouseover" : "this.style.backgroundColor='#f5f5f5'"})

    for tr in trs :
        bookdata  = tr.findAll('td' )    
        for book in bookdata :        
            try :
                f1.write(book.text)
                f1.write(book.a.text)            
            except :
                pass
        f1.write("----\n")

f1.close()

f1 = open("dongjak_20200203.txt","rt")
f2 = open("dongjak_20200203.csv","wt")

a = ""
cnt = 0 
for s in f1 :
    if s[:4] == "----" :
        f2.write(a+"\n")
        a = ""
    else :
        s = s.replace("\r","").replace("\n","")
        if s[:4] ==  "대출" :
            a = s + "," + a
        elif len(s) >= 1 :
            a += s + ","

time.sleep(10)		
browser.quit()
