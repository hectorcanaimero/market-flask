import os
import slug
import json
from app import app
from flask import jsonify, Response, request
from app.models import Shop, Category


@app.route('/shop', methods=['GET'])
def Shops():
    items = Shop.objects().to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/shop', methods=['POST'])
def CreateShop():
    body = request.get_json()
    body['slug'] = slug.slug(body['name'])
    items = Shop(**body).save()
    path = '%s/public/%s' % (os.getcwd(), items.id)
    os.mkdir(path, 755)
    return Response(items.to_json(), mimetype="application/json", status=200)


@app.route('/shop/<string:id>', methods=['GET'])
def ShopId(id):
    items = Shop.objects().get(id=id).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/shop/nit/<id>', methods=['GET'])
def ShopNit(id):
    items = Shop.objects().filter(nit=id).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/shop/slug/<string:slug>', methods=['GET'])
def ShopSlug(slug):
    items = Shop.objects().filter(slug=slug).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/shop/collection/<id>', methods=['GET'])
def ShopCollection(id):
    categories = InternCategoriesShop(id)
    shop = Shop.objects().filter(id=id)
    for t in shop:
        items = {
            "id": str(t['id']),
            "name": t['name'],
            "email": t['email'],
            "nit": t['nit'],
            "phone": t['phone'],
            "address": t['address'],
            "shipping": t['shipping'],
            "_categories": json.loads(categories)
        }
        return items, 200


def InternCategoriesShop(shop):
    return Category.objects().filter(shop=shop).to_json()