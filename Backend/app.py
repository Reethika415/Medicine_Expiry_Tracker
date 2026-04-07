from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes.auth import auth
from routes.medicines import medicines
from routes.alerts import alerts

app.register_blueprint(auth)
app.register_blueprint(medicines)
app.register_blueprint(alerts)

if __name__ == '__main__':
    app.run(debug=True, port=5000)