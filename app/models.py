from app import db


class Users(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)


class Customer(db.Document):
    name = db.StringField(required=True)
    phone = db.IntField(required=True)
    email = db.EmailField()
    shipping = db.DictField()
    notification = db.StringField()


class Favorite(db.Document):
    customer = db.StringField()
    shop = db.StringField()


class Order(db.Document):
    customer = db.StringField()
    order = db.DictField()
    shipping = db.StringField()
    payment = db.StringField()
    data = db.DateField()


class Product(db.Document):
    name = db.StringField()
    slug = db.StringField()
    description = db.StringField()
    image = db.StringField()
    extras = db.DictField()
    preco = db.DictField()
    category = db.StringField()
    shop = db.StringField()


class Category(db.Document):
    name = db.StringField(required=True)
    slug = db.StringField(required=True)
    shop = db.StringField()


class Shop(db.Document):
    name = db.StringField(required=True)
    slug = db.StringField()
    nit = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    phone = db.IntField(required=True, unique=True)
    address = db.DictField()
    shipping = db.DictField()
    payment = db.DictField()
    conversor = db.DictField()
    categories = db.ReferenceField(Category)


class Available(db.Document):
    customer = db.StringField()
    shop = db.StringField()
    stars = db.IntField()