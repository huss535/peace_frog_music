from flask import Blueprint, render_template, url_for, request
import music.adapters.repository as repo
import music.genres.services as services

genres_blueprint = Blueprint(
    'genres_bp', __name__)


@genres_blueprint.route('/tracks_by_genre', methods=['GET', 'POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    tracks = tracks_by_genre(projectpath)
    return render_template("meat/genre.html", track_list=tracks[0],genre_name =tracks[1] )


def tracks_by_genre(genre_name):
    return services.retrieve_tracks(repo.repo_instance, genre_name)


@genres_blueprint.route('/searchGenre', methods=['GET', 'POST'])
def form_page():
    return render_template('meat/search_genres.html')


