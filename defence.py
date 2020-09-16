import setYear
import setTeam
import time
import pymysql

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
        setYear.setYear(year, driver)

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

            setTeam.setTeam(team, driver)

            for line in range(1, 21):
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

            for line in range(0, 20):
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
                      """ % (name, teamname, yearVal, pos, g, gs, ip, e, pko, po, a, dp, fpct, pb, sb, cs, csper)

                cur.execute(sql)
                conn.commit()

    conn.close()