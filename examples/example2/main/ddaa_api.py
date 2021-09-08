from ddaa_template_parser import *

def createApi(tables,apiFileName,templateFileName,methods):
    api = defineFlask(tables,templateFileName,methods);
    f = open(apiFileName, "w")
    f.write(api)
    f.close()

def defineFlask(tables,templateFileName,methods):
    lines=[]
    lines.append("import json\nimport pyodbc\nfrom flask import Flask,request\napp = Flask(__name__)\n")
    lines.append("def getConnection():")
    lines.append("\treturn pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=ddaa;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')\n")
    lines.append(getFromDdaa(tables,templateFileName,methods))
    lines.append("if __name__ == '__main__':\n\tapp.run(debug=True)")
    return "\n".join(lines)

def getFromDdaa(tables,templateFileName,methods):
    apis=[]
    for table in tables:
        apis.append("\n".join(getApiTemplate(templateFileName,table,methods)))
    return "\n".join(apis)
