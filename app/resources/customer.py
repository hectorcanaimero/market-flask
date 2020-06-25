from app import app
from flask import Response, request
from app.models import Customer


@app.route('/customer', methods=['GET'])
def Customers():
    items = Customer.objects().to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route('/customer', methods=['POST'])
def CreateCustomer():
    body = request.get_json()
    items = Customer(**body).save()
    return Response(items.to_json(), mimetype="application/json", status=200)


@app.route('/customer/<string:id>', methods=['GET'])
def CustomerId(id):
    items = Customer.objects().filter(id=id).to_json()
    return Response(items, mimetype="application/json", status=200)