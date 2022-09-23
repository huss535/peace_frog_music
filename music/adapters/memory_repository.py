import csv
import os
from pathlib import Path

from werkzeug.security import generate_password_hash

from music.adapters.repository import AbstractRepository
from music.adapters.csvdatareader import TrackCSVReader

from music.domainmodel import track
from music.domainmodel.user import User


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.tracks = []
        self.genres = set()
        self.albums = set()
        self.artists = set()
        self.users = []
        self.prev_first = 0
        self.prev_last = 0
        self.first = 0
        self.last = 0

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_name) -> User:
        for user in self.users:
            if user.user_name == user_name:
                return user
            else:
                return None

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


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_users(data_path: Path, repo: MemoryRepository):
    users = dict()
    count = 1
    users_filename = str(Path(data_path) / "users.csv")
    for data_row in read_csv_file(users_filename):
        user = User(user_id=count,
                    user_name=data_row[1],
                    password=generate_password_hash(data_row[2])
                    )
        repo.add_user(user)
        users[data_row[0]] = user
        count += 1
    return users


def populate(alb, repo: MemoryRepository):
    repo.add_tracks(alb)
    users = load_users(alb, repo)

# repo = MemoryRepository()
# alb = os.path.abspath("data")
# repo.add_tracks(alb)
# print(len(repo.tracks))
