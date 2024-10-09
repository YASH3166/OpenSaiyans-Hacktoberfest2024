class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books
        self.issued_books = {}

    def display_books(self):
        if not self.available_books:
            print("\nNo books available right now.")
        else:
            print("\nAvailable books:")
            for book in self.available_books:
                print(f"- {book}")

    def add_book(self, book_name):
        self.available_books.append(book_name)
        print(f"\n'{book_name}' has been added to the library.")

    def issue_book(self, book_name, user):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.issued_books[book_name] = user
            print(f"\n'{book_name}' has been issued to {user}.")
        elif book_name in self.issued_books:
            print(f"\n'{book_name}' is already issued to {self.issued_books[book_name]}.")
        else:
            print(f"\nSorry, '{book_name}' is not available in the library.")

    def return_book(self, book_name):
        if book_name in self.issued_books:
            user = self.issued_books.pop(book_name)
            self.available_books.append(book_name)
            print(f"\n'{book_name}' has been returned by {user}.")
        else:
            print(f"\n'{book_name}' was not issued or does not belong to the library.")

    def view_issued_books(self):
        if not self.issued_books:
            print("\nNo books have been issued.")
        else:
            print("\nIssued books:")
            for book, user in self.issued_books.items():
                print(f"- '{book}' issued to {user}")


def library_menu():
    library = Library(["The Catcher in the Rye", "To Kill a Mockingbird", "1984", "Pride and Prejudice"])
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Display available books")
        print("2. Add a new book")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. View issued books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_name = input("Enter the name of the book to add: ").strip()
            library.add_book(book_name)
        elif choice == "3":
            book_name = input("Enter the name of the book to issue: ").strip()
            user = input("Enter the name of the user: ").strip()
            library.issue_book(book_name, user)
        elif choice == "4":
            book_name = input("Enter the name of the book to return: ").strip()
            library.return_book(book_name)
        elif choice == "5":
            library.view_issued_books()
        elif choice == "6":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    library_menu()
