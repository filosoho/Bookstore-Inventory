#============================== Libraries =======================================================
# Import the required libraries.
# For connecting to the SQLite database.
import sqlite3
# For formatting the books table
from tabulate import tabulate

#============================== Connect to the database =========================================
# Connect to the SQLite database.
with sqlite3.connect('ebookstore.db') as conn:
    cursor = conn.cursor()

    # Create the books table if it doesn't exist.
    conn.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
    ''')

    # Check if there is any data in the database.
    numb_rows = len(cursor.execute('''select * from books
    where id >= 3001 and id <= 3005''').fetchall())
    

    # If there is no data in the database, insert new data.
    if numb_rows == 0:
        # Populate the table with some sample data.
        conn.execute('''
        INSERT INTO books (id, title, author, qty)
        VALUES
            (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
            (3002, 'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 40),
            (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
            (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
            (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
        ''')

#======================================== Functions =======================================================


# Function to add a new book to the database.
def add_book():
    """
    Adds a book to the database.
    """
    with sqlite3.connect('ebookstore.db') as conn:
        # Get the book details from the user.
        title = input('Enter book title: ')
        author = input('Enter book author: ')
        while True:
            qty_str = input('Enter book quantity: ')
            try:
                qty = int(qty_str)
                break
            except ValueError:
                print('\nInvalid input. Please enter an integer.')
        
        # Insert the new book into the database.
        conn.execute('INSERT INTO books (title, author, qty) VALUES (?, ?, ?)', (title, author, qty))
        conn.commit()
        print('\nBook added to database.')


# Function to update an existing book in the database.
def update_book():
    """
    Updates a book in the database.
    """
    with sqlite3.connect('ebookstore.db') as conn:
        # Show all the books to the user.
        show_all_books()

        # Get the book ID to update from the user.
        check = False
        while check == False:
            book_id_str = input('Enter book ID: ')
            try:
                book_id = int(book_id_str)
                # Check if book ID exists in the database.
                cursor = conn.execute("SELECT id FROM books WHERE id = ?", (book_id,))
                if cursor.fetchone() is None:
                    print("\nBook ID does not exist.")
                else:
                    check = True
                    break
            except ValueError:
                print('\nInvalid input. Please enter an integer.')

        # Get the updated book details from the user.
        title = input('Enter new book title (or press enter to keep existing title): ')
        author = input('Enter new book author (or press enter to keep existing author): ')
        qty = input('Enter new book quantity (or press enter to keep existing quantity): ')

        # Build the SQL query based on user input.
        query = 'UPDATE books SET '
        updates = []

        # Check if title is provided and append it to updates.
        if title:
            updates.append(f"title = '{title}'")
        
        # Check if author is provided and append it to updates.
        if author:
            updates.append(f"author = '{author}'")

        # Check if qty is provided and append it to updates.
        if qty:
            while True:
                try:
                    qty_int = int(qty)
                    updates.append(f"qty = {qty_int}")
                    break
                except ValueError:
                    print('\nInvalid input. Please enter an integer.')
                    qty = input('Enter new book quantity (or press enter to keep existing quantity): ')

        # Check if any updates were provided.
        if not updates:
            print('\nNo updates provided.')
            return

        # Add updates to the query and execute it.
        query += ', '.join(updates)
        query += f' WHERE id = {book_id}'
        conn.execute(query)
        # Commit the changes.
        conn.commit()

        print(f'\nBook with ID {book_id} updated.')


# Function to delete an existing book in the database.
def delete_book():
    """
    Deletes a book from the database.
    """
    # Show all the books to the user.
    show_all_books()

    # Set check variable to False to start while loop.
    check = False
    while check == False:
        # Get book ID from the user.
        book_id_str = input('Enter book ID: ')

        try:
            # Convert book ID to integer.
            book_id = int(book_id_str)

            # Check if book ID exists in the database
            cursor = conn.execute("SELECT id FROM books WHERE id = ?", (book_id,))
            
            # If book ID does not exist in the database, print error message.
            if cursor.fetchone() is None:
                print("\nBook ID does not exist.")
            # If book ID exists in the database, set check to True and break out of the while loop.
            else:
                check = True
                break
        # If the input is not an integer, print error message.    
        except ValueError:
            print('\nInvalid input. Please enter an integer.')

    # Delete the book from the database.
    conn.execute(f'DELETE FROM books WHERE id = {book_id}')
    # Commit the changes
    conn.commit()

    print('\nBook deleted from database.')


# Function to search an existing book in the database.
def search_books():
    """
    Searches for a book in the database based on user input.
    """
    # Get search term from user.
    search_term = input('\nEnter search term: ').lower()

    # Search for books based on the search term.
    cursor = conn.execute(f'SELECT * FROM books WHERE lower(title) LIKE "%{search_term}%" OR lower(author) LIKE "%{search_term}%"')
    results = cursor.fetchall()

    # If no books are found, print error message.
    if len(results) == 0:
        print('\nNo results found.')
    # If books are found, print them out in a table.
    else:
        book_table = []
        for result in results:
            book_table.append([result[0], result[1], result[2], result[3]])
        print(f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ {len(results)} results found: ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
        print(tabulate(book_table, headers=["ID", "Title", "Author", "Quantity"]))
        print("\n----------------------------------------------------------------------------\n")


# Function to show all existing books in the database.
def show_all_books():
    """
    Shows all the books in the database.
    """
    # Get all books from the database.
    cursor = conn.execute("SELECT * FROM books")
    books = cursor.fetchall()

    # Print all books in a table.
    book_table = []
    for book in books:
        book_table.append([book[0], book[1], book[2], book[3]])
    print("\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ [ BOOKS ] ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
    print(tabulate(book_table, headers=["ID", "Title", "Author", "Quantity"]))
    print("\n----------------------------------------------------------------------------\n")


#============================================ Main Menu ======================================================
output = '''Select an option:

1. Enter book
2. Update book
3. Delete book
4. Search books
5. Show all books
0. Exit
'''

# Display the main menu and prompt the user for their choice.
while True:
    print("\n───────────────────  Welcome to the Bookstore Inventory!  ──────────────────────\n")
    choice = input(output)

    if choice == '0':
        #-------- Comment this out, if you want to keep the database with new inserted data -------

        # Removes new inserted data by the user from the database. 
        # Your changes to the data won't be saved.
        cursor.execute('DROP TABLE IF EXISTS books')
        #-------------------------------------------------------------------

        conn.commit()
        break
    elif choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '5':
        show_all_books()
    else:
        print('\nInvalid choice. Please try again.\n')

# Close the database connection.
conn.close()