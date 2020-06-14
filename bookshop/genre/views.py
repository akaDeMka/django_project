from django.shortcuts import render, get_object_or_404

from .models import Genre

# Create your views here.
def add (request):
    pass

def index(request):
    context = {'genre_list': Genre.objects.all()}
    return render(request,'index.html',context)

def edit(request,genre_id):
    genre = get_object_or_404 (Genre, pk=genre_id)
    return render(request,'edit.html',{'genre':genre})

def delete(request,genre_id):
    genre = get_object_or_404 (Genre, pk=genre_id)
    return render(request,'delete.html',{'genre':genre})