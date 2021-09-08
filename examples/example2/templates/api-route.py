@app.route("/${ROUTE_NAME}",methods = [${ROUTE_METHODS}])
def getAll():
	if request.method == 'GET':
		apiResponseMeta={"code":"CODE-XXXX","message":"default message"}
		apiResponseData={"${ROUTE_NAME}":[]}
		apiResponse={"meta":apiResponseMeta,"data":apiResponseData}
		conn = getConnection()
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
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute("insert into ${ROUTE_NAME}(%s) values (%s)"%(','.join(keys),','.join(values)))
		conn.commit()
		return apiResponse

	return apiResponse