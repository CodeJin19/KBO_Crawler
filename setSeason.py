import time

def setSeason(driver):
    # 스크롤다운 옵션에서 정규 시즌 설정 및 대기

    team = driver.find_element_by_xpath(
        "//select[@id='cphContents_cphContents_cphContents_ddlSeries_ddlSeries']/option[@value='0']")
    team.click()
    time.sleep(2)