# import packages
import time
import requests

from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options   
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# district list 
cities = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도']
dict_dist = dict([(key, []) for key in cities])

# setting up selenium
options = Options()
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome')
#options.add_argument('headless')

# open a browser
driver = webdriver.Chrome('/Users/daesikkim/Downloads/chromedriver', options=options)
driver.implicitly_wait(3)

# Load "info.nec.go.kr" - 선거비용 > 선거비용공개
driver.get('http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020180613&topMenuId=CE&secondMenuId=CELA02')
time.sleep(0.5)

# move 선거비용공개 > 구시군의장선거
driver.find_element_by_css_selector('#electionId4').click()

# select dropdown menus 
# looping through all options

select01 = Select(driver.find_element_by_name('cityCode'))
select01.select_by_visible_text("서울특별시")
select02 = Select(driver.find_element_by_name('sggCityCode'))
select02.select_by_visible_text('')