import shutil
import tempfile
import os

import pytest
from flask import Flask
from invenio_base.signals import app_loaded
from oarepo_taxonomies.ext import OarepoTaxonomies


@pytest.yield_fixture(scope="module")
def app():
    instance_path = tempfile.mkdtemp()
    app = Flask('testapp', instance_path=instance_path)

    app.config.update(
        SERVER_NAME='127.0.0.1:5000',
        INVENIO_INSTANCE_PATH=instance_path,
        DEBUG=True,
        # in tests, api is not on /api but directly in the root
        FLASK_TAXONOMIES_URL_PREFIX='/2.0/taxonomies/',
        # RECORDS_REST_ENDPOINTS=RECORDS_REST_ENDPOINTS,
    )

    app.secret_key = 'changeme'
    print(os.environ.get("INVENIO_INSTANCE_PATH"))

    OarepoTaxonomies(app)

    app_loaded.send(app, app=app)

    with app.app_context():
        # app.register_blueprint(taxonomies_blueprint)
        print(app.url_map)
        yield app

    shutil.rmtree(instance_path)
