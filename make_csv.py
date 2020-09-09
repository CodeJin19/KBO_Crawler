from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import pymysql

"""
    00 : OB LT SS HH HD HT LG SK
    01 : OB LT SS HH HD HT LG SK
    02 : OB LT SS HH HD HT LG SK
    03 : OB LT SS HH HD HT LG SK
    04 : OB LT SS HH HD HT LG SK
    05 : OB LT SS HH HD HT LG SK
    06 : OB LT SS HH HD HT LG SK
    07 : OB LT SS HH HD HT LG SK

    08 : OB LT SS HH    HT LG SK WO
    09 : OB LT SS HH    HT LG SK WO
    10 : OB LT SS HH    HT LG SK WO
    11 : OB LT SS HH    HT LG SK WO
    12 : OB LT SS HH    HT LG SK WO

    13 : OB LT SS HH    HT LG SK WO NC
    14 : OB LT SS HH    HT LG SK WO NC

    15 : OB LT SS HH    HT LG SK WO NC KT
    16 : OB LT SS HH    HT LG SK WO NC KT
    17 : OB LT SS HH    HT LG SK WO NC KT
    18 : OB LT SS HH    HT LG SK WO NC KT
    19 : OB LT SS HH    HT LG SK WO NC KT
    20 : OB LT SS HH    HT LG SK WO NC KT
 """

def crawling(f) :
    writer = csv.writer(f)
    writer.writerow(['a', 'b', 'c'])

    # print("몇 년도부터 크롤링할 지 입력하세요 (최소 2010) YYYY: ")
    yearFrom = 2010
    # print("몇 년도까지 크롤링할 지 입력하세요 (최대 2019) YYYY: ")
    yearTo = 2010
    teamList = ['OB', 'LT', 'SS', 'HH', 'HD', 'HT', 'LG', 'SK', 'WO', 'NC', 'KT']

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')
    time.sleep(2)

    try:
        # 웹페이지 연결
        driver.get('https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx')
        time.sleep(2)

#------------------------------------------------------------------

        option = driver.find_element_by_xpath("//*[@id='contents']/div[2]/ul/li[2]/img")
        option.click()
        time.sleep(2)

        month = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value='" + str(4) + "']")
        month.click()

        year = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/div/div/select[2]/option[@value='" + str(yearFrom) + "']")
        year.click()

        time.sleep(2)

        day = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(3) + "]/td[" + str(6) + "]/a")
        day.click()
            #//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[7]
            #//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[7]/a
            #//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[4]
            #//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[4]/a
        x = input()

#------------------------------------------------------------------
    
    except BaseException as e:
        print("----------------------------------")
        print("error :")
        print(e)
        print("----------------------------------")
    finally:
        driver.quit()
        print("quit driver")

"""
    # driver 연결 및 대기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver', options=options)
"""
def generate() :
    f = open('KBO_data.csv', 'wt', encoding='utf-8', newline="")

    crawling(f)

    f.close()