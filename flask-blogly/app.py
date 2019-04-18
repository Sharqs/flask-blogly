"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime, date, time

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
    posts = Post.query.filter(Post.user_id == profile.id).all()
    return render_template('/userDetails.html', profile=profile, post_list=posts)


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


@app.route('/users/<int:user_id>/posts/new')
def new_post(user_id):
    profile = User.query.get_or_404(user_id)
    return render_template('newPost.html', profile=profile)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def new_post_submitted(user_id):
    title = request.form['title']
    content = request.form['content']
    created_at = datetime.now()
    print('************')
    print(created_at)

    new_post = Post(title=title, content=content, created_at=created_at, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')


@app.route('/posts/<int:post_id>')
def posts(post_id):
    post = Post.query.get_or_404(post_id)
    profile = User.query.get_or_404(post.user_id)
    return render_template('posts.html', post=post, profile=profile)


@app.route('/posts/<int:post_id>', methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(f'/users/{post.id}')
