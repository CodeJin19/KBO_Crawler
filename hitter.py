import setYear
import setTeam
import time
import pymysql

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