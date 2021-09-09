import json
import pyodbc
from flask import Flask,request
app = Flask(__name__)

def getConnection():
	return pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=ddaa;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')

@app.route("/animals",methods = ['GET','POST'])
def getAll():
	if request.method == 'GET':
		apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
		apiResponseData={"animals":[]}
		apiResponse={"meta":apiResponseMeta,"data":apiResponseData}
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM animals')
		rows=[]
		columns = [column[0] for column in cursor.description]
		for row in cursor.fetchall():
			apiResponse["data"]["animals"].append(dict(zip(columns, row)))
	elif request.method == 'POST':
		req = request.get_json()
		keys=[]
		values=[]
		for item in req:
			keys.append(item)
			values.append("'"+str(req[item])+"'")
		apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
		apiResponse={"meta":apiResponseMeta}
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute("insert into animals(%s) values (%s)"%(','.join(keys),','.join(values)))
		conn.commit()
		return apiResponse

	return apiResponse

@app.route("/animals/<id>",methods = ['GET'])
def getOne(id):
	
	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta,"data":{}}
	conn = getConnection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM animals WHERE id = '%s'"%(id))
	rows=[]
	columns = [column[0] for column in cursor.description]
	for row in cursor.fetchall():
		apiResponse["data"]=dict(zip(columns, row))
	
	return apiResponse

@app.route("/animals/<id>",methods = ['DELETE'])
def deleteOne(id):

	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta}
	conn = getConnection()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM animals WHERE id = '%s'"%(id))
	conn.commit()

	return apiResponse
if __name__ == '__main__':
	app.run(debug=True)