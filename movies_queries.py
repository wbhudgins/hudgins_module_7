import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "RangerUp1515!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

db = None

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    # Query 1: Select all fields for the studio table
    print("-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    for row in cursor:
        print("Studio ID: {} \nStudio Name: {}\n".format(row[0], row[1]))

    # Query 2: Select all fields for the genre table
    print("-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    for row in cursor:
        print("Genre ID: {} \nGenre Name: {}\n".format(row[0], row[1]))

    # Query 3: Select the movie names for movies with a runtime less than two hours
    print("-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    for row in cursor:
        print("Film Name: {} \nRuntime: {}\n".format(row[0], row[1]))

    # Query 4: Get a list of film names and directors ordered by director
    print("-- DISPLAYING Director RECORDS in Order --")
    cursor.execute(
        "SELECT film_name, film_director FROM film ORDER BY film_director")
    for row in cursor:
        print("Film Name: {} \nDirector: {}\n".format(row[0], row[1]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)
finally:
    if db:
        db.close()
