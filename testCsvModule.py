import csv
import pymysql

def generator(f, conn, team1, team2, year):
    wr = csv.writer(f)

    table = []
    tmp = []
    actual = []
    cnt = 0

    cur = conn.cursor()

    sql = "SELECT * FROM pitcherdb WHERE teamname=%s and year=%s"
    cur.execute(sql, (teamName[i], year))
    rows = cur.fetchall()

    for row in rows:
        tmp.clear()
        cnt += 1

        for k in range(4, 20):
            tmp.append(row[k])

        table.append(tmp.copy())

    tmp.clear()

    for k in range(len(table[0])):
        sum = 0

        for l in range(len(table)):
            sum += float(table[l][k])

        avg = sum / cnt
        tmp.append(avg)
        actual.append(avg)

    table.clear()
    cnt = 0

    sql = "SELECT * FROM hitterdb WHERE teamname=%s and year=%s"
    cur.execute(sql, (teamName[j], year))
    rows = cur.fetchall()

    for row in rows:
        tmp.clear()
        cnt += 1

        for k in range(4, 17):
            tmp.append(row[k])

        table.append(tmp.copy())

    tmp.clear()

    for k in range(len(table[0])):
        sum = 0

        for l in range(len(table)):
            sum += float(table[l][k])

        avg = sum / cnt
        tmp.append(avg)
        actual.append(avg)

    wr.writerow(actual)
    actual.clear()