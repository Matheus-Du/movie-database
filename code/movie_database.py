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


def get_movie_by_actor(actorName):
    # return info about a movie based on the name of an actor
    global connection, cursor
    '''
    query = "SELECT title, release_year, genre, release_country, actors, description, avg_score" \
            "FROM Movies WHERE actors LIKE '%{}%' COLLATE NOCASE;".format(actorName)'''
    query = "SELECT title, release_year, genre, actors, description, avg_score " \
            "FROM Movies WHERE actors LIKE '%{}%' COLLATE NOCASE".format(actorName)
    cursor.execute(query)
    connection.commit()
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("ERROR: no movie exists with that name or actor")
    else:
        for row in rows:
            print("Title: {} \nRelease year: {} \nGenre: {} \nActors: {} \nDescription: {} \nAverage score: {}\n"
                  .format(row[0], row[1], row[2], row[3], row[4], row[5]))

    return


def get_movie_info(movieName):
    # return info about a movie based on the user input of the movie title
    global connection, cursor

    query = "SELECT title, release_year, genre, release_country, description, avg_score " \
            "FROM Movies WHERE title LIKE '%{}%' COLLATE NOCASE; ".format(movieName)
    cursor.execute(query)
    connection.commit()
    rows = cursor.fetchall()

    if len(rows) == 0:
        # if no results for movie title, search by actor names
        get_movie_by_actor(movieName)
    else:
        for row in rows:
            print("\nTitle: {} \nRelease Year: {} \nGenre: {} \nCountry of Release: {} "
                  "\nDescription: {} \nAverage Rating: {}"
                  .format(row[0], row[1], row[2], row[3], row[4], row[5]))

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
