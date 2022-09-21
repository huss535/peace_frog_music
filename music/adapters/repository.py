import abc

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_tracks(self, alb):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_album(self, album_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_genre(self, album_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_artist(self, album_name):
        raise NotImplementedError
