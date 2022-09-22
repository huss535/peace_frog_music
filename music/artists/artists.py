from flask import Blueprint, render_template, url_for, request
from music.adapters.memory_repository import MemoryRepository
from music.trackList.services import retrieve_tracks
import music.adapters.repository as repo
import music.artists.services as services

artists_blueprint = Blueprint(
    'artists_bp', __name__)


@artists_blueprint.route('/tracks_by_artist', methods=['GET', 'POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    tracks = tracks_by_artist(projectpath)
    return render_template("meat/artist.html", track_list=tracks[0],artist_name =tracks[1] )


def tracks_by_artist(artist_name):
    return services.retrieve_tracks(repo.repo_instance, artist_name)


@artists_blueprint.route('/searchArtist', methods=['GET', 'POST'])
def form_page():
    return render_template('meat/search_artists.html')


