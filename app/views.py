from flask import Flask, jsonify, request
from app import app
import json
import uuid
from werkzeug.security import generate_password_hash
from .models import User_request
# from .models import User_auth

# app.config['SECRET_KEY'] = 'thisissecret'
# app.config['*****']

user_request = User_request()
# user_log = User_auth() 

# #get all requests for all users
# @app.route('/api/v1/request/', methods=['GET'])
# def _get_details():
#     requests = user_request.get_requests()
#     return jsonify(requests), 200

# #get all requests for one user
# @app.route('/api/v1/request/<int:id>', methods=['GET'])
# def user_detail(id):
#     single_request = user_request.get_request_for_one_user(id)
#     return jsonify (single_request), 200


#create request
@app.route('/api/v1/request/create', methods=['POST'])
def create_item():
    create = request.get_json()
    if create['id']=="" or create['name']=="" or create['dop']=="" or create['top']=="" or create['item requested for']=="":
        return jsonify({'message':'All fields are to be filled', 'status':'failed'}),400
    create = user_request.create_request(create['id'],create['name'],create['dop'],create['top'],create['item requested for'])
    return jsonify({'status':'ok',  'message':'Request placed successfully'}),201

# #update 
# @app.route('/api/v1/request/update/<string:name>', methods=['PUT'])
# def update_item(name):
#     modify = request.get_json()
#     if modify['name']=="":
#         return jsonify({'status':'failed',  'message': 'Enter a valid name'}),400
#     else:
#         modified = user_request.update_request(name ,modify['name'])
#         return jsonify({'details': modify['name']}), 200

# #sign-in
# @app.route('/api/v1/signin', methods=['POST'])
# def user_sign_in():
#     data = request.get_json()

#     data = user_log.sign_in(data['username'], data['password'])
#     return jsonify({'message': 'Welcome'}),200
# #sign-up
# @app.route('/api/v1/signup', methods=['POST'])
# def user_sign_up():
#     data = request.get_json()

#     hashed_password = generate_password_hash(data['password'], method='sha256')
#     new_user = user(public_id=str(uuid.uuid4()), name=data['name'],pasword=hashed_password,admin=False)
#     user_log.sign_up()
#     # data = user_log.sign_up(data['name'], data['username'],data['password'],data['email'])
    
#     return jsonify({'message':'Account successfully created'}), 201
