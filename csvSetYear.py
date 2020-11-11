from selenium import webdriver
import time


def setYear(yearValue, driver):
    option = driver.find_element_by_xpath("//*[@id='contents']/div[2]/ul/li[2]/img")
    option.click()
    time.sleep(2)

    year = driver.find_element_by_xpath(
        "//*[@id='ui-datepicker-div']/div/div/select[2]/option[@value='" + str(yearValue) + "']")
    year.click()

    if yearValue == 2010: #2010.03.27
        month = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value='" + str(2) + "']")
        month.click()

        time.sleep(2)

        day = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(4) + "]/td[" + str(7) + "]/a")
        day.click()
    elif yearValue == 2011: #2011.04.02
        month = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value='" + str(3) + "']")
        month.click()

        time.sleep(2)

        day = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(1) + "]/td[" + str(7) + "]/a")
        day.click()
    elif yearValue == 2012: #2012.04.07
        month = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/div/div/select[1]/option[@value='" + str(3) + "']")
        month.click()

        time.sleep(2)

        day = driver.find_element_by_xpath(
            "//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(1) + "]/td[" + str(7) + "]/a")
        day.click()
    else: #todo : set other years
        print("Hi")