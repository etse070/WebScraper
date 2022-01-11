# Econ 503 Senior Thesis
# Web scraper for collecting average faculty salary by public institution sourced from the Chronicle
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

#4-year Public colleges

url = "https://data.chronicle.com/category/sector/1/faculty-salaries/"

driver = webdriver.Chrome("\\Users\\ethan\\OneDrive\\Desktop\\HR and MGMT Articles and Data\\Thesis Code\\chromedriver.exe")
driver.get(url)

public_college_info = []

for page in range(27):
    for row in range(25):
        public_college_info.append(driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[" + str(row + 1) + "]/td[1]/a").get_attribute("innerText"))
        for column in range(1,4):
            public_college_info.append(driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[" + str(row + 1) + "]/td[" + str(column + 1) + "]").get_attribute("innerText"))

    driver.find_elements_by_xpath("//*[@id='DataTables_Table_0_next']")[0].click()
    time.sleep(3)

print(public_college_info)

res = np.reshape(public_college_info, (int(len(public_college_info)/4), 4))

res_df = pd.DataFrame(res)

# Export the spreadsheet to a csv file
res_df.to_csv('public_avg_faculty_salary.csv', index=False)

# Check the current working directory: Go to the folder and locate the csv file.
print(os.getcwd())
