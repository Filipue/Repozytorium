from flask import Flask
from flask_restful import Resource, Api
from movies import get_movies
from links import get_links
from ratings import get_ratings
from tags import get_tags

app = Flask(__name__)
api = Api(app)

'''
api.add_resource(get_movies, "/movies")
api.add_resource(get_links, "/links")
api.add_resource(get_ratings, "/ratings")
api.add_resource(get_tags, "/tags")
'''

class Movies(Resource):
    def get(self):
        return get_movies()


api.add_resource(Movies, '/movies')

class Links(Resource):
    def get(self):
        return get_links()


api.add_resource(Links, '/links')


class Ratings(Resource):
    def get(self):
        return get_ratings()


api.add_resource(Ratings, '/ratings')


class Tags(Resource):
    def get(self):
        return get_tags()


api.add_resource(Tags, '/tags')


if __name__ == '__main__':
    app.run(debug=True)

# pip freeze > requirements.txt - komenda dodająca plik requirements.txt