from bookstore.models import Category


def category(*_):
    return Category.objects.all()


def new_category(_, info, input):
    category = Category.objects.create(name=input["name"])
    return {"created": True, "category": category, "err": None}
