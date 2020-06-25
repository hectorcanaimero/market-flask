import os
import time
import hashlib
import slug
from app import app
from flask import jsonify, Response, request, render_template
from app.models import Product


@app.route('/products', methods=['GET'])
def Products():
    items = Product.objects().to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/product', methods=['POST'])
def CreateProduct():
    name = ''
    path = '%s/public/5ef26c251a8d3f34c2351c66/' % (os.getcwd())
    print (path)
    body = request.get_json()
    if request.files:
        f = request.files['file']
        f.save(path, f.filename)
        return 'file uploaded successfully'
    # body['image'] = hashlib.md5(slug.slug(body['name']).encode()).hexdigest()[:15]
    body['slug'] = slug.slug(body['name'])
    print(body)
    items = Product(**body).save()
    return Response(items.to_json(), mimetype="application/json", status=200)


@app.route('/product/<string:id>', methods=['GET'])
def ProductId(id):
    items = Products.objects().get(id=id).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/product/slug/<string:slug>', methods=['GET'])
def ProductSlug(slug):
    items = Products.objects().filter(slug=slug).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route("/upload")
def upload_image():
    return render_template('upload.html')