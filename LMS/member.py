from database import connect_to_db

def register_member(name, phone, email, address):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO Members (name, phone, email, address) VALUES (%s, %s, %s, %s)",
                   (name, phone, email, address))
    db.commit()
    db.close()

def view_available_books():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Books WHERE available > 0")
    books = cursor.fetchall()
    db.close()
    return books

def search_books_by_title(title):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Books WHERE title LIKE %s", ("%" + title + "%",))
    books = cursor.fetchall()
    db.close()
    return books

def view_issued_books(member_id):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute('''SELECT Books.title, Books.author, IssuedBooks.issue_date, IssuedBooks.return_date
                      FROM IssuedBooks
                      JOIN Books ON IssuedBooks.book_id = Books.book_id
                      WHERE IssuedBooks.member_id = %s''', (member_id,))
    issued_books = cursor.fetchall()
    db.close()
    return issued_books
