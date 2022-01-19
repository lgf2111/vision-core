from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

ACCESS = {'customer': 1,
          'admin': 2}

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    access = db.Column(db.Integer, nullable=False, default=1)
    username = db.Column(db.String(100), unique=True, nullable=False) # String should be cap 20
    avatar = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    tokens = db.Column(db.Text)
    def is_admin(self):
        return True if self.access == ACCESS['admin'] else False
    def access_level(self, access):
        return True if self.access <= access else False
    def __repr__(self):
        role = dict((v, k) for k, v in ACCESS.items())[self.access].capitalize()
        return f"{role}('{self.username}', '{self.email}', '{self.password}')"

# @login_manager.user_loader
# def load_user(user_id):
#     return Customer.query.get(int(user_id))

# class AccountCredentials(db.Model, UserMixin):
#     __abstract__ = True
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)

# class Customer(AccountCredentials):
#     id = db.Column(db.Integer, primary_key = True)

# class Employee(AccountCredentials):
#     id = db.Column(db.Integer, primary_key = True)

#class Request(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    productName = db.Column(db.String(20), nullable=False)
#    productID = db.Column()