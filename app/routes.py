from app import app,response
from app.controllers import DosenController
from app.controllers import UserController
from flask import request
from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

@app.route('/')
def index():
  return 'Method Not Defined'

@app.route('/api/dosen', methods=['GET','POST'])
@jwt_required()
def dosens():
  if request.method == 'GET':
    return DosenController.index()
  else:
    return DosenController.create()

@app.route('/api/dosen/pembimbing/<id>', methods=['GET'])
@jwt_required()
def detail(id):
  return DosenController.detailBimbingan(id)

@app.route('/api/dosen/<id>', methods=['GET','PUT','DELETE'])
@jwt_required()
def find(id):
  if request.method == 'GET':
    return DosenController.find(id)
  elif request.method == 'POST':
    return DosenController.update(id)
  else:
    return DosenController.delete(id)

@app.route('/api/admin', methods=['POST'])
@jwt_required()
def createAdmin():
  return UserController.createAdmin()

@app.route('/api/admin/login', methods=['POST'])
def login():
  return UserController.login()

@app.route('/api/islogin', methods=['GET'])
@jwt_required()
def isLogin():
  current_user = get_jwt_identity()
  return response.success(current_user,"success")

@app.route('/api/upload/image', methods=['POST'])
def uploadImage():
  return UserController.uploadImage()