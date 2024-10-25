import admin
import member

def admin_menu():
    print("\nAdmin Menu")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. View Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

def member_menu():
    print("\nMember Menu")
    print("1. Register")
    print("2. View Available Books")
    print("3. Search Book by Title")
    print("4. View Issued Books")
    print("5. Exit")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Admin")
        print("2. Member")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                admin_menu()
                admin_choice = input("Choose an option: ")
                if admin_choice == '1':
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    genre = input("Enter genre: ")
                    quantity = int(input("Enter quantity: "))
                    admin.add_book(title, author, genre, quantity)
                elif admin_choice == '2':
                    book_id = int(input("Enter book ID to remove: "))
                    admin.remove_book(book_id)
                elif admin_choice == '3':
                    books = admin.view_books()
                    for book in books:
                        print(book)
                elif admin_choice == '4':
                    book_id = int(input("Enter book ID: "))
                    member_id = int(input("Enter member ID: "))
                    issue_date = input("Enter issue date (YYYY-MM-DD): ")
                    admin.issue_book(book_id, member_id, issue_date)
                elif admin_choice == '5':
                    book_id = int(input("Enter book ID: "))
                    member_id = int(input("Enter member ID: "))
                    return_date = input("Enter return date (YYYY-MM-DD): ")
                    admin.return_book(book_id, member_id, return_date)
                elif admin_choice == '6':
                    break

        elif choice == '2':
            while True:
                member_menu()
                member_choice = input("Choose an option: ")
                if member_choice == '1':
                    name = input("Enter name: ")
                    phone = input("Enter phone: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    member.register_member(name, phone, email, address)
                elif member_choice == '2':
                    books = member.view_available_books()
                    for book in books:
                        print(book)
                elif member_choice == '3':
                    title = input("Enter book title to search: ")
                    books = member.search_books_by_title(title)
                    for book in books:
                        print(book)
                elif member_choice == '4':
                    member_id = int(input("Enter member ID: "))
                    issued_books = member.view_issued_books(member_id)
                    for book in issued_books:
                        print(book)
                elif member_choice == '5':
                    break

        elif choice == '3':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
