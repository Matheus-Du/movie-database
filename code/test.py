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


def get_movie_info(movieName):
    # return info about a movie based on the user input of the movie title
    global connection, cursor

    query = "SELECT title, release_year, genre, country, description, avg_rating " \
            "FROM Movies WHERE title = '{}' COLLATE NOCASE; ".format(movieName)
    cursor.execute(query)
    connection.commit()
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Error: no movies with that title")
    else:
        for row in rows:
            print(row)

    return


def main():
    global connection, cursor

    path = './movies.db'
    connect(path)
    movieName = input("Enter the name of a movie: ")
    get_movie_info(movieName)

    return


if __name__ == '__main__':
    main()
