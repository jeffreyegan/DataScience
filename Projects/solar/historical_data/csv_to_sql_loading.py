import sqlite3, os

db_path = os.path.join("..", "solar.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()


add_enphase = False
add_rec = False

if add_enphase:
    f = open("solar_production.csv")
    line = f.readline()  # header
    line = f.readline()  # first row
    while not line == '':
        print(line.split(","))
        q = "INSERT OR REPLACE INTO production (date, energy_Wh) VALUES ('"+line.split(",")[0]+"', "+line.split(",")[1][:-1]+")"
        cur.execute(q)
        line = f.readline()
    conn.commit()
    conn.close()
    f.close()


if add_rec:
    month = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
    f = open("rec.csv")
    line = f.readline()  # header
    line = f.readline()  # first row
    while not line == '':
            #print(line.split(","))
            v1 = str(month[line.split(',')[0][0:3]])
            v2 = str(line.split(',')[0][-2:])
            v3 = str(line.split(',')[1])
            v4 = line.split(',')[2][:-1]
            v5 = str(v4.split('/')[0])
            v6 = str(v4.split('/')[1])
            v7 = str(v4.split('/')[2])
            q = "INSERT OR REPLACE INTO rec (month, year, reading, date_recorded, r_mo, r_dy, r_yr) VALUES ("+v1+", "+v2+", "+v3+", '"+v4+"', "+v5+", "+v6+", "+v7+")"
            print(q)
            cur.execute(q)
            conn.commit()
            line = f.readline()
    f.close()


conn.close()