from setYear import setYear
from setTeam import setTeam
from setSeason import setSeason
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
                runnerTable = driver.find_element_by_xpath("//*[@id='cphContents_cphContents_cphContents_udpContent']/div[2]/table")
                lines = runnerTable.find_elements_by_tag_name("tr")

                for i in range(len(lines)):
                    if i != 0:
                        tmp = lines[i].text.split(' ')

                        if tmp[7] == '-':
                            sbper = 0
                        else:
                            sbper = float(tmp[7])
                        yearVal = int(year)
                        name = str(tmp[1])
                        teamname = str(tmp[2])
                        g = int(tmp[3])
                        sba = int(tmp[4])
                        sb = int(tmp[5])
                        cs = int(tmp[6])
                        oob = int(tmp[8])
                        pko = int(tmp[9])

                        sql = """insert into runnerdb
                                              (name, teamName, year, g, sba, sb, cs, sbper, oob, pko)
                                              values('%s', '%s', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d')
                                              """ % (name, teamname, yearVal, g, sba, sb, cs, sbper, oob, pko)

                        cur.execute(sql)
                        conn.commit()

                flag = False

    conn.close()