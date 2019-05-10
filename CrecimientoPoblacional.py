import urllib
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from sys import stdin
import time

chrome_options = Options()
driver = None
try:
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"), chrome_options=chrome_options)
    driver.get("https://www.worldometers.info/world-population/")
except Exception as e:
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
    driver.get("https://www.worldometers.info/world-population/")
nacimientos = set()
for i in range(1000):
    try:
        valores = driver.find_elements_by_xpath('//*[@id="maincounter-wrap"]/div/span/*')
        numero = ""
        for j in valores:
            numero += j.get_attribute('innerHTML')
        numero = numero.replace(",", "")
        nacimientos.add(int(numero))
    except:
        continue
nacimientos = list(nacimientos)
nacimientos.sort()
print(nacimientos, len(nacimientos))
driver.quit()