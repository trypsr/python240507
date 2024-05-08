import sqlite3

con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.execute("create table PhoneBook (Name text, PhoneNum text);")

cur.execute("insert into PhoneBook values ('전우치', '010-2977-4444')")
name = "홍길동"
phoneNubmer = "010-2977-4433"
cur.execute("insert into PhoneBook values (?, ?)", (name, phoneNubmer))

datalist = (("이순신", "010-2977-1111"), ("박문수", "010-2977-2222"))
cur.executemany("insert into PhoneBook values (?, ?)", datalist)




cur.execute("select * from PhoneBook;")
for row in cur:
    print(row[0], row[1])