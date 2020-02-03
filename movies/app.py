import sys
import os
import json
from bottle import Bottle, request, run

def create_app():
    app = Bottle()

    @app.get('/healthz')
    def app_healthz():
        return "<p>Healthy</p>"

    @app.get('/movies')
    def get_movies():
        movies = {
            'movies': [
                'awesome movie 1',
                'awesome movie 2',
                'awesome movie 3',
                'awesome movie 4',
                'awesome movie 5',
            ]
        }
        return json.dumps(movies)


    return app


wsapp = None

if __name__ == "__main__":
    run(create_app(), host="0.0.0.0", port=8080, debug=True)
else:
    wsapp = create_app()