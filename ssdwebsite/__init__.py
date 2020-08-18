import os

from flask import Flask, render_template



#######################
##### Error Pages #####
#######################


def page_not_found(e):
  return render_template('error.html'), 404

def not_allowed(e):
  return render_template('error.html'), 403
#------------------------------------------

def create_app(test_config=None):
    """Factory to configure and return a Flask application.
    Keyword arguments:
    test_config -- dictionary to configure the app for tests (default None)
    """

    # Create the Flask application object using this module's name
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, not_allowed)

    # Configure App
    # -------------
    # Default configuration, can be overwritten by specific environment
    app.config.from_mapping(
        SECRET_KEY="anything",
        DB_URL="postgresql://ssdWebsite_user@localhost/sddWebsite",
        DB_SSLMODE="allow",
    )

    if test_config is None:
        # App configuration for dev or prod if `config.py` exists
        app.config.from_pyfile("config.py", silent=True)

        # Check for environment variables on Heroku
        prod_db_url = os.environ.get("DATABASE_URL", None)
        if prod_db_url is not None:
            app.config.from_mapping(
                DB_URL=prod_db_url,
                DB_SSLMODE="require"
            )
    else:
        # App configuration specifically for tests
        app.config.from_mapping(test_config)


    # Route for home page
    @app.route('/')
    def index():
        return render_template('mainPages/index.html')


    # Return application object to be used by a WSGI server, like gunicorn
    return app
