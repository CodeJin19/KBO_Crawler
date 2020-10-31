from selenium.webdriver.common.by import By
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

            flag = True
            page = 1

            print(str(year) + " " + str(team))

            while(flag):
                hitterTable = driver.find_element_by_xpath("//*[@id='cphContents_cphContents_cphContents_udpContent']/div[3]")
                lines = hitterTable.find_elements_by_tag_name("tr")

                for i in range(len(lines)):
                    if i != 0:
                        tmp = lines[i].text.split(' ')

                        if tmp[3] == '-':
                            avg = 0
                        else:
                            avg = float(tmp[3])
                        yearVal = int(year)
                        name = str(tmp[1])
                        teamname = str(tmp[2])
                        g = int(tmp[4])
                        pa = int(tmp[5])
                        ab = int(tmp[6])
                        r = int(tmp[7])
                        h = int(tmp[8])
                        b2 = int(tmp[9])
                        b3 = int(tmp[10])
                        hr = int(tmp[11])
                        tb = int(tmp[12])
                        rbi = int(tmp[13])
                        sac = int(tmp[14])
                        sf = int(tmp[15])

                        sql = """insert into hitterdb
                                          (name, teamName, year, avg, g, pa, ab, r, h, 2b, 3b, hr, tb, rbi, sac, sf)
                                          values('%s', '%s', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')
                                          """ % (name, teamname, yearVal, avg, g, pa, ab, r, h, b2, b3, hr, tb, rbi, sac, sf)

                        cur.execute(sql)
                        conn.commit()

                cnt = len(driver.find_elements_by_id("cphContents_cphContents_cphContents_ucPager_btnNo2"))

                if 0 < cnt :
                    if page == 1:
                        driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo2").click()
                        page = 2
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