from flask import Blueprint, request

reviews_blueprint = Blueprint(
    'reviews_bp', __name__)


@reviews_blueprint.route('/reviewsPerSong', methods=['GET', 'POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    tracks = tracks_by_genre(projectpath)
    return render_template("meat/genre.html", track_list=tracks[0],genre_name =tracks[1] )
