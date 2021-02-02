from django.shortcuts import render,HttpResponse
from movie.models import Movie
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    allmovies = Movie.objects.all()
    context = {'allmovies':allmovies}
    return render(request,'index.html',context)

def details(request,slug):
    movie = Movie.objects.filter(slug = slug).first()
    context1 = {'movie':movie}    
    return render(request,'movie.html',context1)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        last_name = request.POST['last_name']
        Password = request.POST['Password']
        email = request.POST['email']

    #create user
        myUser = User.objects.create_user(username,email,Password)
        myUser.first_name = name
        myUser.last_name = last_name
        myUser.save() 
        print("Accoutn created succefully!!")

    else:
        return HttpResponse('Not allowed')

           