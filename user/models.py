from __init_db__ import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    true_name = db.Column(db.String(32),nullable=True)
    sex=db.Column(db.Enum('男','女','保密'),default='保密')
    birthday=db.Column(db.DateTime,nullable=True)
    tel=db.Column(db.String(11),unique=True,nullable=True)
    mail=db.Column(db.String(64),unique=True,nullable=True)
    address=db.Column(db.String(100),nullable=True)
    head_url=db.Column(db.String(16),nullable=True)

class Account(db.Model):
    __tablename__='account'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    account_name=db.Column(db.String(32),unique=True)
    password = db.Column(db.String(129))
    # blog = db.relationship('Blog', backref='blog', lazy=True)
    # blog = db.relationship('Blog', order_by=Blog.id,back_populates="account")