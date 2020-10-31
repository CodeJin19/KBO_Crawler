from selenium import webdriver
import csv
import pymysql
import time

def test():
    f = open('KBO_data.csv', 'w', encoding='utf-8', newline="")

    wr = csv.writer(f)
    wr.writerow(
        ['score', 'era', 'g', 'w', 'l', 'sv', 'hld', 'wpct', 'ip', 'h', 'hr', 'bb', 'hbp', 'so', 'r', 'er', 'whip',
         'avg', 'g', 'pa', 'ab', 'r', 'h', '2b', '3b', 'hr', 'tb', 'rbi', 'sac', 'sf'])

    passwd = input("비번을 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')
    time.sleep(2)

    try:
        # 웹페이지 연결
        driver.get('https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx')
        time.sleep(2)

        option = driver.find_element_by_xpath("//*[@id='contents']/div[2]/ul/li[2]/img")
        option.click()
        time.sleep(2)

        year = 2010

        driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]/option[@value='" + str(year) + "']").click()
        driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value='" + str(8) + "']").click()
        driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(4) + "]/td[" + str(3) + "]/a").click()

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
            print("lblHomePitcher")
            table.clear()
            cnt = 0

            pitcherTable = driver.find_element_by_xpath("//*[@id='tblHomePitcher']")
            lines = pitcherTable.find_elements_by_tag_name("tr");

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
            print("lblAwayHitter")
            table.clear()
            cnt = 0

            hitterTable = driver.find_element_by_xpath("//*[@id='tblAwayHitter1']/tbody")
            lines = hitterTable.find_elements_by_tag_name("tr");

            idx = 0

            for line in lines:
                name = line.text.split(' ')[2]
                idx += 1

                records = driver.find_element_by_xpath(
                    "//*[@id='tblAwayHitter2']/table/tbody/tr[" + str(idx) + "]").text
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
            print("lblAwayPitcher")
            table.clear()
            cnt = 0

            pitcherTable = driver.find_element_by_xpath("//*[@id='tblAwayPitcher']")
            lines = pitcherTable.find_elements_by_tag_name("tr");

            print("test1")
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
            print("test2")

            for j in range(len(table[0])):
                sum = 0

                for i in range(len(table)):
                    sum += float(table[i][j])

                avg = sum / cnt
                tmp.append(avg)
                actual.append(avg)

            # lblHomeHitter --------------------------------------------------------------------
            print("lblHomeHitter")
            table.clear()
            cnt = 0

            hitterTable = driver.find_element_by_xpath("//*[@id='tblHomeHitter1']/tbody")
            lines = hitterTable.find_elements_by_tag_name("tr");

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

    except BaseException as e:
        print("----------------------------------")
        print("error :")
        print(e)
        print("----------------------------------")
    finally:
        driver.quit()
        print("quit driver")