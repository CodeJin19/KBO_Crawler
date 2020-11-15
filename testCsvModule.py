import csv
import pymysql

def generator(f, conn, x, y, year):
    wr = csv.writer(f)

    table = []
    tmp = []
    actual = []
    cnt = 0

    cur = conn.cursor()

    teamList = ['OB', 'LT', 'SS', 'HH', 'HD', 'HT', 'LG', 'SK', 'WO', 'NC', 'KT']
    teamName = ['두산', '롯데', '삼성', '한화', '현대', 'KIA', 'LG', 'SK', '넥센', 'NC', 'KT']

    actual.append(teamList[x])
    actual.append(teamList[y])

    #team1 def
    sql = "SELECT * FROM pitcherdb WHERE teamname=%s and year=%s"
    cur.execute(sql, (teamName[x], year))
    rows = cur.fetchall()

    for row in rows:
        tmp.clear()
        cnt += 1

        for i in range(4, 20):
            tmp.append(row[i])

        table.append(tmp.copy())

    tmp.clear()

    for i in range(len(table[0])):
        sum = 0

        for j in range(len(table)):
            sum += float(table[j][i])

        avg = sum / cnt
        tmp.append(avg)
        actual.append(avg)

    table.clear()
    cnt = 0

    #team2 attck
    sql = "SELECT * FROM hitterdb WHERE teamname=%s and year=%s"
    cur.execute(sql, (teamName[y], year))
    rows = cur.fetchall()

    for row in rows:
        tmp.clear()
        cnt += 1

        for i in range(4, 17):
            tmp.append(row[i])

        table.append(tmp.copy())

    tmp.clear()

    for i in range(len(table[0])):
        sum = 0

        for j in range(len(table)):
            sum += float(table[j][i])

        avg = sum / cnt
        tmp.append(avg)
        actual.append(avg)

    wr.writerow(actual)
    actual.clear()

    actual.append(teamList[y])
    actual.append(teamList[x])

    table.clear()
    cnt = 0

    #team2 def
    sql = "SELECT * FROM pitcherdb WHERE teamname=%s and year=%s"
    cur.execute(sql, (teamName[y], year))
    rows = cur.fetchall()

    for row in rows:
        tmp.clear()
        cnt += 1

        for i in range(4, 20):
            tmp.append(row[i])

        table.append(tmp.copy())

    tmp.clear()

    for i in range(len(table[0])):
        sum = 0

        for j in range(len(table)):
            sum += float(table[j][i])

        avg = sum / cnt
        tmp.append(avg)
        actual.append(avg)

    table.clear()
    cnt = 0

    #team1 attck
    sql = "SELECT * FROM hitterdb WHERE teamname=%s and year=%s"
    cur.execute(sql, (teamName[x], year))
    rows = cur.fetchall()

    for row in rows:
        tmp.clear()
        cnt += 1

        for i in range(4, 17):
            tmp.append(row[i])

        table.append(tmp.copy())

    tmp.clear()

    for i in range(len(table[0])):
        sum = 0

        for j in range(len(table)):
            sum += float(table[j][i])

        avg = sum / cnt
        tmp.append(avg)
        actual.append(avg)

    wr.writerow(actual)
    actual.clear()