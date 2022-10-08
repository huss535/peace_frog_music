from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship, synonym

# global variable giving access to the MetaData (schema) information of the database
from music import Track
from music.domainmodel import track, artist, album
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre

metadata = MetaData()

albums_table = Table(
    'albums', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('album_id', Integer, unique=True, nullable=False),
    Column('title', String(255), nullable=False),
    Column('album_url', String(255), nullable=False),
    Column('album_type', String(255), nullable=False),
    Column('release_year', Integer)
)

artists_table = Table(
    'artists', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('artist_id', Integer, unique=True, nullable=False),
    Column('full_name', String(1024), nullable=False)

)

genres_table = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('genre_id', Integer, unique=True, nullable=False),
    Column('name', String(1024), unique=True, nullable=False)
)

tracks_table = Table(
    'tracks', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('track_id', Integer, unique=True, nullable=False),
    Column('artists_id', ForeignKey('artists.artist_id')),
    Column('title', String(255), nullable=False),
    Column('track_url', String(255), nullable=False),
    Column('track_duration', Integer, nullable=False)
)

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, unique=True, nullable=False),
    Column('user_name', String(1024), unique=True, nullable=False),
    Column('password', String(1024), nullable=False)
)


def map_model_to_tables():
    mapper(Album, albums_table, properties={
        '_Album__title': albums_table.c.title,
        '_Album__album_id': albums_table.c.album_id,
        '_Album__album_url': albums_table.c.album_url,
        '_Album__album_type': albums_table.c.album_type,
        '_Album__release_year': albums_table.c.release_year

    })

    mapper(Artist, artists_table, properties={
        '_Artist__full_name': artists_table.c.full_name,
        '_Artist__artist_id': artists_table.c.artist_id,

    })

    mapper(Genre, genres_table, properties={
        '_Genre__genre_id': genres_table.c.genre_id,
        '_Genre__name': genres_table.c.name,

    })

    mapper(Track, tracks_table, properties={
        '_Track__title': tracks_table.c.title,
        '_Track__track_id': tracks_table.c.track_id,
        '_Track__track_url': tracks_table.c.track_url,
        '_Track__track_duration': tracks_table.c.track_duration,
        '_Track__album': relationship(artist, backref="_artist__artist_id"),
        '_Track__artist': relationship(artist, backref="_artist__artist_id"),
        '_Track__genres': relationship(artist, backref="_artist__artist_id")


    })
