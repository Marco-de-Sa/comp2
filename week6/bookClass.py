class Book:
    def __init__(self, title, author, pages, release_date, position = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.release_date = release_date
        self.position = position

    def print_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages} Release date: {self.release_date}, Current page: {self.position}"

    def read(self, page_nr):
        print(f"you have read {page_nr} pages out of {self.pages}")
        self.position = int(page_nr)

book1 = Book(input("what is the title of the book: "), input("author's name: "), int(input("how many pages: ")), input("what was the release date of the book in dd/mm/yyyy format: "))
book2 = Book(input("what is the title of the book: "), input("author's name: "), int(input("how many pages: ")), input("what was the release date of the book in dd/mm/yyyy format: "))
book3 = Book(input("what is the title of the book: "), input("author's name: "), int(input("how many pages: ")), input("what was the release date of the book in dd/mm/yyyy format: "))

print(book1.print_summary())
print(book2.print_summary())
print(book3.print_summary())

while book1.position < book1.pages:
    book1.read(int(input(f"what page are you on for {book1.title}: ")))
while book2.position < book2.pages:
    book2.read(int(input(f"what page are you on for {book2.title}: ")))
while book3.position < book3.pages:
    book3.read(int(input(f"what page are you on for {book3.title}: ")))

print(book1.print_summary())
print(book2.print_summary())
print(book3.print_summary())