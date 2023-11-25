class EBookReader:
    def __init__(self):
        self.purchased_books = []

    def buy_book(self, book):
        self.purchased_books.append(book)
        print(f"Congratulations! You have purchased {book.title}.")

    def view_purchased_books(self):
        if len(self.purchased_books) == 0:
            print("You haven't purchased any books yet.")
        else:
            print("Your purchased books:")
            for book in self.purchased_books:
                print(f"- {book.title}")

    def read_book(self, book):
        if book in self.purchased_books:
            print(f"Reading {book.title}...")

        else:
            print(f"You haven't purchased {book.title}. Please buy it first.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Usage
ebook_reader = EBookReader()

# Buy new books
book1 = Book("Pride and Prejudice", "Jane Austen")
ebook_reader.buy_book(book1)

book2 = Book("To Kill a Mockingbird", "Harper Lee")
ebook_reader.buy_book(book2)

book3 = Book("1984", "George Orwell")
ebook_reader.buy_book(book3)

# View purchased books
ebook_reader.view_purchased_books()

# Read a purchased book
ebook_reader.read_book(book2)