from selenium import webdriver
from csvCrawler import crawling
from csvSetYear import setYear
import csv
import time
import pymysql


def controler(f):
    print("몇 년도부터 크롤링할 지 입력하세요 (최소 2010) YYYY: ")
    yearFrom = int(input())
    print("몇 년도까지 크롤링할 지 입력하세요 (최대 2012) YYYY: ")
    yearTo = int(input())
    yearTo += 1

    passwd = input("비번을 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')

    # driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver', options=options)
    time.sleep(2)

    try:
        # 웹페이지 연결
        driver.get('https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx')
        time.sleep(2)

        for year in range(yearFrom, yearTo):
            setYear(year, driver)

            date = driver.find_element_by_xpath("//*[@id='lblGameDate']")
            dateString = date.text
            yearString = dateString[0:4]

            while yearString != str(yearTo):
                print(dateString)

                try:
                    crawling(f, driver, conn, year)
                except BaseException as e:
                    print(dateString + str(e))

                bttn = driver.find_element_by_xpath("//*[@id='lnkNext']")
                bttn.click()

                date = driver.find_element_by_xpath("//*[@id='lblGameDate']")
                dateString = date.text
                yearString = dateString[0:4]


    except BaseException as e:
        print("----------------------------------")
        print("error :")
        print(e)
        print("----------------------------------")
    finally:
        driver.quit()
        print("quit driver")

"""
    # driver 연결 및 대기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver', options=options)
"""
"""
2010 : 1 / 2 감소
2010.09.21

2010.04.09(금)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblAwayHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2010.04.11(일)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblAwayHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2010.06.06(일)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblHomeHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2010.07.24(토)list index out of range

2010.09.16(목)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblHomeHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2010.10.13(수)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblAwayHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)


2011 : 8 / 17 감소
2011.03.13
2011.05.12
2011.06.18
2011.07.06
2011.07.31
2011.08.14
2011.09.25
2011.10.04

2011.04.10(일)list index out of range

2011.04.13(수)list index out of range

2011.05.11(수)list index out of range

2011.05.15(일)list index out of range

2011.05.21(토)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblHomeHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2011.07.01(금)list index out of range

2011.07.08(금)list index out of range

2011.07.23(토)list index out of range

2011.08.10(수)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblAwayHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2011.09.09(금)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblHomeHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2011.09.13(화)list index out of range

2011.10.06(목)list index out of range


2012 : 12 / 59 감소
2012.03.30
2012.04.19
2012.04.26
2012.05.13
2012.06.06
2012.06.07
2012.07.08
2012.08.21
2012.08.29
2012.09.06
2012.09.19
2012.09.26

2012.03.21(수)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblAwayHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2012.03.24(토)list index out of range

2012.04.01(일)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblAwayHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2012.04.13(금)list index out of range

2012.04.28(토)list index out of range

2012.04.29(일)list index out of range

2012.05.04(금)list index out of range

2012.05.06(일)list index out of range

2012.05.09(수)list index out of range

2012.05.25(금)list index out of range

2012.05.31(목)list index out of range

2012.06.01(금)list index out of range

2012.06.12(화)list index out of range

2012.06.13(수)list index out of range

2012.06.17(일)list index out of range

2012.06.21(목)list index out of range

2012.06.30(토)list index out of range

2012.07.04(수)list index out of range

2012.07.12(목)list index out of range

2012.07.13(금)list index out of range

2012.07.18(수)list index out of range

2012.07.19(목)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblHomeHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.75)

2012.07.21(토)list index out of range

2012.07.26(목)list index out of range

2012.08.01(수)list index out of range

2012.08.02(목)list index out of range

2012.08.04(토)list index out of range

2012.08.05(일)list index out of range

2012.08.07(화)list index out of range

2012.08.08(수)list index out of range

2012.08.11(토)list index out of range

2012.08.17(금)list index out of range

2012.08.19(일)list index out of range

2012.08.25(토)list index out of range

2012.09.02(일)list index out of range

2012.09.05(수)list index out of range

2012.09.10(월)list index out of range

2012.09.12(수)list index out of range

2012.09.14(금)list index out of range

2012.09.15(토)list index out of range

2012.09.16(일)list index out of range

2012.09.22(토)list index out of range

2012.09.23(일)list index out of range

2012.09.25(화)list index out of range

2012.09.27(목)list index out of range

2012.09.28(금)list index out of range

2012.09.29(토)list index out of range

2012.10.01(월)list index out of range

2012.10.02(화)list index out of range

2012.10.05(금)list index out of range

2012.11.08(목)Message: element click intercepted: Element <li game_sc="3" le_id="1" sr_id="8" season="2012" g_id="20121108LMCS0" g_dt="20121108" s_nm="사직" vs_game_cn="1" away_id="LM" home_id="CS" away_nm="라미고" home_nm="차이나" away_p_id="10207" home_p_id="10308" entry_ck="1" start_ck="1" result_ck="0" lineup_ck="0" vod_ck="0" kbot_se="0" class="list-review" style="float: left; list-style: none; position: relative; width: 160px; margin-right: 9px;">...</li> is not clickable at point (993, 353). Other element would receive the click: <div class="bx-loading"></div>
  (Session info: headless chrome=86.0.4240.75)

2012.11.09(금)Message: element click intercepted: Element <li game_sc="3" le_id="1" sr_id="8" season="2012" g_id="20121109PEYO0" g_dt="20121109" s_nm="사직" vs_game_cn="1" away_id="PE" home_id="YO" away_nm="퍼스" home_nm="요미우리" away_p_id="10102" home_p_id="10416" entry_ck="1" start_ck="1" result_ck="0" lineup_ck="0" vod_ck="0" kbot_se="0" class="list-review" style="float: left; list-style: none; position: relative; width: 160px; margin-right: 9px;">...</li> is not clickable at point (993, 353). Other element would receive the click: <div class="bx-loading"></div>
  (Session info: headless chrome=86.0.4240.75)

2012.11.10(토)Message: element click intercepted: Element <li game_sc="3" le_id="1" sr_id="8" season="2012" g_id="20121110YOLT0" g_dt="20121110" s_nm="사직" vs_game_cn="1" away_id="YO" home_id="LT" away_nm="요미우리" home_nm="롯데" away_p_id="10402" home_p_id="79349" entry_ck="1" start_ck="1" result_ck="0" lineup_ck="0" vod_ck="0" kbot_se="0" class="list-review" style="float: left; list-style: none; position: relative; width: 160px; margin-right: 9px;">...</li> is not clickable at point (993, 353). Other element would receive the click: <div class="bx-loading"></div>
  (Session info: headless chrome=86.0.4240.75)

2012.11.11(일)Message: element click intercepted: Element <li game_sc="3" le_id="1" sr_id="8" season="2012" g_id="20121111YOLM0" g_dt="20121111" s_nm="사직" vs_game_cn="1" away_id="YO" home_id="LM" away_nm="요미우리" home_nm="라미고" away_p_id="10405" home_p_id="10216" entry_ck="1" start_ck="1" result_ck="0" lineup_ck="0" vod_ck="0" kbot_se="0" class="list-review" style="float: left; list-style: none; position: relative; width: 160px; margin-right: 9px;">...</li> is not clickable at point (1077, 353). Other element would receive the click: <div class="bx-loading"></div>
  (Session info: headless chrome=86.0.4240.75)


2013 : 12 / 59 감소
2013.03.02(토)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.03(일)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.04(월)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.05(화)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.06(수)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.08(금)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.09(토)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.10(일)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.11(월)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.12(화)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.13(수)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.14(목)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.15(금)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.16(토)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.17(일)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.18(월)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.19(화)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.20(수)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='contents']/div[3]/div/div[1]/ul"}
  (Session info: headless chrome=86.0.4240.183)

2013.03.21(목)list index out of range

2013.03.23(토)list index out of range

2013.04.02(화)list index out of range

2013.04.10(수)list index out of range

2013.04.12(금)list index out of range

2013.04.14(일)list index out of range

2013.04.16(화)list index out of range

2013.04.19(금)list index out of range

2013.04.21(일)list index out of range

2013.04.24(수)list index out of range

2013.04.27(토)list index out of range

2013.04.28(일)list index out of range

2013.04.30(화)list index out of range

2013.05.01(수)list index out of range

2013.05.02(목)list index out of range

2013.05.03(금)list index out of range

2013.05.07(화)list index out of range

2013.05.09(목)list index out of range

2013.05.12(일)list index out of range

2013.05.14(화)list index out of range

2013.05.15(수)list index out of range

2013.05.16(목)list index out of range

2013.05.19(일)list index out of range

2013.05.22(수)list index out of range

2013.05.23(목)list index out of range

2013.05.25(토)list index out of range

2013.05.26(일)list index out of range

2013.05.29(수)list index out of range

2013.05.31(금)list index out of range

2013.06.01(토)list index out of range

2013.06.02(일)list index out of range

2013.06.04(화)list index out of range

2013.06.06(목)list index out of range

2013.06.08(토)list index out of range

2013.06.11(화)list index out of range

2013.06.12(수)list index out of range

2013.06.15(토)list index out of range

2013.06.19(수)list index out of range

2013.06.20(목)list index out of range

2013.06.22(토)list index out of range

2013.06.26(수)list index out of range

2013.06.27(목)list index out of range

2013.06.28(금)list index out of range

2013.07.02(화)list index out of range

2013.07.03(수)list index out of range

2013.07.06(토)list index out of range

2013.07.09(화)list index out of range

2013.07.11(목)list index out of range

2013.07.12(금)list index out of range

2013.07.16(화)Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='tblAwayHitter2']/table/tbody/tr[1]"}
  (Session info: headless chrome=86.0.4240.183)
  
2013.07.17(수)list index out of range

2013.07.23(화)list index out of range

2013.07.24(수)list index out of range

2013.07.26(금)list index out of range

2013.07.27(토)list index out of range

2013.07.30(화)list index out of range

2013.08.01(목)list index out of range

2013.08.02(금)list index out of range

2013.08.06(화)list index out of range

2013.08.08(목)list index out of range

2013.08.09(금)list index out of range

2013.08.10(토)list index out of range

2013.08.13(화)list index out of range

2013.08.14(수)list index out of range

2013.08.16(금)list index out of range

2013.08.17(토)list index out of range

2013.08.18(일)list index out of range

2013.08.20(화)list index out of range

2013.08.22(목)list index out of range

2013.08.23(금)list index out of range

2013.08.25(일)list index out of range

2013.08.28(수)list index out of range

2013.08.29(목)list index out of range

2013.08.30(금)list index out of range

2013.08.31(토)list index out of range

2013.09.05(목)list index out of range

2013.09.08(일)list index out of range

2013.09.10(화)list index out of range

2013.09.11(수)list index out of range

2013.09.12(목)list index out of range

2013.09.14(토)list index out of range

2013.09.15(일)list index out of range

2013.09.16(월)list index out of range

2013.09.17(화)list index out of range

2013.09.18(수)list index out of range

2013.09.21(토)list index out of range

2013.09.24(화)list index out of range

2013.09.25(수)list index out of range

2013.09.26(목)list index out of range

2013.09.27(금)list index out of range

2013.09.28(토)list index out of range

2013.09.29(일)list index out of range

2013.09.30(월)list index out of range

2013.10.01(화)list index out of range

2013.10.02(수)list index out of range

2013.10.04(금)list index out of range

2013.11.15(금)Message: element click intercepted: Element <li game_sc="3" le_id="1" sr_id="8" season="2013" g_id="20131115FBSS0" g_dt="20131115" s_nm="타이중" vs_game_cn="1" away_id="FB" home_id="SS" away_nm="볼로냐" home_nm="삼성" entry_ck="1" start_ck="0" result_ck="0" lineup_ck="0" vod_ck="0" kbot_se="0" class="list-review" style="float: left; list-style: none; position: relative; width: 160px; margin-right: 9px;">...</li> is not clickable at point (1077, 353). Other element would receive the click: <div class="bx-loading"></div>
  (Session info: headless chrome=86.0.4240.183)

2013.11.17(일)Message: element click intercepted: Element <li game_sc="3" le_id="1" sr_id="8" season="2013" g_id="20131117SSTE0" g_dt="20131117" s_nm="타오위앤" vs_game_cn="1" away_id="SS" home_id="TE" away_nm="삼성" home_nm="퉁이" entry_ck="1" start_ck="0" result_ck="0" lineup_ck="0" vod_ck="0" kbot_se="0" class="list-review" style="float: left; list-style: none; position: relative; width: 160px; margin-right: 9px;">...</li> is not clickable at point (1077, 353). Other element would receive the click: <div class="bx-loading"></div>
  (Session info: headless chrome=86.0.4240.183)

2013.11.18(월)Message: element click intercepted: Element <li game_sc="3" le_id="1" sr_id="8" season="2013" g_id="20131118CVSS0" g_dt="20131118" s_nm="타이중" vs_game_cn="1" away_id="CV" home_id="SS" away_nm="캔버라" home_nm="삼성" entry_ck="1" start_ck="0" result_ck="0" lineup_ck="0" vod_ck="0" kbot_se="0" class="list-review" style="float: left; list-style: none; position: relative; width: 160px; margin-right: 9px;">...</li> is not clickable at point (1077, 353). Other element would receive the click: <div class="bx-loading"></div>
  (Session info: headless chrome=86.0.4240.183)
"""