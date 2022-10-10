from flask import Blueprint, render_template, url_for, request;
import music.adapters.repository as repo
import music.post_review.services as services
import music.domainmodel.review as Review;

post_reviews_blueprint = Blueprint(
    'post_reviews_bp', __name__)


@post_reviews_blueprint.route('/post_review', methods=['GET', 'POST'])
def handle_data():
    track_name = request.form['track_name']
    review_text = request.form['review_text']
    new_review = Review(track_name, review_text)
    services.add_new_review(new_review)
    # TODO confirmation/failure to post page
    return render_template("meat/post_review.html", track_list=tracks[0],post_review_name =tracks[1] )


@post_reviews_blueprint.route('/searchpost_review', methods=['GET', 'POST'])
def form_page():
    return render_template('meat/search_post_reviews.html')


