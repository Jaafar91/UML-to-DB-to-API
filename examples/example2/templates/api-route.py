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
		return "test"

	return apiResponse