from ddaa_template_parser import *

def createApi(tableNames,apiFileName,templateFileName,methods):
    api = defineFlask(tableNames,templateFileName,methods);
    f = open(apiFileName, "w")
    f.write(api)
    f.close()

def defineFlask(tableNames,templateFileName,methods):
    lines=[]
    lines.append("import pyodbc\nfrom flask import Flask,request\napp = Flask(__name__)\n")
    lines.append("def getConnection():")
    lines.append("\treturn pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=ddaa;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')\n")
    lines.append(getFromDdaa(tableNames,templateFileName,methods))
    lines.append("if __name__ == '__main__':\n\tapp.run(debug=True)")
    return "\n".join(lines)

def getFromDdaa(tableNames,templateFileName,methods):
    apis=[]
    for table in tableNames:
        for i in range(0):
            if x == 0:
                lines =[]
                lines.append('@app.route("/%s",methods = ["GET", "POST"])\ndef getAll():'%(table))
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
        apis.append("\n".join(getApiTemplate(templateFileName,table,methods)))
    return "\n".join(apis)
