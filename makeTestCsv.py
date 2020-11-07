import csv
import time
import pymysql

def controler(f):
    print("몇 년도부터 크롤링할 지 입력하세요 (최소 2010) YYYY: ")
    yearFrom = int(input())
    print("몇 년도까지 크롤링할 지 입력하세요 (최대 2012) YYYY: ")
    yearTo = int(input())
    yearTo += 1

    passwd = input("비번을 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')

    wr = csv.writer(f)



"""
    # driver 연결 및 대기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver', options=options)
"""