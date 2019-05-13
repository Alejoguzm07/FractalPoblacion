import turtle
import urllib
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from turtle import *

def factor(driver):
    try:
        valoresn = list(
            driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div[2]/span/*'))
        valoresm = list(
            driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[3]/div[2]/span/*'))
        factorn = valoresn[1].get_attribute('innerHTML')
        factorm = valoresm[1].get_attribute('innerHTML')
        return factorn, factorm
    except:
        return factor(driver)
def main():
    chrome_options = Options()
    driver = None
    try:
        driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"), chrome_options=chrome_options)
        driver.get("https://www.worldometers.info/world-population/")
    except Exception as e:
        driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
        driver.get("https://www.worldometers.info/world-population/")
    nacimientos = set()
    muertes = set()
    t = turtle.Turtle()
    t.color("green")
    t2 = turtle.Turtle()
    t2.color("red")
    t.home()
    t2.home()
    factorn, factorm = factor(driver)

    fn = int(factorn) / 100
    fm = int(factorm) / 100
    for i in range(500):
        try:
            time.sleep(2)
            valoresn = list(driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div[2]/span/*'))
            valoresm = list(driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[3]/div[2]/span/*'))
            numeron = valoresn[-1].get_attribute('innerHTML')
            numerom = valoresm[-1].get_attribute('innerHTML')
            print(numeron, factorn)
            print(numerom, factorm)
            nn = int(numeron)
            nm = int(numerom)
            nacimientos.add(nn)
            muertes.add(nm)
            print(nn * fn, nm * fm)
            t.forward(nn * fn)
            t2.forward(nm * fm)
            t.left(30 + (nn/100))
            t2.left(30 + (nn/100))
        except:
            continue
    nacimientos = list(nacimientos)
    print(nacimientos, len(nacimientos))
    muertes = list(muertes)
    print(muertes, len(muertes))
    driver.quit()
main()

