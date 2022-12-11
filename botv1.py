import random
import webbrowser as web
import subprocess as sub


# importing required package of webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.opera.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
# edge_path = "msedgedriver.exe"
# driver = webdriver.Edge(edge_path)
import time
from selenium.webdriver.common.keys import Keys








def main():
    browser = webdriver.Edge(r"msedgedriver.exe")
    file1 = open('names.txt', 'r' , encoding="utf-8")
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print(line.strip())

        # Simply just open a new Edge browser and go to lambdatest.com
        browser.maximize_window()
        browser.get('http://www.google.com')
        browser.implicitly_wait(10)
        try:
            search_bar = browser.find_elements_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
            browser.implicitly_wait(10)
            for char in line.strip():
                start = 0.1  # please edit the speed here
                stop = 0.6  # change this (the maximum value is 1 or 0.9)
                step = 0.3
                precision = 0.1
                f = 1 / precision
                n = random.randrange(start * f, stop * f, step * f) / f
                time.sleep(n)
                search_bar[0].send_keys(char)

            browser.implicitly_wait(10)



        #     search_bar[0].send_keys(line.strip())
        #     browser.implicitly_wait(10)
            search_bar[0].send_keys(Keys.ENTER)
            browser.implicitly_wait(10)
        #
        #     # links = browser.getPageSource().contains("text to search")
        #
            linkv =  "//cite[contains(text(),'https://fulllengthaudiobook.com')]"
            # xpath = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/div/a/h3'
            result1 = browser.find_elements_by_xpath(linkv)

            ifyes = len(result1)

            if(ifyes > 0):


                browser.implicitly_wait(10)
                result1[0].click()
                browser.implicitly_wait(10)
                sleep(20)

            # browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(
            #     EC.element_to_be_clickable((By.XPATH, '//*[@id="mep_1"]/div/div[3]/div[1]/button'))))

                audio =  browser.find_element_by_css_selector("button[aria-controls='mep_1")
            # browser.implicitly_wait(10)
            # audio[0].click()
                ActionChains(browser).move_to_element(audio).click().perform()
                browser.execute_script("arguments[0].click();", audio)
                sleep(5)
                browser.implicitly_wait(10)
                ActionChains(browser).move_to_element(audio).click().perform()

            for i in range(60):
                sleep(1)
            browser.quit()


















        except TimeoutException:
            print("No element found")
        sleep(10)
    # browser.close()
    # browser.maximize_window()
    # browser.get('fulllengthaudiobook')
    # browser.implicitly_wait(10)
    # linkv = "//span[contains(text(),'https://fulllengthaudiobook.com')]"
    # # xpath = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/div/a/h3'
    # result1 = browser.find_elements_by_xpath(linkv)
    # browser.implicitly_wait(10)
    # result1[0].click()

if __name__ == "__main__":
    main()