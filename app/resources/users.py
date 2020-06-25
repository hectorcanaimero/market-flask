from flask import jsonify, request
from app import app, bcrypt, jwt
from app.models import Users


@jwt.unauthorized_loader
def unnautorized(callback):
    return jsonify({'ok': False, 'message': 'Missing Authorization Header'}), 401


@app.route('/user/register', methods=['POST'])
def Register():
    body = request.get_json()
    body['password'] = bcrypt.generate_password_hash(body['password']).decode('utf-8')
    items = Users(**body).save()
    success = {'name': items['name'], 'email': items['email']}
    if items:
        return {"ok": True, "data": success}, 200
    return {"ok": False, "data": {"message": "User not created"}}, 400
