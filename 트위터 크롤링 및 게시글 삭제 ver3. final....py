#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip3 install selenium')


# In[ ]:


from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# In[ ]:


from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:/Users/tyumi/Downloads/chromedriver.exe")
driver.get('https://twitter.com')
time.sleep(3)
from selenium.webdriver.common.by import By
input_id=driver.find_element(By.NAME,'text')
input_id.send_keys('WRITE YOUR ID')
driver.find_element(By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div').click()
time.sleep(3)
#input_some=driver.find_element(By.TAG_NAME,'input')
#input_some.send_keys(WRITE YOUR ID)
#driver.find_element(By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div').click()
#time.sleep(3)
input_pw=driver.find_element(By.NAME,'password')
input_pw.send_keys('WRITE YOUR PASSWORD')
driver.find_element(By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div > div').click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,'#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-15zivkp.r-1bymd8e.r-13qz1uu > nav > a:nth-child(7) > div > div > svg > g > path').click()


# In[ ]:


get_ipython().system('pip3 install pyautogui')


# In[ ]:


import pyautogui


# In[ ]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# In[ ]:


#Retweet 지우기
cucu=driver.current_url
while True:
    pyautogui.moveTo(1920/3,1080/2)
    button5location = pyautogui.locateOnScreen("myScreenshot.png",confidence=0.9) 
    button6location = pyautogui.locateOnScreen("myScreenshotkk.png",confidence=0.9)
    if button5location==None and button6location==None:
        pyautogui.scroll(-500)
        continue
    elif button5location==None:
        pyautogui.scroll(-200)
        continue
    else:
        point = pyautogui.center(button5location) # Box 객체의 중앙 좌표를 리턴합니다. 
        pyautogui.click(point[0],point[1],duration=0.5)
        k=0
        if cucu!=driver.current_url:
            driver.back()
            continue
        cc=driver.find_elements(By.CSS_SELECTOR,'#layers > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div:nth-child(2) > div > div.css-1dbjc4n.r-14lw9ot.r-1q9bdsx.r-1upvrn0.r-thhjwx.r-1udh08x.r-u8s1d > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > span')
        if len(cc)>0:
            if cc[0].text=='Undo Retweet':
                ActionChains(driver).move_to_element(cc[0]).click(cc[0]).perform()
            else:
                continue
        else:
            continue        


# In[ ]:


#내가 쓴 트윗 청소기
cucu=driver.current_url
while True:
    pyautogui.moveTo(1920/3,1080/2)
    button5location = pyautogui.locateOnScreen("myScreenshot.png",confidence=0.9) 
    button6location = pyautogui.locateOnScreen("myScreenshotkk.png",confidence=0.9)
    if button5location==None and button6location==None:
        pyautogui.scroll(-400)
        continue
    elif button6location==None:
        pyautogui.scroll(-100)
        continue
    point = pyautogui.center(button6location) # Box 객체의 중앙 좌표를 리턴합니다. 
    pyautogui.click(point[0],point[1],duration=0.5)
    if cucu!=driver.current_url:
        driver.back()
        continue
    cc=driver.find_elements(By.CSS_SELECTOR,'#layers > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div > div:nth-child(2) > div > div.css-1dbjc4n.r-14lw9ot.r-1q9bdsx.r-1upvrn0.r-thhjwx.r-1udh08x.r-u8s1d > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > span')
    if len(cc)>0:
        if 'Del' in cc[0].text:
            ActionChains(driver).move_to_element(cc[0]).click(cc[0]).perform()
            cc=driver.find_elements(By.CSS_SELECTOR,'#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-1kihuf0.r-18u37iz.r-1pi2tsx.r-1777fci.r-1pjcn9w.r-xr3zp9.r-1xcajam.r-ipm5af.r-9dcw1g > div.css-1dbjc4n.r-z6ln5t.r-14lw9ot.r-1867qdf.r-1jgb5lz.r-1rnoaur.r-494qqr.r-13qz1uu > div.css-1dbjc4n.r-eqz5dr.r-1hc659g.r-1n2ue9f.r-11c0sde.r-13qz1uu > div.css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-16y2uox.r-6gpygo.r-peo1c.r-1ps3wis.r-1ny4l3l.r-1udh08x.r-1guathk.r-1udbk01.r-o7ynqc.r-6416eg.r-lrvibr.r-3s2u2q > div > span > span')
            ActionChains(driver).move_to_element(cc[0]).click(cc[0]).perform()
            time.sleep(4)
            continue
        else:                                    
            button5location = pyautogui.locateOnScreen("screenb.png",confidence=0.9) 
            point = pyautogui.center(button5location) # Box 객체의 중앙 좌표를 리턴합니다. 
            pyautogui.click(point[0],point[1],duration=0.5)
            continue
    else:
        continue

