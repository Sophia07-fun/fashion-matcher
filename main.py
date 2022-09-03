from flask import Flask
from apps.login.views import api_blueprint
def create_app():
    app = Flask(__name__)
    # app.register_blueprint(api_blueprint,url_prefix='/login')

    return app


if __name__ == '__main__':
    app = create_app()


    app.run()
