
from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "ambergautam"
app.config['MONGO_URI'] =  "mongodb://<databaseuser>:<password>@ds111598.mlab.com:11598/ambergautam"
mongo = PyMongo(app)



@app.route('/', methods = ['POST', 'GET'])
def register():
	if request.method == 'POST':
		users = mongo.db.users 
		users.insert({'firstname' : request.form['fname'],'lasttname' : request.form['lname'],'email' : request.form['email'],'comment' : request.form['comment'], })
	return render_template('index.html') 

if __name__ == '__main__':
	app.secret_key = '12345'
	app.run(debug = True) 