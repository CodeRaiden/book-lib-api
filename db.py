# CREATING THE DATABASE AND TABLE FOR THE BOOK LIBRARY

# first we will import the sqlite3 module from the python standard library
import sqlite3

# creating a new sqlite database is as simple as creating the connection using a Sqlite3 module
# to establish a connection to the sqlite database we will pull the 'connect()' function from the sqlite3 module and then parse in a file path. and if the database represented by the file path does not exist in that path in the sqlserver, it will be created in that path
# We will save this sqlite connection in the variable "conn"

conn = sqlite3.connect("book.sqlite")
# if we run this file above the sqlite database file will be created in our project directory

# next we will need to create a cursor object for the database connection.
# a cursor object by pulling the "cursor" property  from the sqlite connection variable "conn"
# the cursor object is used to execute SQL statements on the sqlite database
# and then we will save this created cursor object in the variable "cursor"
cursor = conn.cursor()

# Next we need to define the sql query to create our database with the database objects/columns id, author, language, title and store it in a variable called "sql_query"
sql_query = """ CREATE TABLE book (
 id integer PRIMARY KEY,
 author text NOT NULL,
 language text NOT NULL,
 title text NOT NULL
)"""

# now we need to excute this query to create our database when the application is run
cursor.execute(sql_query)

# # # Now if we run the application again it will create our database table in the application folder


# # INTEGRATING THE ONLINE(REMOTE) MYSQL DATABASE INTO THE FLASK APPLICATION

# # import sqlite3
# # Here below instead of importing the sqlite3 module, we will import the pymysql module
# import pymysql


 
# # conn = sqlite3.connect("book.sqlite")
# # And here we will connect the pymysql instead of the sqlite3 and in the connect function parameters we will parse
# # in information for the connection in the form of variables and values for the "host as sql6.freesqldatabase.com",
# # "database as sql6635776", "user as sql6635776", "password as WVfzRIpkwH",
# # "charset as utf8mb4", and inorder to get the cursorclass result as a dictionary we will set the "cursorclass variable as pymysql.cursors.DictCursor" 
# conn = pymysql.connect(
#  host='sql6.freesqldatabase.com',
#  database='sql6635776',
#  user='sql6635776',
#  password='WVfzRIpkwH',
#  charset='utf8mb4',
#  cursorclass = pymysql.cursors.DictCursor
# )

# # The rest of the code will be similar only that at the end of the code we will close the mysql connection as seen in the last line of code.
# cursor = conn.cursor()

# sql_query = """ CREATE TABLE book (
#  id integer PRIMARY KEY,
#  author text NOT NULL,
#  language text NOT NULL,
#  title text NOT NULL
# )"""


# cursor.execute(sql_query)
# # closing the mysql connection
# conn.close()
# # when we run the db.py file it will create the book table in this database 
# # then we will go to the app.py file to link up the created pymysql database to our application.