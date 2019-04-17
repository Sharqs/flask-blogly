"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)
db.create_all()

debug = DebugToolbarExtension(app)

@app.route('/')
def notHome():
    return redirect('/users')


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('/users.html', user_list=users)


@app.route('/users/new')
def new_user():
    return render_template('/newUser.html')


@app.route('/users', methods=["POST"])
def new_user_submit():
    user_data = request.form()
    return redirect('/users')


@app.route('/users/<int:user_id>')
def user_page():
    return render_template('/userDetails.html')


@app.route('/users/<int:user_id>/edit')
def display_edit():
    return render_template('editUser.html')


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def edit_user():
    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def delete_user():

    return redirect('/users')