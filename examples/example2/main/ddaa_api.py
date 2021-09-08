def createApi(tableNames,apiFileName):
    api = defineFlask(tableNames);
    f = open(apiFileName, "w")
    f.write(api)
    f.close()

def defineFlask(tableNames):
    lines=[]
    lines.append("import pyodbc\nfrom flask import Flask\napp = Flask(__name__)\n")
    lines.append("def getConnection():")
    lines.append("\treturn pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=ddaa;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')\n")
    lines.append(getFromDdaa(tableNames))
    lines.append("if __name__ == '__main__':\n\tapp.run(debug=True)")
    return "\n".join(lines)

def getFromDdaa(tableNames):
    apis=[]
    for table in tableNames:
        lines =[]
        lines.append('@app.route("/%s")\ndef getAll():'%(table))
        lines.append('\tapiResponseMeta={"code":"CODE-XXXX","message":"default message"}')
        lines.append('\tapiResponseData={"%s":[]}'%(table))
        lines.append('\tapiResponse={"meta":apiResponseMeta,"data":apiResponseData}')
        lines.append("\tconn = getConnection()")
        lines.append("\tcursor = conn.cursor()")
        lines.append("\tcursor.execute('SELECT * FROM %s')"%(table))
        lines.append("\trows=[]")
        lines.append("\tcolumns = [column[0] for column in cursor.description]")
        lines.append("\tfor row in cursor.fetchall():")
        lines.append('\t\tapiResponse["data"]["%s"].append(dict(zip(columns, row)))'%(table))
        lines.append("\treturn apiResponse\n")
        apis.append("\n".join(lines))
    return "\n".join(apis)
