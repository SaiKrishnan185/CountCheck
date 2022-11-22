import sqlite3

def userDb():
    conn = sqlite3.connect('db1.sqlite')
    return conn

def sourceDb():
    conn = sqlite3.connect('db2.sqlite')
    return conn
