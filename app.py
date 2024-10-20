# app.py
from flask import Flask
from routes.apis import apis
from routes.admin_client import admin_client
from extensions import db  # Импортируем db из extensions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app) 

# Регистрация Blueprints
app.register_blueprint(apis)
app.register_blueprint(admin_client)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8888)
