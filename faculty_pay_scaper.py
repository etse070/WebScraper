# Econ 503 Senior Thesis
# Web scraper for collecting average faculty salary by Private institution sourced from the Chronicle
# Written by Ethan Tse with help from Ahra Wu

import pandas as pd
import numpy as np
import requests
import re
import os
import time
import sys

import keyboard
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

#4-year Private colleges

url = "https://data.chronicle.com/category/sector/2/faculty-salaries/"

driver = webdriver.Chrome("\\Users\\ethan\\OneDrive\\Desktop\\HR and MGMT Articles and Data\\Thesis Code\\chromedriver.exe")
driver.get(url)

private_college_info = []

# Parses data from 13 pages of faculty salaries
for page in range(13):
    for row in range(25):
        private_college_info.append(driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[" + str(row + 1) + "]/td[1]/a").get_attribute("innerText"))
        for column in range(1,4):
            private_college_info.append(driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[" + str(row + 1) + "]/td[" + str(column + 1) + "]").get_attribute("innerText"))

    driver.find_elements_by_xpath("//*[@id='DataTables_Table_0_next']")[0].click()
    time.sleep(3)
    

# Reshapes data matrix
res = np.reshape(private_college_info, (int(len(private_college_info)/4), 4))

res_df = pd.DataFrame(res)

# Export the spreadsheet to a csv file
#res_df.to_csv('res1.csv', index=False)

# Check the current working directory: Go to the folder and locate the csv file.
#print(os.getcwd())
