import json
import pyodbc
from flask import Flask,request
app = Flask(__name__)

def getConnection():
	return pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=uda;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')

${API_ROUTES}

if __name__ == '__main__':
	app.run(debug=True)