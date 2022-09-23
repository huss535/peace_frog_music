import pytest

from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre
from music.trackList import services as trakcs_services
from music.genres import services as genres_services


def test_trackList_services(in_memory_repo):
    number_of_tracks = len(trakcs_services.retrieve_tracks(in_memory_repo))
    assert number_of_tracks == 2000


def test_genres_services(in_memory_repo):
    genre = Genre(4, "Jazz")
    genres = genres_services.retrieve_tracks(in_memory_repo, "Jazz")
    list_of_genres = genres[0]
    boolean = True
    for track in list_of_genres:
        if genre not in track.genres:
            boolean = False

    assert boolean == True


def test_artist_services(in_memory_repo):
    artist = Artist(52, "Abominog")
    artists = genres_services.retrieve_tracks(in_memory_repo, "Abominog")
    list_of_artists = artists[0]
    boolean = True
    for track in list_of_artists:
        if artist != track.artist:
            boolean = False

    assert boolean == True

