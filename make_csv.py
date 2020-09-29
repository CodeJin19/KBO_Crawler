from selenium import webdriver
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

def setYear(yearValue, driver):
    option = driver.find_element_by_xpath("//*[@id='contents']/div[2]/ul/li[2]/img")
    option.click()
    time.sleep(2)

    year = driver.find_element_by_xpath(
        "//*[@id='ui-datepicker-div']/div/div/select[2]/option[@value='" + str(yearValue) + "']")
    year.click()

    if yearValue == 2010: #2010.03.27
        month = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value='" + str(2) + "']")
        month.click()

        time.sleep(2)

        day = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(4) + "]/td[" + str(7) + "]/a")
        day.click()
    elif yearValue == 2011:
        print("Hi")

def crawling(f) :
    # print("몇 년도부터 크롤링할 지 입력하세요 (최소 2010) YYYY: ")
    yearFrom = 2010
    # print("몇 년도까지 크롤링할 지 입력하세요 (최대 2019) YYYY: ")
    yearTo = 2010
    teamList = ['OB', 'LT', 'SS', 'HH', 'HD', 'HT', 'LG', 'SK', 'WO', 'NC', 'KT']

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')
    time.sleep(2)

    wr = csv.writer(f)

    try:
        # 웹페이지 연결
        driver.get('https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx')
        time.sleep(2)

        for year in range(yearFrom, (yearTo + 1)):
            setYear(year, driver)

            game_list = driver.find_element_by_xpath("//*[@id='contents']/div[3]/div/div[1]/ul")
            games = game_list.find_elements_by_tag_name("li")

            table = []
            tmp = []
            actual = []

            passwd = input("비번을 입력하세요 : ")
            conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
            cur = conn.cursor()

            for game in games:
                game.click()
                time.sleep(2)

                awayScore = driver.find_element_by_xpath("//*[@id='tblScordboard3']/tbody/tr[1]/td[1]")
                actual.append(awayScore.text)

                # lblHomePitcher --------------------------------------------------------------------
                actual.clear()
                table.clear()
                cnt = 0

                pitcherTable = driver.find_element_by_xpath("//*[@id='tblHomePitcher']")
                lines = pitcherTable.find_elements_by_tag_name("tr");

                for line in lines:
                    name = line.text.split(' ')[0]

                    if name != "선수명" and name != "TOTAL":
                        sql = "SELECT * FROM pitcherdb WHERE name=%s and year=%s"
                        cur.execute(sql, (name, year))
                        rows = cur.fetchall()

                        for row in rows:
                            tmp.clear()
                            cnt += 1

                            for i in range(4, 20):
                                tmp.append(row[i])

                            table.append(tmp.copy())

                tmp.clear()

                for j in range(len(table[0])):
                    sum = 0

                    for i in range(len(table)):
                        sum += float(table[i][j])

                    avg = sum / cnt
                    tmp.append(avg)
                    actual.append(avg)

                # wr.writerow(actual)

                # lblAwayHitter --------------------------------------------------------------------
                table.clear()
                cnt = 0

                hitterTable = driver.find_element_by_xpath("//*[@id='tblAwayHitter1']/tbody")
                lines = hitterTable.find_elements_by_tag_name("tr");

                idx = 0

                for line in lines:
                    name = line.text.split(' ')[2]
                    idx += 1

                    records = driver.find_element_by_xpath("//*[@id='tblAwayHitter2']/table/tbody/tr[" + str(idx) + "]").text
                    records = records.split(' ')

                    for record in records:
                        if record != "":
                            sql = "SELECT * FROM hitterdb WHERE name=%s and year=%s"
                            cur.execute(sql, (name, year))
                            rows = cur.fetchall()

                            for row in rows:
                                tmp.clear()
                                cnt += 1

                                for i in range(4, 17):
                                    tmp.append(row[i])

                                table.append(tmp.copy())
                            break

                tmp.clear()

                for j in range(len(table[0])):
                    sum = 0

                    for i in range(len(table)):
                        sum += float(table[i][j])

                    avg = sum / cnt
                    tmp.append(avg)
                    actual.append(avg)

                wr.writerow(actual)

                homeScore = driver.find_element_by_xpath("//*[@id='tblScordboard3']/tbody/tr[2]/td[1]")

                # id = lblAwayPitcher
                #//*[@id="tblAwayPitcher"]/tbody/tr[1]/td[1]
                #//*[@id="tblAwayPitcher"]/tbody/tr[2]/td[1]

                #lblHomeHitter

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
    f = open('KBO_data.csv', 'w', encoding='utf-8', newline="")

    wr = csv.writer(f)
    wr.writerow(['score', 'era', 'g', 'w', 'l', 'sv', 'hld', 'wpct', 'ip','h', 'hr', 'bb', 'hbp', 'so', 'r', 'er', 'whip', 'avg', 'g', 'pa', 'ab', 'r', 'h', '2b', '3b', 'hr', 'tb', 'rbi', 'sac', 'sf'])

    crawling(f)

    f.close()