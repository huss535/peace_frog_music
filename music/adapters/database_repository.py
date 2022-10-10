from abc import ABC
from datetime import date
from typing import List

from sqlalchemy import desc, asc
# from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session

from music.domainmodel.track import Track
from music.adapters.repository import AbstractRepository
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class database_repository(AbstractRepository):

    def __init__(self, session_factory):
        self.tracks = []
        self.first = 0
        self.last = 0
        self.prev_first = 0
        self.prev_last = 0
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_tracks(self, track: Track):
        self.tracks.append(track)
        with self._session_cm as scm:
            scm.session.add(track)
            scm.commit()

    def add_albums(self, album: Album):
        with self._session_cm as scm:
            scm.session.add(album)
            scm.commit()

    def add_genres(self, genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def add_artists(self, artist: Artist):
        with self._session_cm as scm:
            scm.session.add(artist)
            scm.commit()

    def get_tracks(self):
        self.tracks = self._session_cm.session.query(Track).all()
        return self.tracks

    def get_tracks_album(self, album_name) -> List[Track]:
        if album_name is None or album_name == "":
            tracks = self._session_cm.session.query(Track).all()

        else:
            tracks = self.get_tracks()
            for i in range(len(tracks) - 1, -1, -1):
                if tracks[i].album == None or tracks[i].album.title != album_name:
                    tracks.pop(i)
            #tracks = self._session_cm.session.query(Track).filter(Track.__album.__title == album_name).all()
        return tracks, album_name

    def get_tracks_artist(self, artist_name):
        if artist_name is None:
            tracks = self._session_cm.session.query(Track).all()
        else:
            tracks = self.get_tracks()
            for i in range(len(tracks) -1 ,-1, -1):
                if tracks[i].artist.full_name != artist_name:
                    tracks.pop(i)
            #tracks = self._session_cm.session.query(Track).filter(Track.__artist.__full_name == artist_name).all()
        return tracks, artist_name

    # BANDAID SOLUTION, USING METHOD RAXXED FROM MEMORY REPO, MAY CHANGE IF HAVE TIME
    def get_tracks_genre(self, genre_name: str):
        tracks = []
        all_tracks = self._session_cm.session.query(Track).all()
        for song in all_tracks:
            if len(song.genres) != 0:
                for genre in song.genres:
                    if genre.name == genre_name:
                        tracks.append(song)
        return tracks, genre_name
