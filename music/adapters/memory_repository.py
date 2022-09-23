import os
from pathlib import Path

from music.adapters.repository import AbstractRepository
from music.adapters.csvdatareader import TrackCSVReader

from music.domainmodel import track


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.tracks = []
        self.genres = set()
        self.albums = set()
        self.artists = set()
        self.prev_first = 0
        self.prev_last = 0
        self.first = 0
        self.last = 0

    def add_tracks(self, alb):
        # alb = os.path.abspath("data")
        # rel = os.path.abspath("data")
        # alb = alb + "/raw_albums_excerpt.csv"
        # rel = rel + "/raw_tracks_excerpt.csv"

        album = str(alb) + '/raw_albums_excerpt.csv'
        track = str(alb) + "/raw_tracks_excerpt.csv"
        file_reader = TrackCSVReader(album, track)
        self.tracks = file_reader.read_csv_files()
        self.tracks.sort()
        self.genres = file_reader.dataset_of_genres
        self.albums = file_reader.dataset_of_albums
        self.artists = file_reader.dataset_of_artists
    def get_tracks_album(self, album_name):
        tracks = []
        for song in self.tracks:
            if song.album is not None:
                if type(song.album.title) == str and song.album.title == album_name:
                    tracks.append(song)
        return tracks

    def get_tracks_genre(self, genre_name):
        tracks = []
        for song in self.tracks:
            if len(song.genres) != 0:
                for genre in song.genres:
                    if genre.name == genre_name:
                        tracks.append(song)
        return tracks, genre_name

    def get_tracks_artist(self, artist_name):
        tracks = []
        for song in self.tracks:
            if song.artist.full_name == artist_name:
                tracks.append(song)

        return tracks, artist_name

    def get_track(self, track_name):
        tracks = []
        for song in self.tracks:
            if song.track_title == track_name:
                tracks.append(song)
        return song, track_name





def populate(alb, repo: MemoryRepository):
    repo.add_tracks(alb)

#repo = MemoryRepository()
#alb = os.path.abspath("data")
#repo.add_tracks(alb)
#print(len(repo.tracks))
