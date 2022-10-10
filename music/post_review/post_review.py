from flask import Blueprint, render_template, url_for, request
import music.adapters.repository as repo
import music.post_review.services as services
from music.domainmodel.review import Review

post_reviews_blueprint = Blueprint(
    'post_reviews_bp', __name__)


@post_reviews_blueprint.route('/post_review', methods=['POST'])
def handle_data():
    track_name = request.form['track_name']
    review_text = request.form['review_text']

    new_review = Review(
        track=str(track_name),
        review_text=str(review_text),

    )
    services.add_review(repo,new_review)
    # TODO confirmation/failure to post page
    return render_template("meat/review_confirmation.html")


@post_reviews_blueprint.route('/post_review', methods=['GET', 'POST'])
def form_page():
    return render_template('meat/post_review.html')


