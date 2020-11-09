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

    table = []
    tmp = []
    actual = []
    cnt = 0

    cur = conn.cursor()

    for year in range(yearFrom, yearTo):
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
                    if i <= j:
                        continue
                    if teamList[i] == 'HD' or teamList[i] == 'NC' or teamList[i] == 'KT' or teamList[j] == 'HD' or teamList[j] == 'NC' or teamList[j] == 'KT':
                        continue
                    else:
                        sql = "SELECT * FROM pitcherdb WHERE teamname=%s and year=%s"
                        cur.execute(sql, (teamName[i], year))
                        rows = cur.fetchall()

                        for row in rows:
                            tmp.clear()
                            cnt += 1

                            for k in range(4, 20):
                                tmp.append(row[k])

                            table.append(tmp.copy())

                        tmp.clear()

                        for k in range(len(table[0])):
                            sum = 0

                            for l in range(len(table)):
                                sum += float(table[l][k])

                            avg = sum / cnt
                            tmp.append(avg)
                            actual.append(avg)

                        table.clear()
                        cnt = 0

                        sql = "SELECT * FROM hitterdb WHERE teamname=%s and year=%s"
                        cur.execute(sql, (teamName[j], year))
                        rows = cur.fetchall()

                        for row in rows:
                            tmp.clear()
                            cnt += 1

                            for k in range(4, 17):
                                tmp.append(row[k])

                            table.append(tmp.copy())

                        tmp.clear()

                        for k in range(len(table[0])):
                            sum = 0

                            for l in range(len(table)):
                                sum += float(table[l][k])

                            avg = sum / cnt
                            tmp.append(avg)
                            actual.append(avg)

                        wr.writerow(actual)
                        actual.clear()

        elif year < 2015:
            for i in range(len(teamList)):
                for j in range(len(teamList)):
                    if i == j or teamList[i] == 'HD' or teamList[i] == 'KT' or teamList[j] == 'HD' or teamList[j] == 'KT':
                        continue
                    else:
                        sql = "SELECT * FROM pitcherdb WHERE teamname=%s and year=%s"
                        cur.execute(sql, (teamName[i], year))
                        rows = cur.fetchall()

        else:
            for i in range(len(teamList)):
                for j in range(len(teamList)):
                    if i == j or teamList[i] == 'HD' or teamList[j] == 'HD':
                        continue
                    else:
                        sql = "SELECT * FROM pitcherdb WHERE teamname=%s and year=%s"
                        cur.execute(sql, (teamName[i], year))
                        rows = cur.fetchall()


"""
    # driver 연결 및 대기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver', options=options)
"""