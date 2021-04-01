from tkinter import *
from tkinter import ttk

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import sqlite3

'''Program allows users to search for a movie title from a list of all movies on IMDb'''
global connection, cursor


def connect(path):
    # connect to the movies DB
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON; ')
    connection.commit()
    return


def test_connection():
    # test the connection of the DB
    query = "SELECT * FROM Movies LIMIT 5; "
    cursor.execute(query)
    connection.commit()
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return



def main():
    path = './movies.db'
    connect(path)
    test_connection()

    return


if __name__ == '__main__':
    main()
