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
    first = request.form['first']
    last = request.form['last']
    img = request.form['img']

    new = User(first_name=first, last_name=last, image_url=img)
    db.session.add(new)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>')
def user_page(user_id):
    profile = User.query.get_or_404(user_id)
    print(profile)
    return render_template('/userDetails.html', profile=profile)


@app.route('/users/<int:user_id>/edit')
def display_edit(user_id):
    profile = User.query.get_or_404(user_id)
    return render_template('editUser.html', profile=profile)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def edit_user(user_id):
    profile = User.query.get_or_404(user_id)

    profile.first_name = request.form['first']
    profile.last_name = request.form['last']
    profile.image_url = request.form['img']

    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    profile = User.query.get_or_404(user_id)
    db.session.delete(profile)
    db.session.commit()
    return redirect('/users')
