import datetime

from flask.ext.bcrypt import check_password_hash as check_hash
from flask.ext.bcrypt import generate_password_hash as make_hash
from flask.ext.login import UserMixin, AnonymousUserMixin
from peewee import *

DATABASE = SqliteDatabase('tacocat.db')


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    @classmethod
    def create_user(cls, email, password, admin=False):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=make_hash(password),
                    admin=admin)
        except IntegrityError:
            raise ValueError("User already exists.")


class Taco(Model):
    """Tacos have a protein, a shell, a true/false for cheese, and a freeform area for extras"""
    protein = CharField()
    shell = CharField()
    cheese = BooleanField()
    extras = TextField()
    user = ForeignKeyField(rel_model=User, related_name='tacos')

    class Meta:
        database = DATABASE


class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Guest'


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco], safe=True)
    DATABASE.close()
