import os
import slug
import json
from app import app
from flask import jsonify, Response, request
from app.models import Order, Customer
from app.notifications import Notifications


@app.route("/order", methods=['POST'])
def orderCreate():
    body = request.get_json()
    customer = Customer.objects().filter(id=body['customer']).first().to_json()
    customer = json.loads(customer)
    req = Notifications.SendUser(customer['notification'])
    items = Order(**body).save()
    return Response(items.to_json(), mimetype="application/json", status=200)


@app.route("/order/<string:id>", methods=['GET'])
def orderId(id):
    items = Order.objects().filter(id=id).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route("/order/customer/<string:id>", methods=['GET'])
def orderCustomer(id):
    items = Order.objects().filter(customer=id).to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route("/order/customer/las/<string:id>", methods=['GET'])
def orderCustomerLast(id):
    items = Order.objects().filter(customer=id).last().to_json()
    return Response(items, mimetype="application/json", status=200)


@app.route("/order/status", methods=['GET'])
def changeStatus():
    req = Notifications.SendActive()
    return jsonify({"status": req.reason, "data": json.loads(req.text)}), 200


@app.route("/order/status/<string:id>", methods=['GET'])
def changeStatusOne(id):
    req = Notifications.SendUser(id)
    return jsonify({"status": req.reason, "data": json.loads(req.text)}), 200