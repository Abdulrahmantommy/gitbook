from peewee import *


# SQLite database using WAL journal mode and 64MB cache.
db =SqliteDatabase('pos.db', pragmas={'journal_mode': 'wal'})


class User(Model):
    username = TextField(null=False, unique=True)
    password = IntegerField(null=False)
    class Meta:
        database = db
class Category(Model):
    category = TextField(null=False, unique=True)
    class Meta:
        database = db
class Items(Model):
    Name = CharField(null=False, unique=True)
    category = ForeignKeyField(Category, backref='category')
    Price = DecimalField(null=False)
    class Meta:
        database = db
class Branch(Model):

    location = CharField()
    class Meta:
        database = db

db.connect(Model)
db.create_tables([User, Category, Items])