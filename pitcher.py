from setYear import setYear
from setTeam import setTeam
from setSeason import setSeason
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
            setSeason(driver)

            flag = True

            while(flag):
                pitcherTable = driver.find_element_by_xpath("//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]/table")
                lines = pitcherTable.find_elements_by_tag_name("tr")

                for i in range(len(lines)):
                    if i != 0:
                        tmp = lines[i].text.split(' ')

                        if len(tmp) == 19:
                            if tmp[3] == '-':
                                era = 0
                            else:
                                era = float(tmp[3])
                            if tmp[9] == '-':
                                wpct = 0
                            else:
                                wpct = float(tmp[9])
                            if '/' in tmp[10]:
                                ip = float(int(tmp[10].split("/")[0]) / int(
                                        tmp[10].split("/")[1]))
                            else:
                                ip = float(tmp[10])
                            if tmp[18] == '-':
                                whip = 0
                            else:
                                whip = float(tmp[18])
                            yearVal = int(year)
                            name = str(tmp[1])
                            teamname = str(tmp[2])
                            g = int(tmp[4])
                            w = int(tmp[5])
                            l = int(tmp[6])
                            sv = int(tmp[7])
                            hld = int(tmp[8])
                            h = int(tmp[11])
                            hr = int(tmp[12])
                            bb = int(tmp[13])
                            hbp = int(tmp[14])
                            so = int(tmp[15])
                            r = int(tmp[16])
                            er = int(tmp[17])
                        else:
                            if tmp[3] == '-':
                                era = 0
                            else:
                                era = float(tmp[3])
                            if tmp[9] == '-':
                                wpct = 0
                            else:
                                wpct = float(tmp[9])
                            if tmp[19] == '-':
                                whip = 0
                            else:
                                whip = float(tmp[19])
                            yearVal = int(year)
                            name = str(tmp[1])
                            teamname = str(tmp[2])
                            g = int(tmp[4])
                            w = int(tmp[5])
                            l = int(tmp[6])
                            sv = int(tmp[7])
                            hld = int(tmp[8])
                            ip = int(tmp[10]) + float(int(tmp[11].split("/")[0]) / int(
                                tmp[11].split("/")[1]))
                            h = int(tmp[12])
                            hr = int(tmp[13])
                            bb = int(tmp[14])
                            hbp = int(tmp[15])
                            so = int(tmp[16])
                            r = int(tmp[17])
                            er = int(tmp[18])

                        sql = """insert into pitcherdb
                                              (name, teamName, year, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)
                                              values('%s', '%s', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%f')
                                              """ % (
                        name, teamname, yearVal, era, g, w, l, sv, hld, wpct, ip, h, hr, bb, hbp, so, r, er, whip)

                        cur.execute(sql)
                        conn.commit()

                flag = False

    conn.close()