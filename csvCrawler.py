from selenium import webdriver
import csv
import time
import pymysql


def crawling(f, driver, conn, year):
    wr = csv.writer(f)

    game_list = driver.find_element_by_xpath("//*[@id='contents']/div[3]/div/div[1]/ul")
    games = game_list.find_elements_by_tag_name("li")

    table = []
    tmp = []
    actual = []

    cur = conn.cursor()

    for game in games:
        isDone = game.find_element_by_class_name("time")


        if isDone.text != "경기종료":
            continue

        game.click()
        time.sleep(2)

        awayScore = driver.find_element_by_xpath("//*[@id='tblScordboard3']/tbody/tr[1]/td[1]")
        actual.clear()
        actual.append(awayScore.text)

        # lblHomePitcher --------------------------------------------------------------------
        table.clear()
        cnt = 0

        pitcherTable = driver.find_element_by_xpath("//*[@id='tblHomePitcher']")
        lines = pitcherTable.find_elements_by_tag_name("tr")

        for line in lines:
            name = line.text.split(' ')[0]

            if name != "선수명" and name != "TOTAL":
                sql = "SELECT * FROM pitcherdb WHERE name=%s and year=%s"
                cur.execute(sql, (name, year))
                rows = cur.fetchall()

                for row in rows:
                    tmp.clear()
                    cnt += 1

                    for i in range(4, 20):
                        tmp.append(row[i])

                    table.append(tmp.copy())

        tmp.clear()

        for j in range(len(table[0])):
            sum = 0

            for i in range(len(table)):
                sum += float(table[i][j])

            avg = sum / cnt
            tmp.append(avg)
            actual.append(avg)

        # lblAwayHitter --------------------------------------------------------------------
        table.clear()
        cnt = 0

        hitterTable = driver.find_element_by_xpath("//*[@id='tblAwayHitter1']/tbody")
        lines = hitterTable.find_elements_by_tag_name("tr")

        idx = 0

        for line in lines:
            name = line.text.split(' ')[2]
            idx += 1

            records = driver.find_element_by_xpath("//*[@id='tblAwayHitter2']/table/tbody/tr[" + str(idx) + "]").text
            records = records.split(' ')

            for record in records:
                if record != "":
                    sql = "SELECT * FROM hitterdb WHERE name=%s and year=%s"
                    cur.execute(sql, (name, year))
                    rows = cur.fetchall()

                    for row in rows:
                        tmp.clear()
                        cnt += 1

                        for i in range(4, 17):
                            tmp.append(row[i])

                        table.append(tmp.copy())
                    break

        tmp.clear()

        for j in range(len(table[0])):
            sum = 0

            for i in range(len(table)):
                sum += float(table[i][j])

            avg = sum / cnt
            tmp.append(avg)
            actual.append(avg)

        wr.writerow(actual)
        actual.clear()

        homeScore = driver.find_element_by_xpath("//*[@id='tblScordboard3']/tbody/tr[2]/td[1]")
        actual.append(homeScore.text)

        # lblAwayPitcher --------------------------------------------------------------------
        table.clear()
        cnt = 0

        pitcherTable = driver.find_element_by_xpath("//*[@id='tblAwayPitcher']")
        lines = pitcherTable.find_elements_by_tag_name("tr")

        for line in lines:
            name = line.text.split(' ')[0]

            if name != "선수명" and name != "TOTAL":
                sql = "SELECT * FROM pitcherdb WHERE name=%s and year=%s"
                cur.execute(sql, (name, year))
                rows = cur.fetchall()

                for row in rows:
                    tmp.clear()
                    cnt += 1

                    for i in range(4, 20):
                        tmp.append(row[i])

                    table.append(tmp.copy())

        tmp.clear()

        for j in range(len(table[0])):
            sum = 0

            for i in range(len(table)):
                sum += float(table[i][j])

            avg = sum / cnt
            tmp.append(avg)
            actual.append(avg)

        # lblHomeHitter --------------------------------------------------------------------
        table.clear()
        cnt = 0

        hitterTable = driver.find_element_by_xpath("//*[@id='tblHomeHitter1']/tbody")
        lines = hitterTable.find_elements_by_tag_name("tr")

        idx = 0

        for line in lines:
            name = line.text.split(' ')[2]
            idx += 1

            records = driver.find_element_by_xpath(
                "//*[@id='tblHomeHitter2']/table/tbody/tr[" + str(idx) + "]").text
            records = records.split(' ')

            for record in records:
                if record != "":
                    sql = "SELECT * FROM hitterdb WHERE name=%s and year=%s"
                    cur.execute(sql, (name, year))
                    rows = cur.fetchall()

                    for row in rows:
                        tmp.clear()
                        cnt += 1

                        for i in range(4, 17):
                            tmp.append(row[i])

                        table.append(tmp.copy())
                    break

        tmp.clear()

        for j in range(len(table[0])):
            sum = 0

            for i in range(len(table)):
                sum += float(table[i][j])

            avg = sum / cnt
            tmp.append(avg)
            actual.append(avg)

        wr.writerow(actual)