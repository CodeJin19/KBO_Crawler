from selenium import webdriver
import csv
import time
import pymysql

def generate() :
    print("몇 년도부터 크롤링할 지 입력하세요 (최소 2010) YYYY: ")
    yearFrom = int(input())
    print("몇 년도까지 크롤링할 지 입력하세요 (최대 2019) YYYY: ")
    yearTo = int(input())

    f = open('KBO_data.csv', 'wt', encoding='utf-8', newline="")
    writer = csv.writer(f)
    writer.writerow(['air','bow','chicken'])

    f.close()
