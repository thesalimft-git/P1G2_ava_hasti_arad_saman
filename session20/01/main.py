# sql ::::> structural query language (crud: 4 main command)
# sql ::::> **sqlite**, access, mysql, postgress, oracle

# open, cursor, command, commit, close
# create a database for a e-commerce system
# tabels: user, product, orders

import sqlite3
con = sqlite3.connect("session20/01/data.db")
cur = con.cursor()
# command = "CREATE TABLE IF NOT EXISTS user(id, name, username, password)"
# command = "CREATE TABLE IF NOT EXISTS product(id, name, price, stock)"
# command = "CREATE TABLE IF NOT EXISTS orderbook(id, user_id, product_id, amount)"
# cur.execute(command)


# add data
# command = """
#     INSERT INTO user VALUES
#         ('1', 'ali', 'aliakbari', '123'),
#         ('2', 'reza', 'rezaasadi', '345'),
#         ('3', 'sara', 'saramohammadi', '678')
# """


# read data
# command = """
#     SELECT * FROM user
# """
# command = """
#     SELECT * FROM user WHERE id = '3'
# """
# command = """
#     SELECT username FROM user WHERE id = '3'
# """
# res = cur.execute(command)
# print(res.fetchall())




# update
command = "DELETE FROM user WHERE id = '1'"
res = cur.execute(command)
con.commit()









