from werkzeug.utils import secure_filename
from app.models.user import User
from app import db,response,app
from flask import request
from flask_jwt_extended import *
from datetime import datetime
import os

def createAdmin():
  try:
    req = request.get_json()

    arrReq = {
      'name':req.get('name'),
      'email':req.get('email'),
      'level':1,
    }

    user = User(name=arrReq['name'], email=arrReq['email'], level=arrReq['level'])
    user.passwordHash(req.get('password'))
    db.session.add(user)
    db.session.commit()

    return response.success(arrReq, "Admin Success Created")
  except Exception as e:
    print(e)

def login():
  try:
    req = request.get_json()
    email = req.get('email')
    password = req.get('password')
    
    user = User.query.filter_by(email=email).first()

    if not user:
      return response.badRequest([], "Email Not Found")

    if not user.checkPassword(password):
      return response.badRequest([], "Incorrect Email Or Password")
    
    data = singleObject(user)
    
    expires = datetime.timedelta(days=7)
    expire_refresh = datetime.timedelta(days=7)

    access_token = create_access_token(data, fresh=True, expires_delta=expires)
    refresh_token = create_refresh_token(data, expires_delta=expire_refresh)

    return response.success({
      "user":data,
      "access_token":access_token,
      "refresh_token":refresh_token,
    }, "Login Success")

  except Exception as e:
    print(e)

def uploadImage():
  try:  
    image = request.files
    now = datetime.now()
    curr_time = now.strftime("%H%M%S")

    if 'image' not in image:
      return response.badRequest("", "No Image For Upload")
    
    file = request.files['image']
    # if file.filename == "":
    #   return response.badRequest("", "Empty File")

    if file and allowedImage(file.filename):
      filename = secure_filename(file.filename)
      renameFile = "image-"+curr_time+"-"+filename

      file.save(os.path.join(app.config['UPLOAD_FOLDER'], renameFile))
      return response.success({"file":renameFile}, "Upload Success")
    else:
      return response.badRequest({"file":file.filename}, "Exstension Not Allowed")
  except Exception as e:
    print(e)

def singleObject(data):
  data = {
    'id':data.id,
    'name':data.name,
    'email':data.email,
    'level':data.level,
  }
  return data

def allowedImage(filename):
  extImage = ['png','jpg','jpeg','svg']
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in extImage
