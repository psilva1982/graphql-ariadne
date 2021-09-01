from bookstore.models import Author

def author(*_):
    return Author.objects.all()
   

def new_author(_,info, input):
    author = Author.objects.create(name=input['name'])      
    return {'created': True, 'author': author, 'err': None}