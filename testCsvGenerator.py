from makeTestCsv import controler
import csv

def generate() :
    f = open('KBO_test_data.csv', 'w', encoding='utf-8', newline="")

    wr = csv.writer(f)
    wr.writerow(['era', 'g', 'w', 'l', 'sv', 'hld', 'wpct', 'ip','h', 'hr', 'bb', 'hbp', 'so', 'r', 'er', 'whip', 'avg', 'g', 'pa', 'ab', 'r', 'h', '2b', '3b', 'hr', 'tb', 'rbi', 'sac', 'sf'])

    controler(f)

    f.close()