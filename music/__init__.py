"""Initialize Flask app."""
import os
from _testcapi import test_config
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker
from sqlalchemy.pool import NullPool

import music.adapters.repository as repo
from flask import Flask, render_template

from music.adapters import memory_repository, repository_populate
from music.adapters.database_repository import database_repository
from music.adapters.memory_repository import MemoryRepository
from music.adapters.orm import map_model_to_tables, metadata
from music.adapters.repository_populate import populate

from music.domainmodel.track import Track
from music.genres import genres
from music.artists import artists
from music.albums import albums
from music.trackList import trackList
from music.authentication import authentication


def create_some_track():
    some_track = Track(1, "Heat Waves")
    some_track.track_duration = 250
    some_track.track_url = 'https://spotify/track/1'
    return some_track


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')
    alb = Path('music') / 'adapters' / 'data'
    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()

    populate(alb, repo.repo_instance)


    # Here the "magic" of our repository pattern happens. We can easily switch between in memory data and
    # persistent database data storage for our application.

    if app.config['REPOSITORY'] == 'memory':
        # Create the MemoryRepository implementation for a memory-based repository.
        repo.repo_instance = memory_repository.MemoryRepository()
        # fill the content of the repository from the provided csv files (has to be done every time we start app!)
        database_mode = False
        repository_populate.populate(alb, repo.repo_instance)

    elif app.config['REPOSITORY'] == 'database':
        # Configure database.
        database_uri = app.config['SQLALCHEMY_DATABASE_URI']

        # CHECK NAME FOR MUSIC.DB

        # We create a comparatively simple SQLite database, which is based on a single file (see .env for URI).
        # For example the file database could be located locally and relative to the application in music.db,
        # leading to a URI of "sqlite:///music.db". 
        # Note that create_engine does not establish any actual DB connection directly!
        database_echo = app.config['SQLALCHEMY_ECHO']
        # Please do not change the settings for connect_args and poolclass!
        database_engine = create_engine(database_uri, connect_args={"check_same_thread": False}, poolclass=NullPool,
                                        echo=database_echo)

        # Create the database session factory using sessionmaker (this has to be done once, in a global manner)
        session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)
        # Create the SQLAlchemy DatabaseRepository instance for an sqlite3-based repository.
        repo.repo_instance = database_repository(session_factory)

        if app.config['TESTING'] == 'True' or len(database_engine.table_names()) == 0:
            print("REPOPULATING DATABASE...")
            # For testing, or first-time use of the web application, reinitialise the database.
            clear_mappers()
            metadata.create_all(database_engine)  # Conditionally create database tables.
            for table in reversed(metadata.sorted_tables):  # Remove any data from the tables.
                database_engine.execute(table.delete())

            # Generate mappings that map domain model classes to the database tables.
            map_model_to_tables()

            database_mode = True
            repository_populate.populate(alb, repo.repo_instance)
            print("REPOPULATING DATABASE... FINISHED")

        else:
            # Solely generate mappings that map domain model classes to the database tables.
            map_model_to_tables()

    # @app.route('/')
    # def home():
    # some_track = create_some_track()
    # # Use Jinja to customize a predefined html page rendering the layout for showing a single track.
    # return render_template('header.html')
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)
        
        from .trackList import trackList
        app.register_blueprint(trackList.track_blueprint)

        from music.genres.genres import handle_data
        app.register_blueprint(genres.genres_blueprint)

        from music.albums.albums import handle_data
        app.register_blueprint(albums.albums_blueprint)
        
        from music.artists.artists import handle_data
        app.register_blueprint(artists.artists_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        # Register a callback the makes sure that database sessions are associated with http requests
        # We reset the session inside the database repository before a new flask request is generated
        @app.before_request
        def before_flask_http_request_function():
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.reset_session()

        # Register a tear-down method that will be called after each request has been processed.
        @app.teardown_appcontext
        def shutdown_session(exception=None):
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.close_session()

    return app
