@app.route("/${ROUTE_NAME}",methods = ['GET','POST'])
def ${ROUTE_NAME}_getAll():
	if request.method == 'GET':
		apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
		apiResponseData={"${ROUTE_NAME}":[]}
		apiResponse={"meta":apiResponseMeta,"data":apiResponseData}
		conn = getConnection(DatabaseType,ConnectionString)
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM ${ROUTE_NAME}')
		rows=[]
		columns = [column[0] for column in cursor.description]
		for row in cursor.fetchall():
			apiResponse["data"]["${ROUTE_NAME}"].append(dict(zip(columns, row)))
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
		cursor.execute("insert into ${ROUTE_NAME}(%s) values (%s)"%(','.join(keys),','.join(values)))
		conn.commit()
		return apiResponse

	return apiResponse

@app.route("/${ROUTE_NAME}/<${ROUTE_UNIQUE}>",methods = ['GET'])
def ${ROUTE_NAME}_getOne(${ROUTE_UNIQUE}):
	
	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta,"data":{}}
	conn = getConnection(DatabaseType,ConnectionString)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM ${ROUTE_NAME} WHERE ${ROUTE_UNIQUE} = '%s'"%(${ROUTE_UNIQUE}))
	rows=[]
	columns = [column[0] for column in cursor.description]
	for row in cursor.fetchall():
		apiResponse["data"]=dict(zip(columns, row))
	
	return apiResponse

@app.route("/${ROUTE_NAME}/<${ROUTE_UNIQUE}>",methods = ['DELETE'])
def ${ROUTE_NAME}_deleteOne(${ROUTE_UNIQUE}):

	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta}
	conn = getConnection(DatabaseType,ConnectionString)
	cursor = conn.cursor()
	cursor.execute("DELETE FROM ${ROUTE_NAME} WHERE ${ROUTE_UNIQUE} = '%s'"%(${ROUTE_UNIQUE}))
	conn.commit()

	return apiResponse

@app.route("/${ROUTE_NAME}/<${ROUTE_UNIQUE}>",methods = ['PUT'])
def ${ROUTE_NAME}_updateOne(${ROUTE_UNIQUE}):

	apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
	apiResponse={"meta":apiResponseMeta}
	req = request.get_json()
	itemsToBeUpdated=[]
	for item in req:
		itemsToBeUpdated.append(item+"="+"'"+str(req[item])+"'")
	print(",".join(itemsToBeUpdated))
	conn = getConnection(DatabaseType,ConnectionString)
	cursor = conn.cursor()
	cursor.execute("UPDATE ${ROUTE_NAME} SET %s WHERE ${ROUTE_UNIQUE} = '%s'"%(",".join(itemsToBeUpdated),${ROUTE_UNIQUE}))
	conn.commit()

	return apiResponse