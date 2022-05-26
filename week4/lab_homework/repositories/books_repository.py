from db.run_sql import run_sql
from models.book import Book
from repositories import authors_repository


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = authors_repository.select(row['author_id'])
        book = Book(row['title'], row['author'] )
        books.append(book)
    return books

def save(book):
    sql = "INSERT INTO books (title, author) VALUES (?, ?) RETURNING *"
    values = [book.title, book.author]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)