import slug
from app import app
from flask import Response, request
from app.models import Category


@app.route('/categories', methods=['GET'])
def Categories():
    items = Category.objects().to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/category', methods=['POST'])
def CreateCategory():
    body = request.get_json()
    body['slug'] = slug.slug(body['name'])
    items = Category(**body).save()
    return Response(items, mimetype="application/json", status=200)


@app.route('/category/<id>', methods=['GET'])
def CategoryId(id):
    items = Category.objects(id=id).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/categories/shop/<shop>', methods=['GET'])
def CategoriesShop(shop):
    items = Category.objects(shop=shop).to_json()
    return Response(items, mimetype="application/json", status=200)

