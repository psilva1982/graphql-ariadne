from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType
from bookstore.resolvers import author_resolver, category_resolver, book_resolver

type_defs = [
    load_schema_from_path("bookstore/schema.graphql"),
]

query = QueryType()
query.set_field("authors", author_resolver.author)
query.set_field("categories", category_resolver.category)
query.set_field("books", book_resolver.books)
query.set_field("book", book_resolver.book)


mutation = MutationType()
mutation.set_field("NewAuthor", author_resolver.new_author)
mutation.set_field("NewCategory", category_resolver.new_category)
mutation.set_field("NewBook", book_resolver.new_book)

schema = make_executable_schema(type_defs, query, mutation)