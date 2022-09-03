from app import app
from apps.login.views import login_blueprint
from apps.fashion.views import fashion_blueprint
from apps.suggestions.views import suggestions_blueprint


app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(fashion_blueprint, url_prefix='/fashion')
app.register_blueprint(suggestions_blueprint, url_prefix='/suggestions')

#database.init_app(app)



if __name__ == '__main__':
    app.run()


