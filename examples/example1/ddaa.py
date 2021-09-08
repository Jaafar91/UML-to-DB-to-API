import re
import pyodbc

NAME="example1"
TARGET_DB_LANGUAGE_EXTENSION='sql'
TARGET_APY_LANGUAGE_EXTENSION='py'
DESIGN_FILE_NAME="%s.plantuml"%(NAME)
DDL_FILE_NAME=".\\out\ddl\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
API_FILE_NAME=".\\out\\api\%s.%s"%("api",TARGET_APY_LANGUAGE_EXTENSION)
TABLES_NAMES=[]

def readDesign():
    lines = open(DESIGN_FILE_NAME).read().split('\n')
    result =removeUnused(lines)
    indexes=countTables(result)
    allTables=parseTables(result,indexes)
    finalResult="\n".join(generateDDL(allTables))
    f = open(DDL_FILE_NAME, "w")
    f.write(finalResult)
    f.close()
    print(finalResult)
    return DDL_FILE_NAME

def generateDDL(allTables):
    ddls = []
    for table in allTables:    
        rows = []
        for line in table:
            row = ""
            if line.startswith("entity"):
                tableName=getTableName(line)
            elif line.startswith("}") == False:
                row = getColumn(replaceIndexes(line))
                rows.append(row)
        ddls.append(CREATE_TABLE %(tableName,tableName,",\n".join(rows)))
        TABLES_NAMES.append(tableName)
    print(TABLES_NAMES)
    return ddls
                
def getColumn(line):
    return line

def getTableName(line):
    tableName=line.replace("{","").replace("entity","").strip()
    return tableName

def countTables(lines):
    indexes=[]
    for x in range(len(lines)):
        if lines[x].startswith("entity"):
            indexes.append(x)
    return indexes

    
def parseTables(lines,indexes):
    allTables =[]
    for x in range(len(indexes)):
        table =[]
        for y in range(indexes[x],len(lines)):
            if(lines[y].startswith("}") or lines[y].endswith("}")):
                table.append(lines[y])
                break
            else:
                table.append(lines[y])
        allTables.append(table)
    return allTables

def removeUnused(uml):
    lines = []
    for line in uml:
        if isValid(line.strip()):
            lines.append(line.strip())
    return lines

def replaceIndexes(line):
    return re.sub(r'\[.*?\]|[\*]|[:]', ' ', line).strip()

def isValid(line):
    if(line.startswith('@')):
       return False
    elif(line.startswith('--')):
        return False
    elif(len(line) == 0):
        return False
    return True
    
def createTables(scriptName):
    lines = open(scriptName).read()
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(lines)
    conn.commit()
    conn.close()
    print("Database Done")

def defineFlask():
    lines=[]
    lines.append("import pyodbc\nfrom flask import Flask\napp = Flask(__name__)\n")
    lines.append("def getConnection():")
    lines.append("\treturn pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=ddaa;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')\n")
    lines.append(getFromDdaa())
    lines.append("if __name__ == '__main__':\n\tapp.run(debug=True)")
    return "\n".join(lines)

def getFromDdaa():
    apis=[]
    for table in TABLES_NAMES:
        lines =[]
        lines.append('@app.route("/%s")\ndef getAll():'%(table))
        lines.append("\tconn = getConnection()")
        lines.append("\tcursor = conn.cursor()")
        lines.append("\tcursor.execute('SELECT * FROM %s')"%(table))
        lines.append("\trows = []")
        lines.append("\tfor row in cursor.fetchall():")
        lines.append("\t\trows.append(row)")
        #lines.append("\treturn rows\n")
        lines.append("\treturn 'Number of rows:%s'%(len(rows))\n")
        apis.append("\n".join(lines))
    return "\n".join(apis)

def createApi():
    api = defineFlask();
    print(API_FILE_NAME)
    f = open(API_FILE_NAME, "w")
    f.write(api)
    f.close()
    print("API Done")

def getConnection():
    return pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=ddaa;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')


def readAll():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM %s"%("testers"))
    for row in cursor.fetchall():
        print(row)
        
scriptName = readDesign()
createTables(scriptName)
createApi()
readAll()
