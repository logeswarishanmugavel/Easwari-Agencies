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
	print 'inside fn'
	try:
		books = db.BookList.find()

		bookList = []
		for book in books:
			print book
			bookItem = {
				'name': book['BookName'],
				'price': book['BookPrice']
			}
			bookList.append(bookItem)
	except Exception,e:
		return str(e)
	return json.dumps(bookList)

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