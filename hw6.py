import sqlite3
db = sqlite3.connect('Students')
r = db.cursor()

r.execute('''CREATE TABLE IF NOT EXISTS
students(
name text, 
surname text,
hobby text, 
birth_year integer,
point integer           

)''')
r.execute("INSERT INTO students VALUES('Atsumu', 'Miya', 'valleyball', 2005, 12)")
r.execute("INSERT INTO students VALUES('Osamu', 'Miya', 'valleyball', 2005, 9)")
r.execute("INSERT INTO students VALUES('Tooru', 'Oikawa', 'valleyball', 2004,9)")
r.execute("INSERT INTO students VALUES('Tobio', 'Kageyama', 'valleyball', 2006, 10)")
r.execute("INSERT INTO students VALUES('Key', 'Tsukishima', 'valleyball', 2006, 8)")
r.execute("INSERT INTO students VALUES('Kenma', 'Kozume', 'valleyball', 2006, 7)")
r.execute("INSERT INTO students VALUES('Iwaizumi', 'Hajime', 'valleyball', 2005, 9)")
r.execute("INSERT INTO students VALUES('Ushijima', 'Wakatoshi', 'valleyball', 2004, 10)")
r.execute("INSERT INTO students VALUES('Hinata', 'Shoyo', 'valleyball', 2006, 10)")
r.execute("INSERT INTO students VALUES('Tetsuro', 'Kuroo', 'valleyball', 2005, 8)")
r.execute("SELECT * FROM students")

r.execute("UPDATE students SET name = 'genius' WHERE point >=10")
r.execute("SELECT rowid, * FROM students")

item = r.fetchall()
for i in item:
    print(i)
for i in item:
    surname = i[1]
    if len(surname) >= 10:
        print(surname)
    else:
        ...
r.execute("SELECT rowid, name FROM students WHERE name = 10 ")
r.execute("DELETE FROM students WHERE rowid % 2 = 0")

print(r.fetchall())
db.commit()
db.close()

