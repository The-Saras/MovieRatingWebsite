from django.shortcuts import render,HttpResponse
from movie.models import Movie

# Create your views here.
def home(request):
    allmovies = Movie.objects.all()
    context = {'allmovies':allmovies}
    return render(request,'index.html',context)

def details(request,slug):
    movie = Movie.objects.filter(slug = slug).first()
    context1 = {'movie':movie}
    
    return render(request,'movie.html',context1)

