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
		return "test"

	return apiResponse
if __name__ == '__main__':
	app.run(debug=True)