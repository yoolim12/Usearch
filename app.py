from flask import Flask, render_template, redirect, session, request, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

import pymysql
from main.config import Config
from main.api_urls import api_url
from main.model import db

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.db = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

db = SQLAlchemy(app)

for url in api_url:
    app.register_blueprint(url)

if __name__ == "__main__":
    app.secret_key = "fdjkj"
    app.run(port=5000, debug=True)