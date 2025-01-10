from django.shortcuts import render
from movieFormApp.forms import movieForm
from movieFormApp.models import Movie

# Create your views here.

def index(request):
    return render(request,'index.html')

def listMovies(request):
    movies = Movie.objects.all()
    return render(request,'listMovies.html',{'movies':movies})

def addMovie(request):
    movie = movieForm()
    if request.method == "POST":
        movie = movieForm(request.POST)
        if movie.is_valid():
            movie.save()
        else:
            print(movie.errors)
        return index(request)
    return render(request,'addMovie.html',{'movies':movie})

