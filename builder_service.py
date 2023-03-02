
from flask import Flask, flash, request, jsonify, abort, g
from flask import send_file
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import logging
from werkzeug.exceptions import NotFound
from image_builder.build import ImageBuilder

from config import configuration


app = Flask(__name__)
app.config['APPLICATION_ROOT'] = configuration.application_root
app.config['SECRET_KEY'] = configuration.secret_key

builder = ImageBuilder(configuration.repositories_cfg, configuration.build_cfg, configuration.registry_cfg)



@app.route('/images/download/<name>')
def download_image (name):
    print('Getting: ', name)
    path = builder.get_filename(name)
    if path is None:
        abort(404, "File " + name + " not found" )
    return send_file(path, as_attachment=True)


application = DispatcherMiddleware(NotFound(), {"/image_creation": app})


if __name__ == '__main__':
    run_simple("0.0.0.0", configuration.port, application)
