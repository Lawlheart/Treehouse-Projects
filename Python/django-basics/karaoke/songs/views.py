from django.shortcuts import render

from .models import Song, Performer


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})


def song_detail(request, pk):
    song = Song.objects.get(pk=pk)
    return render(request, 'songs/song_detail.html', {'song': song})


def performer_detail(request, pk):
    performer = Performer.objects.get(pk=pk)
    songs = Song.objects.get(performer=performer)
    return render(request, 'songs/performer_detail.html', {
        'performer': performer, 'songs': songs})
