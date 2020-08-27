from __init_db__ import db


class Blog(db.Model):
    __tablename__='blog'
    id=db.Column(db.Integer,primary_key=True,unique=True)
    sentence=db.Column(db.Text)
    publication_date=db.Column(db.DateTime)
    # account_id=db.Column(db.Integer,db.ForeignKey('account.id'))
    # account=db.relationship('Account',back_populates='blog')
