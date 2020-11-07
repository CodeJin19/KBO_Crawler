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

    teamList = ['OB', 'LT', 'SS', 'HH', 'HD', 'HT', 'LG', 'SK', 'WO', 'NC', 'KT']
    teamName = ['두산', '롯데', '삼성', '한화', '현대', 'KIA', 'LG', 'SK', '넥센', 'NC', 'KT']

    cur = conn.cursor()

    for year in range(yearFrom, (yearTo + 1)):
        if year < 2008:
            for i in range(len(teamList)):
                for j in range(len(teamList)):
                    if i <= j:
                        continue
                    elif teamList[i] == 'WO' or teamList[i] == 'NC' or teamList[i] == 'KT' or teamList[j] == 'WO' or teamList[j] == 'NC' or teamList[j] == 'KT':
                        continue
                    else:
                        sql = "SELECT * FROM pitcherdb WHERE teamname=%s and year=%s"
                        cur.execute(sql, (teamName[i], year))
                        rows = cur.fetchall()

        elif year < 2013:
            for i in range(len(teamList)):
                for j in range(len(teamList)):
                    if i == j or teamList[i] == 'HD' or teamList[i] == 'NC' or teamList[i] == 'KT' or teamList[j] == 'HD' or teamList[j] == 'NC' or teamList[j] == 'KT':
                        continue
                    else:
                        conn
        elif year < 2015:
            for i in range(len(teamList)):
                for j in range(len(teamList)):
                    if i == j or teamList[i] == 'HD' or teamList[i] == 'KT' or teamList[j] == 'HD' or teamList[j] == 'KT':
                        continue
                    else:
                        conn
        else:
            for i in range(len(teamList)):
                for j in range(len(teamList)):
                    if i == j or teamList[i] == 'HD' or teamList[j] == 'HD':
                        continue
                    else:
                        conn


"""
    # driver 연결 및 대기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver', options=options)
"""