from readFile import read_file
from klasa import Ratings

def get_ratings_data():
    data = read_file("data/ratings.csv")
    ratings = []
    for rating in data.split('\n'):
        if len(rating) and "userId" not in rating:
            rating = rating.split(',')
            ratings.append(rating)
    return ratings

def get_ratings():
    print(get_ratings_data())
    return [Ratings(rating[0], rating[1], rating[2], rating[3]).__dict__ for rating in get_ratings_data()]