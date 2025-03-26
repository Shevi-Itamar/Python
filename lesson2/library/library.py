from book import Book


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.checked_out_books = {}

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("The argument must be an instance of the Book class.")
        self.books.append(book)

    def add_user(self, username):
        if not username:
            raise ValueError("Username must not be empty.")
        self.users.append(username)

    def check_out_book(self, username, book):
        if username not in self.users:
            raise ValueError(f"User '{username}' is not registered.")
        if not isinstance(book, Book):
            raise TypeError("The argument must be an instance of the Book class.")
        if book not in self.books:
            raise ValueError(f"Book '{book.title}' by {book.author} is not in the library.")
        if book.is_checked_out:
            raise ValueError(f"Book '{book.title}' by {book.author} is already checked out.")

        self.checked_out_books[username] = book
        book.is_checked_out = True

    def return_book(self, username, book):
        if username not in self.users:
            raise ValueError(f"User '{username}' is not registered.")
        if not isinstance(book, Book):
            raise TypeError("The argument must be an instance of the Book class.")
        if book not in self.books:
            raise ValueError(f"Book '{book.title}' by {book.author} is not in the library.")
        if book not in self.checked_out_books or self.checked_out_books[username] != book:
            raise ValueError(f"Book '{book.title}' by {book.author} was not checked out by '{username}'.")

        self.checked_out_books.pop(username)
        book.is_checked_out = False

    def search_books(self, search_term):
        if not search_term:
            raise ValueError("Search term must not be empty.")
        return [book for book in self.books if search_term.lower() in book.title.lower()]