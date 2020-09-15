import time

def setTeam(teamValue, driver):
    # 스크롤다운 옵션에서 팀 설정 및 대기

    team = driver.find_element_by_xpath(
        "//select[@id='cphContents_cphContents_cphContents_ddlTeam_ddlTeam']/option[@value='" + str(teamValue) + "']")
    team.click()
    time.sleep(2)