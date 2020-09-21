import setYear
import setTeam
import time
import pymysql

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
                if '/' in table[line][11]:
                    ip = int(table[line][11].split(" ")[0]) + float(int(table[line][11].split(" ")[1].split("/")[0]) / int(table[line][11].split(" ")[1].split("/")[1]))
                else:
                    ip = float(table[line][11])
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
                h = int(table[line][12])
                hr = int(table[line][13])
                bb = int(table[line][14])
                hbp = int(table[line][15])
                so = int(table[line][16])
                r = int(table[line][17])
                er = int(table[line][18])

                sql = """insert into pitcherdb
                      (name, teamName, year, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)
                      values('%s', '%s', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%f')
                      """ % (name, teamname, yearVal, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)

                cur.execute(sql)
                conn.commit()

    conn.close()