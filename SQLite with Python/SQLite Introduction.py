import sqlite3

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS example(Language VARCHAR, Version REAL, Skill TEXT)")

create_table()

def enter_static_data():
    c.execute("INSERT INTO example VALUES ('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES ('Java', 8.2, 'Intermediate')")
    c.execute("INSERT INTO example VALUES ('C++', 10.2, 'Advanced')")
    c.execute("INSERT INTO example VALUES ('Java', 9.0, 'Beginner')")
    c.execute("INSERT INTO example VALUES ('C++', 10.1, 'Advanced')")
    c.execute("INSERT INTO example VALUES ('JavaScript', 7.5, 'Intermediate')")
    c.execute("INSERT INTO example VALUES ('SQL', 5.0, 'Expert')")
    c.execute("INSERT INTO example VALUES ('Python', 2.0, 'Beginner')")
    c.execute("INSERT INTO example VALUES ('Python', 3.2, 'Expert')")
    c.execute("INSERT INTO example VALUES ('C#', 9.9, 'Expert')")
    c.execute("INSERT INTO example VALUES ('C#', 5.0, 'Beginner')")
    c.execute("INSERT INTO example VALUES ('Java', 9.9, 'Expert')")
    conn.commit()


def enter_dynamic_data():
    print("ENTER NEW DATABASE RECORD\n\r")
    lang = input("Which language?: ")
    ver = float(input("What version?: "))
    skill = input("What skill level?: ")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, ver, skill))
    conn.commit()

def read_from_database():
    print("RETREIVE DATABASE RECORDS\n\r")
    lang = input("Which language?: ")
    sql = "SELECT * FROM example WHERE Language = ?"
    for row in c.execute(sql, [(lang)]):
        print(row)

read_from_database()

conn.close()