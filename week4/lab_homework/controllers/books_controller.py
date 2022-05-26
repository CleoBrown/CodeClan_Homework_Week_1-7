from flask import Flask, render_template
from repositories import authors_repository, books_repository
from models.author import Author
from models.book import Book


from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@books_blueprint.route("/books")
def books():
    books = books_repository.select_all()  
    return render_template("books/index.html", books=books)