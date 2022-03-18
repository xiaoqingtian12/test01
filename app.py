from flask import Flask, g, session
from flask_migrate import Migrate
from blueprints import qa_bp, user_bp, center_bp, api_bp, demand_bp
from exts import db, mail
import config
from models import UserModel

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)
app.register_blueprint(center_bp)
app.register_blueprint(api_bp)
app.register_blueprint(demand_bp)


@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            g.user = user
        except:
            g.user = None


@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
