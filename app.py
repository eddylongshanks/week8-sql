from helpers.providers import FieldNameProvider
import sqlite3
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/test_database.db"
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    secondname = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(32), nullable=False)

    # Define __repr__ that will be called when querying e.g. 'Users.query.all()'
    def __repr__(self):
        obj_repr = f'ID: {self.id}, ' \
                   f'First Name: {self.firstname}, ' \
                   f'Second Name: {self.secondname}, ' \
                   f'Country: {self.country}' \

        return obj_repr


@app.route("/")
def index():
    all_users = Users.query.all()
    return render_template("index.html", all_users=all_users)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        _form = request.form

        _error_summary = get_errors(_form)

        if _error_summary:            
            return render_template("add_user.html", error_summary=_error_summary)

        new_user = Users(firstname=_form['first-name'],
                         secondname=_form['second-name'],
                         country=_form['country'])

        print(new_user)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/")

    return render_template("add_user.html")


def get_errors(form_to_validate):
        invalid_input = list()

        field_name_provider = FieldNameProvider()

        for i, k in form_to_validate.items():
            if k == "":
                invalid_input.append(field_name_provider.get_name(i))
        
        if invalid_input:
            error_summary = f"Following information is required: {', '.join(invalid_input)}"
            return error_summary

app.run(debug=True)
