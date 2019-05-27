from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    comments = db.relationship('Comment', backref='user', lazy="dynamic")
    posts = db.relationship('Post', backref='user_post', lazy = "dynamic")
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f'User {self.username}'    

class Category(db.Model):
    __tablename__="categories"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer)
    pitch_category = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    posts=db.relationship('Post', backref='comment', lazy='dynamic')

   
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    text = db.Column(db.String(255))
    post_id = db.Column(db.Integer)
    category=db.Column(db.String(255))
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    comment_id =db.Column(db.Integer, db.ForeignKey('comments.id'))
    
    # comments=db.relationship('Comment', backref='post', lazy='dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()


    def get_posts(self):
        posts = Post.query.all()
        return posts

    def get_post(self):
        post = Post.query.filter_by(user_id)
        return post


    def __repr__(self):
        return f'User {self.name}'
