import json
import pyodbc
from flask import Flask,request
from api_database_connection import *
app = Flask(__name__)

DatabaseType='${DB_TYPE}'
ConnectionString='${CONNECTION_STRING}'

${API_ROUTES}

if __name__ == '__main__':
	app.run(debug=True)