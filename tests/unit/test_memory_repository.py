import pytest
from music.adapters.repository import RepositoryException
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre


def test_repository_builds_database(in_memory_repo):
    assert len(in_memory_repo.genres) == 60


def test_repository_tracks_by_genre(in_memory_repo):
    genre = Genre(4, "Jazz")
    tracks = in_memory_repo.get_tracks_genre("Jazz")
    list_wanted = tracks[0]
    boolean = True
    for track in list_wanted:
        if genre not in track.genres:
            boolean = False

    assert boolean == True


def test_repository_tracks_by_album(in_memory_repo):
    album = Album(4, "Niris")
    tracks = in_memory_repo.get_tracks_genre("Niris")
    list_wanted = tracks[0]
    boolean = True
    for track in list_wanted:
        if album != track.album:
            boolean = False

    assert boolean == True


def test_repository_tracks_by_artist(in_memory_repo):
    artist = Artist(52, "Abominog")
    tracks = in_memory_repo.get_tracks_artist("Abominog")
    list_wanted = tracks[0]
    boolean = True
    for track in list_wanted:
        if artist != track.artist:
            boolean = False

    assert boolean == True
