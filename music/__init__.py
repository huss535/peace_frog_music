"""Initialize Flask app."""
from _testcapi import test_config
from pathlib import Path

import music.adapters.repository as repo
from flask import Flask, render_template
from music.adapters.memory_repository import populate, MemoryRepository

from music.domainmodel.track import Track
from music.trackList import trackList


def create_some_track():
    some_track = Track(1, "Heat Waves")
    some_track.track_duration = 250
    some_track.track_url = 'https://spotify/track/1'
    return some_track


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path_album = str(Path('music') / 'adapters' / 'data' / 'raw_albums_excerpt.csv')
    data_path_tracks = str(Path('music') / 'adapters' / 'data' / 'raw_tracks_excerpt.csv')
    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()

    populate(repo.repo_instance)

    # @app.route('/')
    # def home():
    # some_track = create_some_track()
    # # Use Jinja to customize a predefined html page rendering the layout for showing a single track.
    # return render_template('header.html')
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(trackList.track_blueprint)
    return app
