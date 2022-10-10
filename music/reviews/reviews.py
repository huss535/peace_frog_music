from flask import Blueprint, render_template, url_for, request
import music.adapters.repository as repo
import music.reviews.services as services

reviews_blueprint = Blueprint(
    'reviews_bp', __name__)


@reviews_blueprint.route('/reviewsPerSong', methods=['GET', 'POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    reviews = reviews_by_tracks(projectpath)
    return render_template("meat/review.html", review_list=reviews[0], track_name=reviews[1])


def reviews_by_tracks(track_name):
    return services.retrieve_tracks(repo.repo_instance, track_name)


@reviews_blueprint.route('/searchReview', methods=['GET', 'POST'])
def form_page():
    return render_template('meat/search_review.html')


