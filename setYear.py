import time

def setYear(yearValue, driver):
    # 스크롤다운 옵션에서 년도 설정 및 대기

    year = driver.find_element_by_xpath(
        "//select[@id='cphContents_cphContents_cphContents_ddlSeason_ddlSeason']/option[@value='" + str(
            yearValue) + "']")
    year.click()
    time.sleep(2)