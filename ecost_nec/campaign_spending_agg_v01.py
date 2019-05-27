import re
import time
import requests
from bs4 import BeautifulSoup

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome')

driver = webdriver.Chrome('/Users/daesikkim/downloads/chromedriver', chrome_options=options)
driver.implicitly_wait(3)

dic_spending = {'district': [], 'party': [], 'name': [], 'spending': [], 'spending_limit': []}

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

for p in range(100, 1000, 100):
    # 시군구에 따라 단위 조정; max 3200
    try:
        driver.get('http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020180613&topMenuId=CE&secondMenuId=CELA02')
        time.sleep(0.5)

        driver.find_element_by_id('electionId4').click()
        time.sleep(0.5)

        select1 = Select(driver.find_element_by_name('cityCode'))
        # 시도에 따라 번호 조정
        province = '2700'
        province_short ='270'
        select1.select_by_value(f'{province}')
        select2 = Select(driver.find_element_by_name('sggCityCode'))
        select2.select_by_value(f'4{province_short}{p}')
        driver.find_element_by_xpath('//*[@id="spanSubmit"]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        for line in range(0, 9):
            if soup.select(f'#table01 > tbody > tr:nth-of-type({line+1})') != []:
                dic_spending['district'].append(soup.select(f'#table01 > tbody > tr:nth-of-type({line+1}) > td.firstTd')[0].string)
                dic_spending['party'].append(soup.select(f'#table01 > tbody > tr:nth-of-type({line+1}) > td:nth-of-type(4)')[0].string)
                dic_spending['name'].append(remove_html_tags(str(soup.select(f'#table01 > tbody > tr:nth-of-type({line+1}) > td:nth-of-type(5)')[0])))
                dic_spending['spending_limit'].append(soup.select(f'#table01 > tbody > tr:nth-of-type({line+1}) > td:nth-of-type(6)')[0].string)
                dic_spending['spending'].append(soup.select(f'#table01 > tbody > tr:nth-of-type({line+1}) > td:nth-of-type(7)')[0].string)
            else:
                break

    except Exception as e:
        print("no more City")


df_spending = pd.DataFrame(dic_spending)
writer = pd.ExcelWriter(f'spending_agg_{province}.xlsx')
df_spending.to_excel(writer, f'{province}')
writer.save()
