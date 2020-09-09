#selenium 패키지 설치 terminal -> pip install selenium
#pymysql 패키지 설치 terminal -> pip install pymysql
from utils import crawling, setDB

if __name__ == "__main__":

    choice = 0

    while choice != 4:
        print("1. 필요 패키지 설명")
        print("2. DB 세팅")
        print("3. Crawling 실행")
        print("4. 종료")
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
        elif choice != 4:
            print("다시 입력해주세요")