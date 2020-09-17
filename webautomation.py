from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
file=pd.read_csv("D:/download/pp3.csv")
d=pd.DataFrame(file)
p=d[['number'][0]]
q=d[['number1'][0]]
r=d[['number2'][0]]
s=d[['number3'][0]]
k=[]
for i in range(len(p)):
    if isinstance(p[i], str):
        
        try:
            j=int(p[i][0:12])

            k.append(j)
        except:
            h=1
for i in range(len(q)):
    if isinstance(p[i], str):
        try:
            j=int(p[i][0:12])

            k.append(j)
        except:
            h=1
for i in range(len(r)):
    if isinstance(p[i], str):
        
        try:
            j=int(p[i][0:12])

            k.append(j)
        except:
            h=1
for i in range(len(s)):
    if isinstance(p[i], str):
        
        try:
            j=int(p[i][0:12])

            k.append(j)
        except:
            h=1
print(len(k))
f=[]
g=[]
for i in range(0,10):
    
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://epos.telangana.gov.in/ePoS/rcTransactionSummaryforCurrentMonth.html')
    searchbox=driver.find_element_by_xpath('//*[@id="rc_no"]')
    searchbox.send_keys(k[i])
    searchbutton=driver.find_element_by_xpath('//*[@id="btngetDetails"]')
    searchbutton.click()
    print('enter 1 or 0',i)
    if k[i]==369300126117:
        break
    t=input()
    if t=='1':
        f.append(k[i])
    else:
        g.append(k[i])
print(f)
print(g)
