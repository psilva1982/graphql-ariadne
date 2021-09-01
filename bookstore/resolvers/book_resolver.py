from django.db.models.query import QuerySet
from bookstore.models import Book, Category, Author
from django.core import serializers


def book(*_, id):
    book = Book.objects.get(pk=id)
    authors = book.authors.all()
    return {
        "id": book.id,
        "title": book.title,
        "category": book.category,
        "authors": authors,
    }


def books(*_, asc=True, order="title"):

    queryset = Book.objects.prefetch_related("authors")

    order = order if asc is True else "-" + order
    queryset = queryset.order_by(order)

    books = []
    for book in queryset:
        authors = [
            {"id": author.id, "name": author.name} for author in book.authors.all()
        ]
        books.append(
            {
                "id": book.id,
                "title": book.title,
                "category": book.category,
                "authors": authors,
            }
        )

    return books


def new_book(_, info, input):

    category = Category.objects.get(pk=input["category"])

    book = Book.objects.create(title=input["title"], category=category)

    for author_id in input["authors"]:

        try:
            author = Author.objects.get(pk=author_id)
            book.authors.add(author)

        except Author.DoesNotExist:
            pass

    return {"created": True, "book": book, "err": None}
