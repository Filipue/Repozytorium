import datetime


class Movies:
    def __init__(self, movieId: str, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres =genres


class Links:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId =tmdbId


class Ratings:
    def __init__(self, userId: str, movieId: str, rating: float, timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.rating =rating
        self.timestamp = timestamp


class Tags:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp
