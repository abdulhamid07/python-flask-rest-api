from app.models.dosen import Dosen
from app.models.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

def index():
  try:
    dosen = Dosen.query.all()
    data = formatArray(dosen)

    return response.success(data, "success")
  except Exception as e:
    print(e)

def find(id):
  try:
    dosen = Dosen.query.filter_by(id=id).first()
    if dosen:
      data = singleObject(dosen)
      return response.success(data, "Success")
    else:
      return response.badRequest("","Dosen Not Found")
  except Exception as e:
    print(e)


def detailBimbingan(id):
  try:
    dosen = Dosen.query.filter_by(id=id).first()
    mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

    if not dosen:
      return response.badRequest([], "Dosen Not Found")
    
    dataMahasiswa = formatMahasiswa(mahasiswa)
    data = singleDetailMahasiswa(dosen, dataMahasiswa)
    return response.success(data, "success")
  except Exception as e:
    print(e)
    
def create():
  try:
    # using json
    req = request.get_json()
    arrReq = {
      'nidn':req.get('nidn'),
      'nama':req.get('nama'),
      'phone':req.get('phone'),
      'alamat':req.get('alamat')
    }

    # using form data
    # nidn = request.form.get('nidn')
    # nama = request.form.get('nama')
    # phone = request.form.get('phone')
    # alamat = request.form.get('alamat')

    # cek NIDN di tabel dosen
    cekDosen = Dosen.query.filter_by(nidn=arrReq["nidn"]).first()
    if cekDosen:
      return response.badRequest([],'Failed Create Data. NIDN Is Exists')

    dosenField = Dosen(nidn=arrReq["nidn"], nama=arrReq["nama"], phone=arrReq["phone"], alamat=arrReq["alamat"])
    db.session.add(dosenField)
    db.session.commit()
    return response.success(arrReq,'Created Success')
  except Exception as e:
    print(e)

def update(id):
  try:
    req = request.get_json()

    arrReq = {
      'nidn':req.get('nidn'),
      'nama':req.get('nama'),
      'phone':req.get('phone'),
      'alamat':req.get('alamat')
    }

    dosen = Dosen.query.filter_by(id=id).first()
    if dosen:
      dosen.nidn = arrReq['nidn']
      dosen.nama = arrReq['nama']
      dosen.phone = arrReq['phone']
      dosen.alamat = arrReq['alamat']

      db.session.commit()
      return response.success(arrReq, "Dosen Has Been Updated")
    else:
      return response.badRequest("", "Dosen Not Found")
  except Exception as e:
    print(e)


def delete(id):
  try:
    dosen = Dosen.query.filter_by(id=id).first()
    if dosen :
      data = singleObject(dosen)
      db.session.delete(dosen)
      db.session.commit()
      return response.success(data, "Data Has Been Deleted")
    else:
      return response.badRequest("", "Dosen Not Found")
  except Exception as e:
    print(e)


def formatArray(datas):
  array = []
  
  for i in datas:
    array.append(singleObject(i))

  return array

def singleObject(data):
  data = {
    'id':data.id,
    'nidn':data.nidn,
    'nama':data.nama,
    'phone':data.phone,
    'alamat':data.alamat,
  }
  return data


def singleDetailMahasiswa(dosen, dataMhs):
  data = {
    'id':dosen.id,
    'nidn':dosen.nidn,
    'nama':dosen.nama,
    'phone':dosen.phone,
    'alamat':dosen.alamat,
    'mahasiswa':dataMhs
  }
  return data

def formatMahasiswa(data):
  array = []
  for i in data:
    array.append(singleMahasiswa(i))
  return array

def singleMahasiswa(mhs):
  data = {
    'id':mhs.id,
    'nim':mhs.nim,
    'nama':mhs.nama,
    'phone':mhs.phone,
    'alamat':mhs.alamat
  }
  return data
