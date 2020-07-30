#!/usr/bin/env python3

import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  

# Headless operation
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'

# secrets that we get from environment variables
try:
    ssn = os.environ['SSN']
    dob = os.environ['DOB']
    email = os.environ['EMAIL']
    first_name = os.environ['FIRSTNAME']
    last_name = os.environ['LASTNAME']
except Exception as e:
    print("The environment variables with your information have not been set. Please set SSN, DOB, EMAIL, FIRSTNAME and LASTNAME.")
    quit()

driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver.get('https://lwdwebpt.dol.state.nj.us/ClaimStatus/claimStatus.htm');

# Wait for the user to login and for the coupa page to load
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'col-md-12')))

box = driver.find_element_by_id('idSSN')
box.send_keys(ssn)

box = driver.find_element_by_id('idConfirmSSN')
box.send_keys(ssn)

# This element was not being populated properly. Had to insert a click event to make it work.
box = driver.find_element_by_id('idDateOfBirth')
box.click()
box.send_keys(dob)

box = driver.find_element_by_id('idConfirmDateOfBirth')
box.send_keys(dob)

box = driver.find_element_by_id('idEmail')
box.send_keys(email)

box = driver.find_element_by_id('idConfirmEmail')
box.send_keys(email)

box = driver.find_element_by_id('idFirstName')
box.send_keys(first_name)

box = driver.find_element_by_id('idLastName')
box.send_keys(last_name)

# Wait for the enter box to appear, and then click it.
ea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'idEnter')))
ea.click()

# Grab the result of our claim
result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="f1"]/div[2]/div/div/div/div[3]/div[1]/font'))).text

print(result)

driver.quit()
