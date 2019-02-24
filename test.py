#!/usr/bin/env python
# coding=utf-8
import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)


users = [
    (1, 'tzago', 'asdf'),
    (2, 'barbosa', 'asdf'),
    (3, 'machado', 'asdf')
]

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users;"


for row in cursor.execute(select_query):
    print row

connection.commit()

connection.close()

