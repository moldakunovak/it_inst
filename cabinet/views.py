from django.shortcuts import render
from .models import Author


# Create your views here.
def get_cabinet(request):
    authors = Author.objects.all()
    q = authors.get(id=1)

    return render(request, 'cabinet.html', locals())


def detail_cabinet(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'detail_cabinet.html', locals())
