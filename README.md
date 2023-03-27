# Bookstore-Inventory

This is a Python program that allows users to interact with a SQLite database for a fictional ebookstore. The database has a table called "books" that contains information about each book in the store, including its title, author, and quantity in stock.

# Libraries

<br>

This program requires the following libraries:

```
sqlite3 for connecting to the SQLite database
tabulate for formatting the books table
```

<br>

These libraries can be installed using pip:

```
pip install sqlite3
pip install tabulate
```

<br>

# Connecting to the database

The program connects to the SQLite database using the sqlite3.connect() function. If the database file does not exist, it will be created automatically. The program then creates the "books" table if it does not already exist.

# Functions

The program provides the following functions for interacting with the database:  

~~~  
add_book()  

This function allows the user to add a new book to the database.  
The user is prompted to enter the book's title, author, and quantity in stock.   
  
-------------------------------------------------------------------------------------------------------------    

update_book()  

This function allows the user to update an existing book in the database.  
The user is shown a list of all the books in the database and prompted to enter the ID of the book to update.     
The user can then update the book's title, author, and/or quantity in stock.   
  
-------------------------------------------------------------------------------------------------------------    

delete_book()  

This function allows the user to delete an existing book from the database.  
The user is shown a list of all the books in the database and prompted to enter the ID of the book to delete.  
  
-------------------------------------------------------------------------------------------------------------    
  
show_all_books()    

This function displays a formatted table of all the books in the database.    
~~~  
<br>

# Usage

<br>

To use this program, simply run the ebookstore.py script. This will start the interactive prompt. From there, you can enter commands to interact with the database.  

~~~
───────────────────  Welcome to the Bookstore Inventory!  ──────────────────────

Select an option:

1. Enter book
2. Update book
3. Delete book
4. Search books
5. Show all books
0. Exit
5

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ [ BOOKS ] ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

  ID  Title                                     Author             Quantity
----  ----------------------------------------  ---------------  ----------
3001  A Tale of Two Cities                      Charles Dickens          30
3002  Harry Potter and the Philosopher's Stone  J.K. Rowling             40
3003  The Lion, the Witch and the Wardrobe      C. S. Lewis              25
3004  The Lord of the Rings                     J.R.R Tolkien            37
3005  Alice in Wonderland                       Lewis Carroll            12

----------------------------------------------------------------------------


───────────────────  Welcome to the Bookstore Inventory!  ──────────────────────

Select an option:

1. Enter book
2. Update book
3. Delete book
4. Search books
5. Show all books
0. Exit
4

Enter search term: harry

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 1 results found: ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

  ID  Title                                     Author          Quantity
----  ----------------------------------------  ------------  ----------
3002  Harry Potter and the Philosopher's Stone  J.K. Rowling          40

----------------------------------------------------------------------------


───────────────────  Welcome to the Bookstore Inventory!  ──────────────────────

Select an option:

1. Enter book
2. Update book
3. Delete book
4. Search books
5. Show all books
0. Exit
2

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ [ BOOKS ] ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

  ID  Title                                     Author             Quantity
----  ----------------------------------------  ---------------  ----------
3001  A Tale of Two Cities                      Charles Dickens          30
3002  Harry Potter and the Philosopher's Stone  J.K. Rowling             40
3003  The Lion, the Witch and the Wardrobe      C. S. Lewis              25
3004  The Lord of the Rings                     J.R.R Tolkien            37
3005  Alice in Wonderland                       Lewis Carroll            12

----------------------------------------------------------------------------

Enter book ID: 3002
Enter new book title (or press enter to keep existing title):
Enter new book author (or press enter to keep existing author):
Enter new book quantity (or press enter to keep existing quantity): 35

Book with ID 3002 updated.

───────────────────  Welcome to the Bookstore Inventory!  ──────────────────────

Select an option:

1. Enter book
2. Update book
3. Delete book
4. Search books
5. Show all books
0. Exit
0
~~~  
  

<br>

![alt text](https://github.com/filosoho/Bookstore-Inventory/blob/6007983cdff0ea5382edfe232e08998b9736018f/Bookstore.png?raw=true)

![alt text](https://github.com/filosoho/Bookstore-Inventory/blob/6007983cdff0ea5382edfe232e08998b9736018f/Bookstore-1.png?raw=true)

<br>

# Contributing

If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License

Feel free to use and modify the code as per your requirements.
