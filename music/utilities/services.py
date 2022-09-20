from typing import Iterable
import random

from music.adapters.repository import AbstractRepository
#from music.domainmodel import Article


def get_tracks_names(repo: AbstractRepository):
    pass
    #tags = repo.get_tags()
    #tag_names = [tag.tag_name for tag in tags]

    #return tag_names

# TODO we COULD salvage this piece of code to get tracks instead of articles
# def get_random_articles(quantity, repo: AbstractRepository):
#     article_count = repo.get_number_of_articles()

#     if quantity >= article_count:
#         # Reduce the quantity of ids to generate if the repository has an insufficient number of articles.
#         quantity = article_count - 1

#     # Pick distinct and random articles.
#     random_ids = random.sample(range(1, article_count), quantity)
#     articles = repo.get_articles_by_id(random_ids)

#     return articles_to_dict(articles)


# ============================================
# Functions to convert dicts to model entities
# ============================================






