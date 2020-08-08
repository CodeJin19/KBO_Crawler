#selenium 패키지 설치 terminal -> pip install selenium
#pymysql 패키지 설치 terminal -> pip install pymysql
from selenium import webdriver
import time
import pymysql

def crawling(driver):
    # driver에서 표 크롤링 및 터미널에 출력

    table = []

    # table = driver.find_element_by_class_name('tData01.tt')
    # tableData = table.text
    # print(type(table)) <class 'selenium.webdriver.remote.webelement.WebElement'>
    # print(type(tableData)) <class 'str'>
    # print(tableData)

    for line in range(1, 31):
        table.append([])

        for idx in range(1, 17):
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

    # print(table)

    # MySQL 연동

    connect = pymysql.connect(host='localhost', user='root', password='1q2w3e4r', db='sample', charset='utf8')
    cursor = connect.cursor()

    for line in table:
        no = int(line[0])
        name = str(line[1])
        teamname = str(line[2])
        avg = float(line[3])
        g = int(line[4])
        pa = int(line[5])
        ab = int(line[6])
        r = int(line[7])
        h = int(line[8])
        b2 = int(line[9])
        b3 = int(line[10])
        hr = int(line[11])
        tb = int(line[12])
        rbi = int(line[13])
        sac = int(line[14])
        sf = int(line[15])

        sql = """insert into sample
        (no, name, teamname, avg, g, pa, ab, r, h, 2b, 3b, hr, tb, rbi, sac, sf)
        values('%d', '%s', '%s', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')
        """ % (no, name, teamname, avg, g, pa, ab, r, h, b2, b3, hr, tb, rbi, sac, sf)

        cursor.execute(sql)
        connect.commit()

    connect.close()


def setYear(yearValue, driver):
    # 스크롤다운 옵션에서 년도 설정 및 대기

    year = driver.find_element_by_xpath(
        "//select[@id='cphContents_cphContents_cphContents_ddlSeason_ddlSeason']/option[@value='" + str(
            yearValue) + "']")
    year.click()
    time.sleep(2)


def setTeam(teamValue, driver):
    # 스크롤다운 옵션에서 팀 설정 및 대기

    team = driver.find_element_by_xpath(
        "//select[@id='cphContents_cphContents_cphContents_ddlTeam_ddlTeam']/option[@value='" + str(teamValue) + "']")
    team.click()
    time.sleep(2)


def setDB():
    # MySQL 연동

    passwd = input("비번을 입력하세요 : ")

    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
    cur = conn.cursor()

    # 두산, 키움, SK, LG, NC, KT, KIA, 삼성, 한화, 롯데
    # DSB, KH, SKY, LGT, NCD, KTW, KIA, SSL, HHE, LTG
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

    # todo : id 생각해보기

    cur.execute("DROP TABLE IF EXISTS playerDB")
    cur.execute("CREATE TABLE playerDB(idx INT(3) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(20), id INT(5))")

    cur.execute("DROP TABLE IF EXISTS hitterDB")
    cur.execute("CREATE TABLE hitterDB(idx INT(3) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), avg DOUBLE(4, 3), g INT(3), pa INT(3), ab INT(3), r INT(3), h INT(3), 2b INT(3), 3b INT(3), hr INT(3), tb INT(3), rbi INT(3), sac INT(3), sf INT(3))")

    cur.execute("DROP TABLE IF EXISTS pitcherDB")
    cur.execute("CREATE TABLE pitcherDB(idx INT(3) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), era DOUBLE(3, 2), g INT(3), w INT(3), l INT(3), sv INT(3), hld INT(3), wpct DOUBLE(4, 3), ip VARCHAR(20), h INT(3), hr INT(3), bb INT(3), hbp INT(3), so INT(3), r INT(3), er INT(3), whip DOUBLE(3, 2))")

    cur.execute("DROP TABLE IF EXISTS defenceDB")
    cur.execute("CREATE TABLE defenceDB(idx INT(3) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), pos VARCHAR(20), g INT(3), gs INT(3), ip VARCHAR(20), e INT(3), pko INT(3), po INT(3), a INT(3), dp INT(3), fpct DOUBLE(4, 3), pb INT(3), sb INT(3), cs INT(3), csper DOUBLE(3, 1))")

    cur.execute("DROP TABLE IF EXISTS runnerDB")
    cur.execute("CREATE TABLE runnerDB(idx INT(3) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), g INT(3), sba INT(3), sb INT(3), cs INT(3), sbper DOUBLE(3, 1), oob INT(3), pko INT(3))")

    conn.close()

def better(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[1]/a")
    option.click()
    time.sleep(2)

    table = []

    for year in range(yearFrom, yearTo):
        setYear(year, driver)

        for team in teamList:
            setTeam(team, driver)

            for line in range(1, 31):
                table.append([])

                for idx in range(1, 17):
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
    print("1")
    cursor = connect.cursor()
    print("2")
    print("len : " + str(len(table)))

    for line in range(len(table)):
        print(line)
        if (table[line][3] == '-'):
            continue
        else:
            no = int(table[line][0])
            name = str(table[line][1])
            teamname = str(table[line][2])
            avg = float(table[line][3])
            g = int(table[line][4])
            pa = int(table[line][5])
            ab = int(table[line][6])
            r = int(table[line][7])
            h = int(table[line][8])
            b2 = int(table[line][9])
            b3 = int(table[line][10])
            hr = int(table[line][11])
            tb = int(table[line][12])
            rbi = int(table[line][13])
            sac = int(table[line][14])
            sf = int(table[line][15])

            print("3")
            sql = """insert into betterdatabase
            (no, name, teamname, avg, g, pa, ab, r, h, 2b, 3b, hr, tb, rbi, sac, sf)
            values('%d', '%s', '%s', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')
            """ % (no, name, teamname, avg, g, pa, ab, r, h, b2, b3, hr, tb, rbi, sac, sf)

            print("4")
            cursor.execute(sql)
            print("5")
            connect.commit()
            print("6")

    connect.close()


def pitcher(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[2]/a")
    option.click()
    time.sleep(2)

    table = []

    for year in range(yearFrom, yearTo):
        setYear(year, driver)

        for team in teamList:
            setTeam(team, driver)

            for line in range(1, 31):
                table.append([])

                for idx in range(1, 20):
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
        if (str(line[9]) == '-'):
            continue
        else:
            no = int(line[0])
            name = str(line[1])
            teamname = str(line[2])
            era = float(line[3])
            g = int(line[4])
            w = int(line[5])
            l = int(line[6])
            sv = int(line[7])
            hld = int(line[8])
            wpct = float(line[9])
            ip = str(line[10])
            h = int(line[11])
            hr = int(line[12])
            bb = int(line[13])
            hbp = int(line[14])
            so = int(line[15])
            r = int(line[16])
            er = int(line[17])
            whip = float(line[18])

            sql = """insert into pitcherdatabase
            (no, name, teamname, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)
            values('%d', '%s', '%s', '%f', '%d', '%d', '%d', '%d', '%d', '%f', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%f')
            """ % (no, name, teamname, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)

            cursor.execute(sql)
            connect.commit()

    connect.close()


def defence(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[3]/a")
    option.click()
    time.sleep(2)

    table = []

    for year in range(yearFrom, yearTo):
        setYear(year, driver)

        for team in teamList:
            setTeam(team, driver)

            for line in range(1, 31):
                table.append([])

                for idx in range(1, 17):
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
        pos = str(line[3])
        g = int(line[4])
        gs = int(line[5])
        ip = str(line[6])
        e = int(line[7])
        pko = int(line[8])
        po = int(line[9])
        a = int(line[10])
        dp = int(line[11])
        fpct = float(line[12])
        pb = int(line[13])
        sb = int(line[14])
        cs = int(line[15])

        sql = """insert into defencedatabase
        (no, name, teamname, pos, g, gs, ip, e, pko, po, a, dp, fpct, pb, sb, cs)
        values('%d', '%s', '%s', '%s', '%d', '%d', '%s', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d', '%d')
        """ % (no, name, teamname, pos, g, gs, ip, e, pko, po, a, dp, fpct, pb, sb, cs)

        cursor.execute(sql)
        connect.commit()

    connect.close()


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


def runnerOrigin(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[4]/a")
    option.click()
    time.sleep(2)

    for year in range(yearFrom, yearTo):
        setYear(year, driver)

        for team in teamList:
            setTeam(team, driver)

            table = driver.find_element_by_class_name('tData01.tt')
            print(str(year) + " - " + str(team))
            print(table.text)


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
            # todo : Crawling
            print("아직 준비 중")
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
        # better(driver, 2018, 2020, teamList)
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