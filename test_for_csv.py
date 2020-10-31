from selenium import webdriver
import csv
import time

def test():
    driver = webdriver.Chrome('C:\ChromeDriver\chromedriver')
    time.sleep(2)

    try:
        # 웹페이지 연결
        driver.get('https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx')
        time.sleep(2)

        option = driver.find_element_by_xpath("//*[@id='contents']/div[2]/ul/li[2]/img")
        option.click()
        time.sleep(2)

        driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]/option[@value='" + str(2010) + "']").click()
        driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value='" + str(2) + "']").click()
        driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(4) + "]/td[" + str(7) + "]/a").click()

        game_list = driver.find_element_by_xpath("//*[@id='contents']/div[3]/div/div[1]/ul")
        games = game_list.find_elements_by_tag_name("li")

        table = []
        tmp = []
        actual = []

        for game in games:
            isDone = game.find_element_by_class_name("time")

            if isDone.text != "경기종료":
                continue

            game.click()
            time.sleep(2)
            x = input()

    except BaseException as e:
        print("----------------------------------")
        print("error :")
        print(e)
        print("----------------------------------")
    finally:
        driver.quit()
        print("quit driver")