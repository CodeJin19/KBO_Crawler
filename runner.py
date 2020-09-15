import setYear
import setTeam
import time
import pymysql

def runner(driver, yearFrom, yearTo, teamList):
    option = driver.find_element_by_xpath(
        "//*[@id='contents']/div[2]/div[2]/ul/li[4]/a")
    option.click()
    time.sleep(2)

    table = []

    passwd = input("비번을 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
    cur = conn.cursor()

    for i in range(0, 20):
        table.append([])

        for j in range(0, 11):
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

            for line in range(1, 21):
                table[line - 1][0] = year

                for idx in range(1, 11):
                    try:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[2]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text
                    except BaseException as e:
                        data = driver.find_element_by_xpath(
                            "//*[@id='cphContents_cphContents_cphContents_udpContent']/div[2]/table/tbody/tr[" + str(line) + "]/td[" + str(idx) + "]")
                        table[line - 1][idx] = data.text

            for line in range(0, 20):
                if table[line][8] == '-':
                    sbper = 0
                else:
                    sbper = float(table[line][8])
                name = str(table[line][2])
                teamname = str(table[line][3])
                yearVal = int(table[line][0])
                g = int(table[line][4])
                sba = int(table[line][5])
                sb = int(table[line][6])
                cs = int(table[line][7])
                oob = int(table[line][9])
                pko = int(table[line][10])

                sql = """insert into runnerdb
                      (name, teamName, year, g, sba, sb, cs, sbper, oob, pko)
                      values('%s', '%s', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d')
                      """ % (name, teamname, yearVal, g, sba, sb, cs, sbper, oob, pko)

                cur.execute(sql)
                conn.commit()

    conn.close()