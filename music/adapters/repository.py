import abc

from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_tracks(self, alb):
        raise NotImplementedError

    @abc.abstractmethod
    def add_albums(self, album: Album):
        raise NotImplementedError

    @abc.abstractmethod
    def add_genres(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def add_artists(self, artist: Artist):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_album(self,album_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_genre(self,genre_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_artist(self, artist_name):
        raise NotImplementedError
# @abc.abstractmethod
# def get_tracks_album(self, album_name):
# raise NotImplementedError

# @abc.abstractmethod
# def get_tracks_genre(self, album_name):
# raise NotImplementedError

# @abc.abstractmethod
#  def get_tracks_artist(self, album_name):
#  raise NotImplementedError
