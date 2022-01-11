# Econ 503 Senior Thesis
# Web scraper for collecting college presidential pay by institution sourced from the Chronicle
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

#Private Colleges

url = "https://www.chronicle.com/article/executive-compensation-at-public-and-private-colleges/#id=table_private_2018"

driver = webdriver.Chrome("\\Users\\ethan\\OneDrive\\Desktop\\HR and MGMT Articles and Data\\Thesis Code\\chromedriver.exe")
driver.get(url)

private_college_info = []

# Private Colleges
# Extracts college name and compensation from 5 pages of data
for page in range(5):

    univ_name= []
    salary_info = []

    univ_name = driver.find_elements_by_css_selector(".college")
    salary_info = driver.find_elements_by_css_selector(".ech_detail")

    for index in range(len(univ_name)):
        private_college_info.append(univ_name[index].get_attribute("innerText"))
        for inner_index in range(4):
            private_college_info.append(salary_info[(index * 4) + inner_index].get_attribute("innerText"))


    driver.find_elements_by_xpath("//*[@id='ec_table']/div[5]/div[2]/a[2]")[0].click()
    time.sleep(3)


# Public Colleges

url = "https://www.chronicle.com/article/executive-compensation-at-public-and-private-colleges/#id=table_public_2018"

driver = webdriver.Chrome("\\Users\\ethan\\OneDrive\\Desktop\\HR and MGMT Articles and Data\\Thesis Code\\chromedriver.exe")
driver.get(url)

public_college_info = []

for page in range(5):

    univ_name= []
    salary_info = []

    univ_name = driver.find_elements_by_css_selector(".college")
    salary_info = driver.find_elements_by_css_selector(".ech_detail")

    for index in range(len(univ_name)):
        public_college_info.append(univ_name[index].get_attribute("innerText"))
        for inner_index in range(4):
            public_college_info.append(salary_info[(index * 4) + inner_index].get_attribute("innerText"))


    driver.find_elements_by_xpath("//*[@id='ec_table']/div[5]/div[2]/a[2]")[0].click()
    time.sleep(3)

# Reshapes data matricies 
res = np.reshape(private_college_info, (int(len(private_college_info)/5), 5))
res_1 = np.reshape(public_college_info, (int(len(public_college_info)/5), 5))

# Transform the list into a spreadsheet
res_df = pd.DataFrame(res)
res_df1 = pd.DataFrame(res_1)

# Export the spreadsheet to a csv file
res_df.to_csv('private_pres_comp.csv', index=False)
res_df1.to_csv('public_pres_comp.csv', index=False)

# Check the current working directory: Go to the folder and locate the csv file.
#print(os.getcwd())
