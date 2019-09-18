from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    #Twitter users that we analyze
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15), nullable = False)

    def __repr__(self):
        return '<User %r>'.format(self.name)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Unicode(280))
    embedding = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
