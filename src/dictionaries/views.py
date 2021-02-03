from django.shortcuts import render
from dictionaries.models import Author

def home_page(request):
    author = Author.objects.first()
    context = {"author": author}
    return  render(request, template_name="home.html", context=context)
