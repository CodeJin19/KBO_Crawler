import setYear
import setTeam
import setSeason
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
            setSeason.setSeason(driver)

            flag = True
            page = 1

            while(flag):
                defenceTable = driver.find_element_by_xpath("//*[@id='cphContents_cphContents_cphContents_udpContent']/div[2]/table")
                lines = defenceTable.find_elements_by_tag_name("tr")

                for i in range(len(lines)):
                    if i != 0:
                        tmp = lines[i].text.split(' ')

                        if len(tmp) == 17:
                            if '/' in tmp[6]:
                                ip = float(int(tmp[6].split("/")[0]) / int(
                                        tmp[6].split("/")[1]))
                            else:
                                ip = float(tmp[6])
                            if tmp[12] == '-':
                                fpct = 0
                            else:
                                fpct = float(tmp[12])
                            if tmp[16] == '-':
                                csper = 0
                            else:
                                csper = float(tmp[16])
                            yearVal = int(year)
                            name = str(tmp[1])
                            teamname = str(tmp[2])
                            g = int(tmp[4])
                            gs = int(tmp[5])
                            e = int(tmp[7])
                            pko = int(tmp[8])
                            po = int(tmp[9])
                            a = int(tmp[10])
                            dp = int(tmp[11])
                            pb = int(tmp[13])
                            sb = int(tmp[14])
                            cs = int(tmp[15])

                        else:
                            if tmp[17] == '-':
                                csper = 0
                            else:
                                csper = float(tmp[17])
                            if tmp[13] == '-':
                                fpct = 0
                            else:
                                fpct = float(tmp[13])
                            yearVal = int(year)
                            name = str(tmp[1])
                            teamname = str(tmp[2])
                            g = int(tmp[4])
                            gs = int(tmp[5])
                            ip = int(tmp[6]) + float(int(tmp[7].split("/")[0]) / int(
                                tmp[7].split("/")[1]))
                            e = int(tmp[8])
                            pko = int(tmp[9])
                            po = int(tmp[10])
                            a = int(tmp[11])
                            dp = int(tmp[12])
                            pb = int(tmp[14])
                            sb = int(tmp[15])
                            cs = int(tmp[16])

                        sql = """insert into defencedb
                                              (name, teamName, year, g, gs, ip, e, pko, po, a, dp, fpct, pb, sb, cs, csper)
                                              values('%s', '%s', '%d', '%d', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d', '%d', '%f')
                                              """ % (
                        name, teamname, yearVal, g, gs, ip, e, pko, po, a, dp, fpct, pb, sb, cs, csper)

                        cur.execute(sql)
                        conn.commit()

                cnt = len(driver.find_elements_by_id("cphContents_cphContents_cphContents_ucPager_btnNo2"))

                if 0 < cnt :
                    if page == 1:
                        driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo2").click()
                        page = 2
                        time.sleep(2)
                        flag = True
                    elif page == 2:
                        driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo3").click()
                        page = 3
                        time.sleep(2)
                        flag = True
                    else:
                        driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo1").click()
                        page = 1
                        time.sleep(2)
                        flag = False
                else:
                    flag = False

    conn.close()
