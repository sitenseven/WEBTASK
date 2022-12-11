import os
from selenium import webdriver
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

def start():
    # web.open('http://net-informations.com', new=2)
    browser = webdriver.Edge(r"msedgedriver.exe")
    # Simply just open a new Edge browser and go to lambdatest.com
    browser.maximize_window()
    browser.get('https://fulllengthaudiobook.com')
    try:
        # Get the text box to insert Email using selector ID
        # myElem_1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'menu-item-36832')))
        # myElem_2 = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'mejs-play')]/button")))
        myElem_2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-controls='mep_6']")))
        # myElem_2 = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mejs-button')))
        # [i.get_attribute('aria-controls') for i in myElem_2]
        # Entering the email address
        # myElem_1.send_keys("rishabhps@lambdatest.com")
        # myElem_1[0].click()
        # ActionChains(browser).move_to_element(myElem_2).click().perform()
        ActionChains(browser).move_to_element(myElem_2).click().perform()
        # l = driver.find_element_by_xpath("//input[@id='txtSearchText']")
        # l.send_keys("Tutorialspoint")
        browser.execute_script("arguments[0].click();", myElem_2)


        # # Get the Submit button to click and start free testing using selector CSS_SELECTOR
        # myElem_2 = WebDriverWait(browser, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#testing_form > div")))
        # # Starting free testing on LambdaTest
        # myElem_2.click()
        sleep(10)
        # ActionChains(browser).move_to_element(myElem_2).click().perform()
    except TimeoutException:
        print("No element found")
    sleep(10)
    # browser.close()