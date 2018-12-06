from flask import Flask
from webapp.views.index import bp as index_bp
from webapp.views.registermember import bp as registermember_bp
from webapp.views.registercollege import bp as registercollege_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(registermember_bp)
app.register_blueprint(registercollege_bp)


