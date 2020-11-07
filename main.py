#selenium 패키지 설치 terminal -> pip install selenium
#pymysql 패키지 설치 terminal -> pip install pymysql
from setDB import setDB
from crawling import crawling
import csvGenerator
import testCsvGenerator
from test import test


if __name__ == "__main__":
    choice = 0

    while choice != 7:
        print("1. 필요 패키지 설명")
        print("2. DB 세팅")
        print("3. Crawling 실행")
        print("4. csv 생성")
        print("5. csv 테스트 모듈")
        print("6. 테스트 csv 생성")
        print("7. 종료")
        choice = int(input("원하는 설정을 입력하세요 : "))

        if choice == 1:
            print("이 프로그램을 실행하기 위해서는 다음과 같은 것들이 설치돼야 합니다.")
            print("\n------------------------")
            print("1. MySQL")
            print("2. Selenium")
            print("3. pymysql")
            print("------------------------\n")
        elif choice == 2:
            setDB()
        elif choice == 3:
            crawling()
        elif choice == 4:
            csvGenerator.generate()
        elif choice == 5:
            test()
        elif choice == 6:
            testCsvGenerator.generate()
        elif choice != 7:
            print("다시 입력해주세요")

"""
    00 : OB LT SS HH HD HT LG SK
    01 : OB LT SS HH HD HT LG SK
    02 : OB LT SS HH HD HT LG SK
    03 : OB LT SS HH HD HT LG SK
    04 : OB LT SS HH HD HT LG SK
    05 : OB LT SS HH HD HT LG SK
    06 : OB LT SS HH HD HT LG SK
    07 : OB LT SS HH HD HT LG SK

    08 : OB LT SS HH    HT LG SK WO
    09 : OB LT SS HH    HT LG SK WO
    10 : OB LT SS HH    HT LG SK WO
    11 : OB LT SS HH    HT LG SK WO
    12 : OB LT SS HH    HT LG SK WO

    13 : OB LT SS HH    HT LG SK WO NC
    14 : OB LT SS HH    HT LG SK WO NC

    15 : OB LT SS HH    HT LG SK WO NC KT
    16 : OB LT SS HH    HT LG SK WO NC KT
    17 : OB LT SS HH    HT LG SK WO NC KT
    18 : OB LT SS HH    HT LG SK WO NC KT
    19 : OB LT SS HH    HT LG SK WO NC KT
    20 : OB LT SS HH    HT LG SK WO NC KT
 """