# from flask import Flask, request, jsonify
# import json
# import sqlite3

# app = Flask(__name__)

# # Now that we have created our remote database server, we no longer need the in house database object
# # books_list = [
# #  {
# #   "id": 0,
# #   "author": "Chinua Achebe",
# #   "language": "English",
# #   "title": "Things fall apart",
# #   },
# #  {
# #   "id": 1,
# #   "author": "Hans Christian Andersen",
# #   "language": "Danish",
# #   "title": "Fairy Tales",
# #   },
# #   {
# #   "id": 2,
# #   "author": "Samuel Beckett",
# #   "language": "Danish",
# #   "title": "Molloy, Malone Dies, The Unnamable, The Triology", 
# #   },
# #  {
# #   "id": 3,
# #   "author": "Giovanni Boccacio",
# #   "language": "Italian",
# #   "title": "The Decameron",
# #   },
# #  {
# #   "id": 6,
# #   "author": "Jorge Luis Borges",
# #   "language": "Spanish",
# #   "title": "Ficciones",
# #   },
# #  {
# #   "id": 5,
# #   "author": "Emily Bront",
# #   "language": "English",
# #   "title": "Wuthering Heights",
# #   },
# # ]


# # So now in order for us not to keep manually creating a connection to the created sqlite3 database remote server here in the app.py file each time we want to query the sqlite database server for a request, we will create a function here called "db_connection" which we can call each time we need to query the database. to do this we will first need to import sqlite3 into the application
# def db_connection():
#   try:
#     # we will create a variable to hold the code for creating a connection to the database as we did when creating the database in the db.py file. Then we will use a try/except for the connection to catch any possible error that may occur
#     conn = sqlite3.connect("book.sqlite")
#   # for any error that occurs when the function is called we want it printed in the inbuilt standard sqlite3 error format
#   except sqlite3.Error as e:
#     print(e)
#   # then we will return the established connect if there are no errors found
#   return conn


# # Here  we will write a route to the books_list database, with the help of the imported request, we will also add methods for Getting the contents of the book_list and Posting a new content in the book_list 
# @app.route('/books', methods=('GET', 'POST'))
# def books():
#  # HANDLING THE GET REQUEST
#  # the first thing we will do is to establish the connection by simply calling the created db_connection function
#  conn = db_connection()
#  # next we create the cursor for writing sql queries to the database
#  cursor = conn.cursor()
#  # so here we will handle the GET request method
#  if request.method == 'GET':
#   # then we will write a query to get the database table data from the database
#   cursor.execute("SELECT * FROM book")
#   # then we will create a variable to hold the data gotten from the book database table in an dictionary to be returned 
#   books = [
#     dict(id=row[0], author=row[1], language=row[2], title=row[3])
#     for row in cursor.fetchall()
#     ]

#   if books is not None:
#    # And if the object is not, then we want to return all the contents of the book_list in a json string to the user with the help of jsonify
#    return jsonify(books)
#    # else if the list is empty, then we will return a '404' not found status code as seen below
#   else:
#    'Nothing Found', 404
  

#  # # HANDLING THE POST REQUEST
#  # # here we will handle the entry of a new book data into the book_list database by the user/client
#  # if request.method == 'POST':
#  #  # the first thing we would like to do here is to collect information from the client for the new entry and hold it in a variable(using the request property ".form") to be used to set up the items(key and value pairs) object for the new entry to be posted/pushed to the book_list database
#  #  new_author = request.form('author')
#  #  new_lan = request.form('language')
#  #  new_title = request.form('title')
#  #  # for the id we will set this to be added automatically.
#  #  # to do this we will get the id of the last book in the books_list and increment it by 1
#  #  new_id = books_list[-1][id]+1

#  #  # then we will use the gotten information entered by the client which is held in the form variables to fill in the new book object entry
#  #  book = {
#  #   "id": new_id,
#  #   "author": new_author,
#  #   "language": new_lan,
#  #   "title": new_title,
#  #  }

# # or
 
# # # HANDLING THE POST REQUEST
#  # # here we will handle the entry of a new book data into the database server by the user/client
#  if request.method == 'POST':
#  # the first thing we would like to do here is to collect information from the client for the new entry and hold it in a variable(using the request property ".form") to be used to set up the items(key and value pairs) object for the new entry to be posted/pushed to the book_list database. which is same as before but only that this time we will not need to handle the id as this will be done automatically for us as hardcoded in the creation of the book database server
#   new_author = request.form['author']
#   new_lan = request.form['language']
#   new_title = request.form['title']
#   # then to input the gotten information into the database we will create a variable called "sql" to hold the database query for inputting information into each row of the database table
#   sql = """INSERT INTO book (author, language, title)
#            VALUES (?, ?, ?)"""
#   # the question marks will help us add values latter in a dynamic way. the question marks are actaually place holders in what is known as parameterized query

#   # then here we will execute the query by writing it to the database by making use of the cursor in which we will include the sql query variable "sql" in the parameter and in a second parameter we will include the values for the parameterized query in the form of a tuple as done below
#   cursor.execute(sql, (new_author, new_lan, new_title))

#   # to save the changes we will need to call the commit method of our database connection "conn"
#   conn.commit()
#   # And finally we will display the posted object's id (the new entry) in a string by using the cursor to print out the lastrow object's id of the book table as done below
#   return f"Book with id: {cursor.lastrowid} created successfully",201



# # we will add another route for getting a book item/object by it's id inorder to perform CRUD operations on it
# @app.route('/book/<int:id>', methods=('GET', 'PUT', 'DELETE'))
# def single_book(id):
#  # first we will create the connection and cursor variables
#  conn = db_connection()
#  cursor = conn.cursor()
#  # we will create the book variable and set it's value to none for now so it can be used any where within the view function depending on the method defined
#  book = None
 
#  # handling the get method to retrieve the book by id
#  if request.method == 'GET':
#   sql = """SELECT * FROM book WHERE id=?"""
#   cursor.execute(sql, (id,))
#   # then we grab the returned rows with the fetchall() method
#   rows = cursor.fetchall()
#   # then we will iterrate through the returned number of row which is one obviously and store the result in the "book" variable we created at the beginning
#   for row in rows:
#    book = row
#   if book is not None:
#    return jsonify(book), 201
#   # if no book with matching id is found, we can input pass as done below which would make sure that nothing happens
#   else:
#    return 'Something went wrong', 404

# #  or we could use an else statement to return a 404 sttus code message
# #  else:
# #   "No Book With Matching Id Found", 404
 
# #  Not correct code
# #  # Handling the put method to update a book by it's id
# #  if request.method == 'PUT':
# #   # then we create the user input
# #   new_author = request.form['author']
# #   new_lan = request.form['language']
# #   new_title = request.form['title']

# #   # we will store the sql command for updating an object in the book database
# #   sql = """UPDATE book 
# #           SET author=?,
# #            language=?,
# #            title=?
# #           WHERE id=?"""

# #   # then we query the database to update the table object with the specified id
# #   cursor.execute(sql, (new_author, new_lan, new_title, id))
# #   # then we commit the changes
# #   conn.commit()
  
# #   # then we return an object of the update book to the client with either codes below
# #   # book['author'] = new_author
# #   # book['language'] = new_lan
# #   # book['title'] = new_title
# #   # book['id'] = id
# #   # return jsonify(book),201
# #   # or

# #   book = {
# #     "id": id,
# #     "author": new_author,
# #     "language": new_lan,
# #     "title": new_title
# #   }
# #   return jsonify(book),201

#   # or

#  # if request.method == 'PUT':
#  #  for book in books_list:
#  #   if book['id'] == id:
#  #    book['author'] = request.form['author']
#  #    book['language'] = request.form['language']
#  #    book['title'] = request.form['title']

#  #    updated_book = {
#  #     'id': id,
#  #     'author': book['author'],
#  #     'language': book['language'],
#  #     'title': book['title'],
#  #    }
#  #    return jsonify(updated_book)
#  # pass

# #  correct code
#  # Handling the put method to update a book by it's id
#  if request.method == 'PUT':
#   # we will store the sql command for updating an object in the book database
#   sql = """UPDATE book 
#           SET author=?,
#            language=?,
#            title=?
#           WHERE id=?"""

#   # then we create the user input
#   new_author = request.form['author']
#   new_lan = request.form['language']
#   new_title = request.form['title']
  
#   # then we return an object of the update book to the client with either codes below
#   # book['author'] = new_author
#   # book['language'] = new_lan
#   # book['title'] = new_title
#   # book['id'] = id
#   # return jsonify(book),201
#   # or

#   updated_book = {
#     "id": id,
#     "author": new_author,
#     "language": new_lan,
#     "title": new_title
#   }

#   # then we query the database to update the table object with the specified id
#   cursor.execute(sql, (new_author, new_lan, new_title, id))
#   # then we commit the changes
#   conn.commit()
#   return jsonify(updated_book),201


#  # Handling the delete method to delete a book by it's id
#  if request.method == 'DELETE':
#   # to delete a book we will store the sql query to delete an object in the database.
#   sql = """DELETE FROM book WHERE id=?"""
#   # then we execute the sql query
#   cursor.execute(sql, (id,))
#   conn.commit()
#   return f"Book with id: {id} was deleted successfully", 200


# if __name__ == '__main__':
#  app.run()






# LINKING THE PYMYSQL DATABASE TO OUR APPLICATION
from flask import Flask, request, jsonify
import json
# here we will import the pymysql instaed of the sqlite3 statement
import pymysql

app = Flask(__name__)

def db_connection():
  try:
    # we will replace the sqlite3 connetion with the pymysql connection along with it's specified credentials in the parenthesis() for making the connection to the remote database
    conn = pymysql.connect(
      host='sql6.freesqldatabase.com',
      database='sql6635776',
      user='sql6635776',
      password='WVfzRIpkwH',
      charset='utf8mb4',
      cursorclass = pymysql.cursors.DictCursor
    )
  # we will also replace the sqlite3 except statement with the pymysql except statement
  except pymysql.Error as e:
    print(e)
  return conn

# Now here for the rest of the code we need some minor changes to get it to work with the pymysql database
@app.route('/books', methods=('GET', 'POST'))
def books():
 conn = db_connection()
 cursor = conn.cursor()
 if request.method == 'GET':
  cursor.execute("SELECT * FROM book") 
  # firstly here in the fetch all query of the pymysql database, we will replace the column integers with the expected dictionary key variable that holds the expected values. this is because the pymysql returns a list of dictionaries
  # books = [
  #   dict(id=row[0], author=row[1], language=row[2], title=row[3])
  #   for row in cursor.fetchall()
  #   ]
  books = [
    dict(id=row['id'], author=row['author'], language=row['language'], title=row['title'])
    for row in cursor.fetchall()
    ]

  if books is not None:
   return jsonify(books)
  else:
   'Nothing Found', 404
 
 if request.method == 'POST':
  new_author = request.form['author']
  new_lan = request.form['language']
  new_title = request.form['title']
  # the next change we will make is here as the pymysql will return a type error for the string conversion question marks(?) used to parse in our VALUES. So instead we will replace them with the "%s" which stands for string input
  # sql = """INSERT INTO book (author, language, title)
  #          VALUES (?, ?, ?)"""
  sql = """INSERT INTO book (author, language, title)
           VALUES (%s, %s, %s)"""

  cursor.execute(sql, (new_author, new_lan, new_title))

  conn.commit()
  return f"Book with id: {cursor.lastrowid} created successfully",201


@app.route('/book/<int:id>', methods=('GET', 'PUT', 'DELETE'))
def single_book(id):
 conn = db_connection()
 cursor = conn.cursor()
 book = None
 
 if request.method == 'GET':
  sql = """SELECT * FROM book WHERE id=?"""
  cursor.execute(sql, (id,))
  rows = cursor.fetchall()

  for row in rows:
   book = row
  if book is not None:
   return jsonify(book), 201
  else:
   return 'Something went wrong', 404

 if request.method == 'PUT':
  sql = """UPDATE book 
          SET author=?,
           language=?,
           title=?
          WHERE id=?"""

  new_author = request.form['author']
  new_lan = request.form['language']
  new_title = request.form['title']


  updated_book = {
    "id": id,
    "author": new_author,
    "language": new_lan,
    "title": new_title
  }

  cursor.execute(sql, (new_author, new_lan, new_title, id))
  conn.commit()
  return jsonify(updated_book),201


 if request.method == 'DELETE':
  sql = """DELETE FROM book WHERE id=?"""
  cursor.execute(sql, (id,))
  conn.commit()
  return f"Book with id: {id} was deleted successfully", 200


if __name__ == '__main__':
 app.run()