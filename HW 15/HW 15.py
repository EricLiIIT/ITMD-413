'''
Author: Eric Li
ITMD 413 HW 15

This program creates a database for this program to connect to and do CRUD operations on.
'''
import sqlite3
import pandas as pd

#Part II
connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10
print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))

print(pd.read_sql('SELECT * FROM titles', connection))

print(pd.read_sql('SELECT * FROM author_ISBN', connection).head())

print(pd.read_sql('SELECT first, last FROM authors', connection))

print(pd.read_sql("""SELECT title, edition, copyright
               FROM titles
               WHERE copyright > '2016'""", connection))

print(pd.read_sql("""SELECT id, first, last
               FROM authors
               WHERE last LIKE 'D%'""", connection, index_col=['id']))

print(pd.read_sql("""SELECT id, first, last
               FROM authors
               WHERE first LIKE '_b%'""", connection, index_col=['id']))

print(pd.read_sql("""SELECT title
               FROM titles
               ORDER By title ASC""", connection))

print(pd.read_sql("""SELECT id, first, last
               FROM authors
               ORDER By last, first""",
               connection, index_col=['id']))

print(pd.read_sql("""SELECT id, first, last
               FROM authors
               ORDER By last DESC, first ASC""",
               connection, index_col=['id']))

print(pd.read_sql("""SELECT isbn, title, edition, copyright
               FROM titles
               WHERE title LIKE '%How to Program'
               ORDER BY title""", connection))

print(pd.read_sql("""SELECT first, last, isbn
               FROM authors
               INNER JOIN author_ISBN
                ON authors.id = author_ISBN.id
               ORDER BY last, first""", connection).head())

# Cursor object allows for updating the database
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                        VALUES ('Sue', 'Red')""")

print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

cursor = cursor.execute("""UPDATE authors SET last='Black'
                        WHERE last='Red' AND first='Sue'""")

print(cursor.rowcount)

print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

cursor = cursor.execute('DELETE FROM authors WHERE id=6')
print(cursor.rowcount)

print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
print(pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3))
print(pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection))
print(pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE
                  '%How to Program' ORDER BY title""", connection))

# Part III
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection)) # a
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)) # b
print(pd.read_sql("""SELECT t.title, t.copyright, t.isbn FROM titles t
                    INNER JOIN  author_ISBN a
                    ON t.isbn = a.isbn
                    WHERE a.id = 1""", connection)) # c

cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('John', 'Doe')""") # d
print(pd.read_sql("""SELECT first, last, id FROM authors WHERE first = 'John' AND last = 'Doe'""", connection))

cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                        VALUES (101010101010, 'Part E', 1, '2021')""")
cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES (7, 101010101010)""") # e

print(pd.read_sql("""SELECT title FROM titles where title = 'Part E'""", connection))
print(pd.read_sql("""SELECT id, isbn FROM author_ISBN WHERE  id = 7""", connection))