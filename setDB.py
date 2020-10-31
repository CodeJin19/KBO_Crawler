import pymysql

def setDB():
    passwd = input("비번을 입력하세요 : ")

    conn = pymysql.connect(host='localhost', user='root', password=passwd, db='sample', charset='utf8')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS hitterDB")
    cur.execute("CREATE TABLE hitterDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), avg DOUBLE(4, 3), g INT(3), pa INT(3), ab INT(3), r INT(3), h INT(3), 2b INT(3), 3b INT(3), hr INT(3), tb INT(3), rbi INT(3), sac INT(3), sf INT(3))")
    """
    cur.execute("DROP TABLE IF EXISTS pitcherDB")
    cur.execute("CREATE TABLE pitcherDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), era DOUBLE(4, 2), g INT(3), w INT(3), l INT(3), sv INT(3), hld INT(3), wpct DOUBLE(4, 3), ip DOUBLE(5, 2), h INT(3), hr INT(3), bb INT(3), hbp INT(3), so INT(3), r INT(3), er INT(3), whip DOUBLE(3, 2))")

    cur.execute("DROP TABLE IF EXISTS defenceDB")
    cur.execute("CREATE TABLE defenceDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), pos VARCHAR(20), g INT(3), gs INT(3), ip VARCHAR(20), e INT(3), pko INT(3), po INT(3), a INT(3), dp INT(3), fpct DOUBLE(4, 3), pb INT(3), sb INT(3), cs INT(3), csper DOUBLE(3, 1))")

    cur.execute("DROP TABLE IF EXISTS runnerDB")
    cur.execute("CREATE TABLE runnerDB(idx INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), teamName VARCHAR(10), year INT(5), g INT(3), sba INT(3), sb INT(3), cs INT(3), sbper DOUBLE(4, 1), oob INT(3), pko INT(3))")
    """
    conn.close()