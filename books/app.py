import sys
import os
import json
from bottle import Bottle, request, run

def create_app():
    app = Bottle()

    @app.get('/healthz')
    def app_healthz():
        return "<p>Healthy</p>"

    @app.get('/books')
    def get_books():
        books = {
            'books': [
                'awesome book 1',
                'awesome book 2',
                'awesome book 3',
                'awesome book 4',
                'awesome book 5',
            ]
        }
        return json.dumps(books)


    return app


wsapp = None

if __name__ == "__main__":
    run(create_app(), host="0.0.0.0", port=8080, debug=True)
else:
    wsapp = create_app()