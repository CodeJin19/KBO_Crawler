#selenium 패키지 설치 terminal -> pip install selenium
#pymysql 패키지 설치 terminal -> pip install pymysql
from selenium import webdriver
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

def hitter(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[1]/a")
    option.click()
    time.sleep(2)

    table = []

    passwd = input("비번을 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
    cur = conn.cursor()

    for i in range(0, 20):
        table.append([])

        for j in range(0, 17):
            table[i].append('a')

    for year in range(yearFrom, (yearTo + 1)):
        setYear(year, driver)
        time.sleep(2)

        for team in teamList:
            if year < 2008:
                if team == 'WO' or team == 'NC' or team == 'KT':
                    continue
            elif year < 2013:
                if team == 'HD' or team == 'NC' or team == 'KT':
                    continue
            elif year < 2015:
                if team == 'HD' or team == 'KT':
                    continue
            else:
                if team == 'HD':
                    continue

            setTeam(team, driver)
            time.sleep(2)

            for line in range(1, 21):
                table[line - 1][0] = year

                for idx in range(1, 17):
                    try:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text
                    except BaseException as e:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text

            for line in range(0, 20):
                if table[line][4] == '-':
                    avg = 0
                else:
                    avg = float(table[line][4])
                name = str(table[line][2])
                teamname = str(table[line][3])
                yearVal = int(table[line][0])
                g = int(table[line][5])
                pa = int(table[line][6])
                ab = int(table[line][7])
                r = int(table[line][8])
                h = int(table[line][9])
                b2 = int(table[line][10])
                b3 = int(table[line][11])
                hr = int(table[line][12])
                tb = int(table[line][13])
                rbi = int(table[line][14])
                sac = int(table[line][15])
                sf = int(table[line][16])

                sql = """insert into hitterdb
                      (name, teamName, year, avg, g, pa, ab, r, h, 2b, 3b, hr, tb, rbi, sac, sf)
                      values('%s', '%s', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')
                      """ % (name, teamname, yearVal, avg, g, pa, ab, r, h, b2, b3, hr, tb, rbi, sac, sf)

                cur.execute(sql)
                conn.commit()

    conn.close()


def pitcher(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[2]/a")
    option.click()
    time.sleep(2)

    table = []

    passwd = input("비번을 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
    cur = conn.cursor()

    for i in range(0, 20):
        table.append([])

        for j in range(0, 20):
            table[i].append('a')

    for year in range(yearFrom, (yearTo + 1)):
        setYear(year, driver)
        time.sleep(2)

        for team in teamList:
            if year < 2008:
                if team == 'WO' or team == 'NC' or team == 'KT':
                    continue
            elif year < 2013:
                if team == 'HD' or team == 'NC' or team == 'KT':
                    continue
            elif year < 2015:
                if team == 'HD' or team == 'KT':
                    continue
            else:
                if team == 'HD':
                    continue

            setTeam(team, driver)
            time.sleep(2)
            lineTo = 20

            if year == 2013 and team == 'WO':
                lineTo = 18
            elif year == 2014 and team == 'SS':
                lineTo = 19
            elif year == 2015 and team == 'SS':
                lineTo = 19
            elif year == 2017 and team == 'NC':
                lineTo = 19

            for line in range(1, (lineTo + 1)):
                table[line - 1][0] = year

                for idx in range(1, 20):
                    try:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text
                    except BaseException as e:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text

            for line in range(0, lineTo):
                if table[line][4] == '-':
                    era = 0
                else:
                    era = float(table[line][4])
                if table[line][10] == '-':
                    wpct = 0
                else:
                    wpct = float(table[line][10])
                if table[line][19] == '-':
                    whip = 0
                else:
                    whip = float(table[line][19])
                name = str(table[line][2])
                teamname = str(table[line][3])
                yearVal = int(table[line][0])
                g = int(table[line][5])
                w = int(table[line][6])
                l = int(table[line][7])
                sv = int(table[line][8])
                hld = int(table[line][9])
                ip = str(table[line][11])
                h = int(table[line][12])
                hr = int(table[line][13])
                bb = int(table[line][14])
                hbp = int(table[line][15])
                so = int(table[line][16])
                r = int(table[line][17])
                er = int(table[line][18])

                sql = """insert into pitcherdb
                      (name, teamName, year, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)
                      values('%s', '%s', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%f', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%f')
                      """ % (name, teamname, yearVal, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)

                cur.execute(sql)
                conn.commit()

    conn.close()


def defence(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[3]/a")
    option.click()
    time.sleep(2)

    table = []

    passwd = input("비번을 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
    cur = conn.cursor()

    for i in range(0, 20):
        table.append([])

        for j in range(0, 18):
            table[i].append('a')

    for year in range(yearFrom, (yearTo + 1)):
        setYear(year, driver)
        time.sleep(2)

        for team in teamList:
            if year < 2008:
                if team == 'WO' or team == 'NC' or team == 'KT':
                    continue
            elif year < 2013:
                if team == 'HD' or team == 'NC' or team == 'KT':
                    continue
            elif year < 2015:
                if team == 'HD' or team == 'KT':
                    continue
            else:
                if team == 'HD':
                    continue

            setTeam(team, driver)
            time.sleep(2)
            lineTo = 20

            for line in range(1, (lineTo + 1)):
                table[line - 1][0] = year

                for idx in range(1, 18):
                    try:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[2]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text
                    except BaseException as e:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[2]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text

            for line in range(0, lineTo):
                if table[line][17] == '-':
                    csper = 0
                else:
                    csper = float(table[line][17])
                name = str(table[line][2])
                teamname = str(table[line][3])
                yearVal = int(table[line][0])
                pos = str(table[line][4])
                g = int(table[line][5])
                gs = int(table[line][6])
                ip = str(table[line][7])
                e = int(table[line][8])
                pko = int(table[line][9])
                po = int(table[line][10])
                a = int(table[line][11])
                dp = int(table[line][12])
                fpct = float(table[line][13])
                pb = int(table[line][14])
                sb = int(table[line][15])
                cs = int(table[line][16])

                sql = """insert into defencedb
                      (name, teamName, year, pos, g, gs, ip, e, pko, po, a, dp, fpct, pb, sb, cs, csper)
                      values('%s', '%s', '%d', '%s', '%d', '%d', '%s', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d', '%d', '%f')
                      """ % (
                name, teamname, yearVal, pos, g, gs, ip, e, pko, po, a, dp, fpct, pb, sb, cs, csper)

                cur.execute(sql)
                conn.commit()

    conn.close()


def runner(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[4]/a")
    option.click()
    time.sleep(2)

    table = []

    for year in range(yearFrom, yearTo):
        setYear(year, driver)

        for team in teamList:
            setTeam(team, driver)

            for line in range(1, 31):
                table.append([])

                for idx in range(1, 10):
                    try:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]/table/tbody/tr[" + str(
                                line) + "]/td[" + str(idx) + "]")
                        table[line - 1].append(data.text)
                    except BaseException as e:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]/table/tbody/tr[" + str(
                                line) + "]/td[" + str(idx) + "]")
                        table[line - 1].append(data.text)

    # MySQL 연동

    connect = pymysql.connect(host='localhost', user='root', password='1q2w3e4r', db='crawling', charset='utf8')
    cursor = connect.cursor()

    for line in table:
        no = int(line[0])
        name = str(line[1])
        teamname = str(line[2])
        g = int(line[3])
        sba = int(line[4])
        sb = int(line[5])
        cs = int(line[6])
        oob = int(line[7])
        pko = int(line[8])

        sql = """insert into runnerdatabase
        (no, name, teamname, g, sba, sb, cs, oob, pko)
        values('%d', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d')
        """ % (no, name, teamname, g, sba, sb, cs, oob, pko)

        cursor.execute(sql)
        connect.commit()

    connect.close()


def setTeam(teamValue, driver):
    # 스크롤다운 옵션에서 팀 설정 및 대기

    team = driver.find_element_by_xpath(
        "//select[@id='cphContents_cphContents_cphContents_ddlTeam_ddlTeam']/option[@value='" + str(teamValue) + "']")
    team.click()
    time.sleep(2)


def setYear(yearValue, driver):
    # 스크롤다운 옵션에서 년도 설정 및 대기

    year = driver.find_element_by_xpath(
        "//select[@id='cphContents_cphContents_cphContents_ddlSeason_ddlSeason']/option[@value='" + str(
            yearValue) + "']")
    year.click()
    time.sleep(2)


def crawling():
    print("원하는 년도를 입력하세요 YYYY ~ YYYY : ")
    # yearFrom = int(input())
    # yearTo = int(input())
    yearFrom = 2010
    yearTo = 2019

    teamList = ['OB', 'LT', 'SS', 'HH', 'HD', 'HT', 'LG', 'SK', 'WO', 'NC', 'KT']

    # driver 연결 및 대기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver', chrome_options=options)
    #driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')
    time.sleep(2)

    try:
        # 웹페이지 연결
        driver.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
        time.sleep(2)

        # hitter(driver, yearFrom, yearTo, teamList)
        # pitcher(driver, yearFrom, yearTo, teamList)
        # defence(driver, yearFrom, yearTo, teamList)
        runner(driver, 2018, 2019, teamList)
    except BaseException as e:
        print("----------------------------------")
        print("error :")
        print(e)
        print("----------------------------------")
    finally:
        driver.quit()
        print("quit driver")


def setDB():
    # MySQL 연동

    passwd = input("비번을 입력하세요 : ")

    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
    cur = conn.cursor()

    # 두산, 키움, SK, LG, NC, KT, KIA, 삼성, 한화, 롯데
    # DSB, KH, SKY, LGT, NCD, KTW, KIA, SSL, HHE, LTG
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

    # todo : id 생각해보기

    cur.execute("DROP TABLE IF EXISTS hitterDB")
    cur.execute("CREATE TABLE hitterDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), avg DOUBLE(4, 3), g INT(3), pa INT(3), ab INT(3), r INT(3), h INT(3), 2b INT(3), 3b INT(3), hr INT(3), tb INT(3), rbi INT(3), sac INT(3), sf INT(3))")

    cur.execute("DROP TABLE IF EXISTS pitcherDB")
    cur.execute("CREATE TABLE pitcherDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), era DOUBLE(4, 2), g INT(3), w INT(3), l INT(3), sv INT(3), hld INT(3), wpct DOUBLE(4, 3), ip VARCHAR(20), h INT(3), hr INT(3), bb INT(3), hbp INT(3), so INT(3), r INT(3), er INT(3), whip DOUBLE(3, 2))")

    cur.execute("DROP TABLE IF EXISTS defenceDB")
    cur.execute("CREATE TABLE defenceDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), pos VARCHAR(20), g INT(3), gs INT(3), ip VARCHAR(20), e INT(3), pko INT(3), po INT(3), a INT(3), dp INT(3), fpct DOUBLE(4, 3), pb INT(3), sb INT(3), cs INT(3), csper DOUBLE(3, 1))")

    cur.execute("DROP TABLE IF EXISTS runnerDB")
    cur.execute("CREATE TABLE runnerDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), g INT(3), sba INT(3), sb INT(3), cs INT(3), sbper DOUBLE(3, 1), oob INT(3), pko INT(3))")

    conn.close()


if __name__ == "__main__":

    choice = 0

    while choice != 4:
        print("1. 필요 패키지 설명")
        print("2. DB 세팅")
        print("3. Crawling 실행")
        print("4. 종료")
        choice = int(input("원하는 설정을 입력하세요 : "))


        if choice == 1:
            print("이 프로그램을 실행하기 위해서는 다음과 같은 것들이 설치돼야 합니다.")
            print("\n------------------------")
            print("1. MySQL")
            print("2. Selenium")
            print("3. pymysql")
            print("------------------------\n")
        elif choice == 2:
            setDB()
        elif choice == 3:
            crawling()
        elif choice != 4:
            print("다시 입력해주세요")

"""
    # teamList = ['OB', 'LT', 'SS', 'WO', 'HH', 'HT', 'KT', 'LG', 'NC', 'SK']
    teamList = ['OB', 'LT']

    # driver 연결 및 대기

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')
    time.sleep(2)

    try:

        # 웹페이지 연결

        driver.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
        time.sleep(2)

        for year in range(2019, 2020):  # 2009년부터 2019년까지 크롤링
            setYear(year, driver)
            print(year)

            for team in teamList:
                setTeam(team, driver)
                print(team)

                crawling(driver)

        # hitter(driver, 2018, 2020, teamList)
        # pitcher(driver, 2018, 2020, teamList)
        # defence(driver, 2018, 2020, teamList)
        # runner(driver, 2018, 2020, teamList)

    except BaseException as e:
        print("----------------------------------")
        print(e)
        print("----------------------------------")
    finally:
        driver.quit()
        print("quit driver")
        """

