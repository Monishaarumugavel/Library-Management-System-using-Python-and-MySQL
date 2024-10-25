import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="library_management"
    )

def create_tables():
    db = connect_to_db()
    cursor = db.cursor()
    
    # Create the tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                        book_id INT AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR(100),
                        author VARCHAR(100),
                        genre VARCHAR(50),
                        quantity INT,
                        available INT);''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Members (
                        member_id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100),
                        phone VARCHAR(15),
                        email VARCHAR(100),
                        address VARCHAR(255));''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS IssuedBooks (
                        issue_id INT AUTO_INCREMENT PRIMARY KEY,
                        book_id INT,
                        member_id INT,
                        issue_date DATE,
                        return_date DATE,
                        FOREIGN KEY (book_id) REFERENCES Books(book_id),
                        FOREIGN KEY (member_id) REFERENCES Members(member_id));''')

    db.commit()
    db.close()
