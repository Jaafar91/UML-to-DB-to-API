import json
import pyodbc
from flask import Flask,request
from api_database_connection import *
app = Flask(__name__)

DatabaseType='SQL SERVER'
ConnectionString='Driver={SQL Server};Server=localhost,1475;Database=uda;UID=SA;PWD=Abc@1234;Trusted_Connection=no;'

@app.route("/animals",methods = ['GET','POST'])
def animals_getAll():
	if request.method == 'GET':
		apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
		apiResponseData={"animals":[]}
		apiResponse={"meta":apiResponseMeta,"data":apiResponseData}
		conn = getConnection(DatabaseType,ConnectionString)
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
		conn = getConnection(DatabaseType,ConnectionString)
		cursor = conn.cursor()
		cursor.execute("insert into animals(%s) values (%s)"%(','.join(keys),','.join(values)))
		conn.commit()
		return apiResponse

	return apiResponse

@app.route("/animals/<id>",methods = ['GET'])
def animals_getOne(id):
	
	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta,"data":{}}
	conn = getConnection(DatabaseType,ConnectionString)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM animals WHERE id = '%s'"%(id))
	rows=[]
	columns = [column[0] for column in cursor.description]
	for row in cursor.fetchall():
		apiResponse["data"]=dict(zip(columns, row))
	
	return apiResponse

@app.route("/animals/<id>",methods = ['DELETE'])
def animals_deleteOne(id):

	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta}
	conn = getConnection(DatabaseType,ConnectionString)
	cursor = conn.cursor()
	cursor.execute("DELETE FROM animals WHERE id = '%s'"%(id))
	conn.commit()

	return apiResponse
@app.route("/cages",methods = ['GET','POST'])
def cages_getAll():
	if request.method == 'GET':
		apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
		apiResponseData={"cages":[]}
		apiResponse={"meta":apiResponseMeta,"data":apiResponseData}
		conn = getConnection(DatabaseType,ConnectionString)
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM cages')
		rows=[]
		columns = [column[0] for column in cursor.description]
		for row in cursor.fetchall():
			apiResponse["data"]["cages"].append(dict(zip(columns, row)))
	elif request.method == 'POST':
		req = request.get_json()
		keys=[]
		values=[]
		for item in req:
			keys.append(item)
			values.append("'"+str(req[item])+"'")
		apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
		apiResponse={"meta":apiResponseMeta}
		conn = getConnection(DatabaseType,ConnectionString)
		cursor = conn.cursor()
		cursor.execute("insert into cages(%s) values (%s)"%(','.join(keys),','.join(values)))
		conn.commit()
		return apiResponse

	return apiResponse

@app.route("/cages/<id>",methods = ['GET'])
def cages_getOne(id):
	
	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta,"data":{}}
	conn = getConnection(DatabaseType,ConnectionString)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM cages WHERE id = '%s'"%(id))
	rows=[]
	columns = [column[0] for column in cursor.description]
	for row in cursor.fetchall():
		apiResponse["data"]=dict(zip(columns, row))
	
	return apiResponse

@app.route("/cages/<id>",methods = ['DELETE'])
def cages_deleteOne(id):

	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta}
	conn = getConnection(DatabaseType,ConnectionString)
	cursor = conn.cursor()
	cursor.execute("DELETE FROM cages WHERE id = '%s'"%(id))
	conn.commit()

	return apiResponse

if __name__ == '__main__':
	app.run(debug=True)