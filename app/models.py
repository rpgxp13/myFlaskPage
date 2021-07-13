from hashlib import md5
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(64), unique=True, nullable=False)
    fullname = db.Column(db.VARCHAR(45), nullable=False)
    email = db.Column(db.VARCHAR(120), unique=True)
    password = db.Column(db.VARCHAR(128), nullable=False)
    datetime_kor = datetime.datetime.utcnow() + datetime.timedelta(hours=9)

    create_time = db.Column(db.TIMESTAMP, default=datetime_kor)

    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    about_me = db.Column(db.VARCHAR(140))
    last_seen = db.Column(db.TIMESTAMP, default=datetime_kor)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=indenticon&s={}'.format(
            digest, size)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.VARCHAR(128), nullable=False)
    content = db.Column(db.TEXT, nullable=False)

    datetime_kor = datetime.datetime.utcnow() + datetime.timedelta(hours=9)

    create_time = db.Column(db.TIMESTAMP, default=datetime_kor)

    def __repr__(self):
        return '<Post {}>'.format(self.content)