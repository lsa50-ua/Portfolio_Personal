from flask import Flask
from portfolio_app.routes import init_routes

def create_app():
    app = Flask(__name__)

    init_routes(app)

    app.run(debug=True, host='127.0.0.1', port=5000)

    return app