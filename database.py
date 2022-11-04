import sqlite3

def userDb():
    conn = sqlite3.connect('dashboard.sqlite')
    return conn

def sourceDb():
    conn = sqlite3.connect('path/active_counts.sqlite')
    return conn
