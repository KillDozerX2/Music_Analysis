from django.shortcuts import render,get_object_or_404 , redirect
from .models import Song , Genre, Artist, Request
from  django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from forms import Request_form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    song_argument = (Song.objects.latest('id').id) - 3
    artist_argument = (Artist.objects.latest('id').id) - 3
    genre_argument = (Genre.objects.latest('id').id) - 3
    Songs = Song.objects.filter(id__gte=song_argument)
    Genres = Genre.objects.filter(id__gte=genre_argument)
    Artists = Artist.objects.filter(id__gte=artist_argument)
    rqst = request.GET.get('query')
    context = {}
    if rqst:
        form = Request_form(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect("/")
        context.update({"form":form,})
        Songs = Song.objects.filter(Title__icontains=rqst)
        Genres = Genre.objects.filter(Name__icontains=rqst)
        Artists = Artist.objects.filter(ArtistName__icontains=rqst)
    context.update({
        "check" : rqst,
        "songs" : Songs,
        "genres":Genres,
        "Artist":Artists,
    })
    return render(request, 'index.html',context)

def Detail(request , arg ,id):
    if arg == 'a':
        artist = get_object_or_404(Artist, id=id)
        print arg
        context = {
            "artist": artist,
            "chck": arg,
            "chck2": len(arg),
        }
        return render(request, 'Details.html', context)
    elif arg == 'g':
        genre = get_object_or_404(Genre, id=id)
        context = {
            "genre": genre,
            "chck": arg,

            "chck2": len(arg),
        }
        return render(request, 'Details.html', context)
    elif arg == 's':
        song = get_object_or_404(Song, id=id)
        context = {
            "song" : song,
            "chck" : arg,

            "chck2": len(arg),
        }
        return render(request , 'Details.html' , context)
    elif arg == 'ss':
        song_list = Song.objects.all()
        paginator = Paginator(song_list, 3)  # Show 25 contacts per page
        page = request.GET.get('page')


        page = request.GET.get('page')
        try:
            song_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            song_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            song_list = paginator.page(paginator.num_pages)

        context = {
            "songs": song_list,
            "chck": arg,
            "chck2": len(arg),
        }
        return render(request, 'Details.html', context)
    elif arg == 'gs':
        genre_list = Genre.objects.all()
        paginator = Paginator(genre_list, 3)  # Show 25 contacts per page
        page = request.GET.get('page')


        page = request.GET.get('page')
        try:
            genre_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            genre_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            genre_list = paginator.page(paginator.num_pages)

        context = {
            "genres": genre_list,
            "chck": arg,
            "chck2": len(arg),
        }
        return render(request, 'Details.html', context)
    elif arg == 'as':
        artist_list = Artist.objects.all()
        paginator = Paginator(artist_list, 3)  # Show 25 contacts per page
        page = request.GET.get('page')

        page = request.GET.get('page')
        try:
            artist_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            artist_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            artist_list = paginator.page(paginator.num_pages)

        context = {
            "artists": artist_list,
            "chck": arg,
            "chck2": len(arg),
        }
        return render(request, 'Details.html', context)

def make_request(request):
    form = Request_form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(to="/")


    context = {
        "form": form,
    }
    return render(request, "Make_request.html", context)