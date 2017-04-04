from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, send_file, jsonify, json, request
from datetime import datetime

app = Flask(__name__)

client = MongoClient('localhost:27017');
db = client.easwari

@app.route("/")
def index():
    return send_file("templates/index.html")

@app.route("/getBookList",methods=['POST'])
def getBookList():
	try:
		books = db.BookList.find()
		print books
		bookList = []
		for book in books:
			bookItem = {
				'bookid': book['BookID'],
				'name': book['BookName'],
				'freq': book['BookFrequency'],
				'type': book['BookType'],
				'lang': book['BookLanguage'],
				'pubname': book['Publisher'],
				'genre': book['Genre'],
			}
			bookList.append(bookItem)
	except Exception,e:
		return str(e)
	return json.dumps(bookList)


@app.route('/getBookListData',methods=['POST'])
def getBookListData():
	print 'inside detail fn'
	try:
		bookid = request.json['id']
		print bookid
		book = db.BookList.find_one({'BookID':bookid})
		bookDetail = {
			'name': book['BookName'],
			'price': book['BookPrice'],
			'freq': book['BookFrequency'],
			'type': book['BookType'],
			'lang': book['BookLanguage'],
			'pubname': book['Publisher'],
			'desc': book['BookDescription'],
			'genre': book['Genre'],
			'photo': book['Photo'],
		}
	except Exception,e:
		return str(e)
	return json.dumps(bookDetail)

@app.route("/addApplication",methods=['POST'])
def addApplication():
	print 'inside add appl'
	try:
		agencyname = request.form.get('agencyname')
		sal = request.form.get('sal')
		contactperson = request.form.get('contactperson')
		agencyarea = request.form.get('agencyarea')
		address = request.form.get('address')
		city = request.form.get('city')
		state = request.form.get('state')
		pincode = request.form.get('pincode')
		phone = request.form.get('phone')
		email = request.form.get('email')

		print city
		print state

		db.Applications.insert({
			'agencyname':agencyname,'sal':sal,'contactperson':contactperson,'agencyarea':agencyarea,'address':address,'city':city,'state':state,'pincode':pincode,'phone':phone,'email':email, 'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f'), 'status':'New'
			})
		return jsonify(status='OK',message='inserted successfully')
	except Exception,e:
		return jsonify(status='ERROR',message=str(e))

@app.route("/addInquiry",methods=['POST'])
def addInquiry():
	print 'inside add inquiry'
	try:
		fullname = request.form.get('fullname')
		phone = request.form.get('phone')
		email = request.form.get('email')
		question = request.form.get('question')

		print fullname
		print datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f')

		db.Inquiries.insert({
			'fullname':fullname,'phone':phone,'email':email,'question':question,'date':datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f'),'answered':'no'
			})
		return jsonify(status='OK',message='inserted successfully')
	except Exception,e:
		return jsonify(status='ERROR',message=str(e))
	
if __name__ == "__main__":
    app.run(host='0.0.0.0')