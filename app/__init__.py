#it's like a python packege for our/my application
from flask import Flask
from .routes import blueprints


def create_app()->Flask:
    app = Flask(__name__)
    app.config["SECRECT_KEY"] = "my-secrect-key"
    app.secret_key = "my-secrect-key"
    
    for blueprint in blueprints:
        app.register_blueprint(
            blueprint,
            url_prefix="/",
        )
    
    return app

create_app()