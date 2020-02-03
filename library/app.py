import sys
import os
import json
import requests
from bottle import Bottle, request, run

NAMESPACE = os.getenv("namespace")

def create_app():
    app = Bottle()

    @app.get('/healthz')
    def app_healthz():
        return "<p>Healthy</p>"

    @app.get('/library/books')
    def get_books():
        svc="books"
        svc_url = "http://{svc}.{namespace}:8080/{svc}".format(svc=svc, namespace=NAMESPACE)
        r = requests.get(svc_url)
        return json.dumps(json.loads(r.text))

    @app.get('/library/movies')
    def get_movies():
        svc="movies"
        svc_url = "http://{svc}.{namespace}:8080/{svc}".format(svc=svc, namespace=NAMESPACE)
        r = requests.get(svc_url)
        return json.dumps(json.loads(r.text))

    @app.get('/library/sounds')
    def get_sounds():
        svc="sounds"
        svc_url = "http://{svc}.{namespace}:8080/{svc}".format(svc=svc, namespace=NAMESPACE)
        r = requests.get(svc_url)
        return json.dumps(json.loads(r.text))

    return app

wsapp = None

if __name__ == "__main__":
    run(create_app(), host="0.0.0.0", port=8080, debug=True)
else:
    wsapp = create_app()

#run(create_app(), host="0.0.0.0", port=8080, debug=True)