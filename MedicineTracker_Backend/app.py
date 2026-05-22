from flask import Flask
from config import Config
from models import db
from routes.auth import auth, init_oauth

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
init_oauth(app)

from routes.medicines import medicines
from routes.alerts import alerts

app.register_blueprint(auth)
app.register_blueprint(medicines)
app.register_blueprint(alerts)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)