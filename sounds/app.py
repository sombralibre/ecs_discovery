import sys
import os
import json
from bottle import Bottle, request, run

def create_app():
    app = Bottle()

    @app.get('/healthz')
    def app_healthz():
        return "<p>Healthy</p>"

    @app.get('/sounds')
    def get_sounds():
        sounds = {
            'sounds': [
                'awesome sound 1',
                'awesome sound 2',
                'awesome sound 3',
                'awesome sound 4',
                'awesome sound 5',
            ]
        }
        return json.dumps(sounds)


    return app


wsapp = None

if __name__ == "__main__":
    run(create_app(), host="0.0.0.0", port=8080, debug=True)
else:
    wsapp = create_app()