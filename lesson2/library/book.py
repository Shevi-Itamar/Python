class Book:
    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author must not be empty.")
        self.title = title
        self.author = author
        self.is_checked_out = False