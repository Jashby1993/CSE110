

with open('books.txt') as books:
    for book in books:
        stripped_book = book.strip()
        print(stripped_book)
