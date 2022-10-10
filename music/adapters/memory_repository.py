from music.adapters.repository import AbstractRepository
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre


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

    def add_albums(self, album: Album):
        pass

    def add_genres(self, genre: Genre):
        pass

    def add_artists(self, artist: Artist):
        pass

    def add_tracks(self, track):
        self.tracks.append(track)

    def get_tracks(self):

        return self.tracks

    def get_tracks_album(self, album_name):
        tracks = []
        for song in self.tracks:
            if song.album is not None:
                if type(song.album.title) == str and song.album.title == album_name:
                    tracks.append(song)
        return tracks, album_name

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

# repo = MemoryRepository()
# alb = os.path.abspath("data")
# repo.add_tracks(alb)
# print(len(repo.tracks))
