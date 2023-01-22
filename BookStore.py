import sqlite3

db = sqlite3.connect('Task 39 - Capstone Project V/ebookstore_db')

cursor = db.cursor()

#Create a table for ebookstore
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ebookstore(
        id INTEGER PRIMARY KEY, 
        title TEXT,
        author TEXT,
        qty INTEGER)
    ''')
db.commit()

# Create list of books
books = [(3001, "A Tale of Two Cities", "Charles Dickens", 30), (3002, "Harry Potter and the Philosopher's Stone", "J.K.Rowling", 40), (3003, "The Lion, the witch and the wardrobe", "C.S.Lewis", 25),
         (3004, "The Lord of the Rings", "J.R.R Tolkien", 37), (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

#Enter books into database
cursor.executemany('''INSERT INTO ebookstore(id, title, author, qty) VALUES(?,?,?,?)''', books)

db.commit()

#function to add book to database
def addBook(id, title, author, qty):
    cursor.execute('''INSERT INTO ebookstore (id, title, author, qty) VALUES(?,?,?,?)''', (id, title, author, qty))
    db.commit()
    print("Book added")

#function to update book
def updateBook(title, qty):
    cursor.execute('''UPDATE ebookstore SET qty = ? WHERE title = ?''', (qty, title))
    db.commit()
    print("Book Updated")

#function to delete book
def deleteBook(title):
    cursor.execute('''DELETE FROM ebookstore WHERE title = ?''', [title])
    db.commit()
    print("Book Deleted")

#function to search for book
def searchBook(title):
    cursor.execute("SELECT * FROM ebookstore WHERE title = ?)", [title])
    for row in cursor:
        print(row)

### Main Menu ###
# Retrieve menu input from user
while True:
    menu = (input('''Please select from the following:
             Press 1 to Enter Book
             Press 2 to Update Book
             Press 3 to Delete Book
             Press 4 to Search Book
             Press 0 to exit
    '''))
    
    if menu == "1": #Enter a new book
        book_id = int(input("Please enter the book id "))
        book_title = input("Please enter the Title of the book ")
        book_author = input("Please enter the Author of the book ")
        book_quantity = int(input("Please enter the quantity of books "))
        book = addBook(book_id, book_title, book_author, book_quantity)
    
    elif menu == "2": #Update a book
        book_title = input("Please enter the Title of the book you wish to update ")
        book_quantity = int(input("Please enter the updated number of books "))
        book = updateBook(book_title, book_quantity)
    
    elif menu == "3": #Delete a book
        book_title = input("Please enter the book title you wish to delete ")
        book = deleteBook(book_title)
    
    elif menu == "4": #Seach for a book
        book_title = input("Please enter the book to search for ")
        book = searchBook(book_title)
    
    elif menu == "5":
        cursor.execute('''SELECT * FROM ebookstore;''')
        all = cursor.fetchall()
        for row in all:
            print(row)
    
    elif menu == "0": #Exit Program
        print("Goodbye")
        db.close()
        exit()
    
    else:
        print("You have entered a wrong choice. Please try again!")
        db.close()
    
    