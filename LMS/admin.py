from database import connect_to_db

def add_book(title, author, genre, quantity):
    db = connect_to_db()
    cursor = db.cursor()
    available = quantity
    cursor.execute("INSERT INTO Books (title, author, genre, quantity, available) VALUES (%s, %s, %s, %s, %s)",
                   (title, author, genre, quantity, available))
    db.commit()
    db.close()

def remove_book(book_id):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Books WHERE book_id = %s", (book_id,))
    db.commit()
    db.close()

def view_books():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    db.close()
    return books

def issue_book(book_id, member_id, issue_date):
    db = connect_to_db()
    cursor = db.cursor()

    # Decrement the available quantity
    cursor.execute("SELECT available FROM Books WHERE book_id = %s", (book_id,))
    available = cursor.fetchone()[0]

    if available > 0:
        cursor.execute("INSERT INTO IssuedBooks (book_id, member_id, issue_date) VALUES (%s, %s, %s)",
                       (book_id, member_id, issue_date))
        cursor.execute("UPDATE Books SET available = available - 1 WHERE book_id = %s", (book_id,))
        db.commit()
        print("Book issued successfully.")
    else:
        print("Book is currently not available.")
    
    db.close()

def return_book(book_id, member_id, return_date):
    db = connect_to_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM IssuedBooks WHERE book_id = %s AND member_id = %s", (book_id, member_id))
    cursor.execute("UPDATE Books SET available = available + 1 WHERE book_id = %s", (book_id,))
    
    db.commit()
    db.close()
