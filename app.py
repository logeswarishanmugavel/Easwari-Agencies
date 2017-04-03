from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, send_file, jsonify, json, request

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
		bookList = []
		for book in books:
			bookItem = {
				'bookid': book['BookID'],
				'name': book['BookName'],
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

@app.route("/getPubList",methods=['POST'])
def getPubList():
	print 'inside pub fn'
	try:
		pubs = db.PublishersList.find()

		pubList = []
		for pub in pubs:
			print pub
			pubItem = {
				'name': pub['PubName'],
				'icon': pub['PubIcon']
			}
			pubList.append(pubItem)
	except Exception,e:
		return str(e)
	return json.dumps(pubList)

@app.route("/addInquiry",methods=['POST'])
def addInquiry():
	print 'inside add inquiry'
	try:
		fullname = request.form.get('fullname')
		phone = request.form.get('phone')
		email = request.form.get('email')
		question = request.form.get('question')

		print fullname

		db.Inquiries.insert({
			'fullname':fullname,'phone':phone,'email':email,'question':question
			})
		return jsonify(status='OK',message='inserted successfully')
	except Exception,e:
		return jsonify(status='ERROR',message=str(e))
	
if __name__ == "__main__":
    app.run(host='0.0.0.0')