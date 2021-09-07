import re
import pyodbc

NAME="example1"
TARGET_DB_LANGUAGE_EXTENSION='sql'
DESIGN_FILE_NAME="%s.plantuml"%(NAME)
DDL_FILE_NAME=".\\out\ddl\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
CREATE_TABLE="CREATE TABLE %s (\n%s\n);\n"

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
        ddls.append(CREATE_TABLE %(tableName,",\n".join(rows)))
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
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost,1475;'
                      'Database=ddaa;'
                      'UID=SA;'
                      'PWD=Abc@1234;'
                      'Trusted_Connection=no;')
    cursor = conn.cursor()
    cursor.execute(lines)
    conn.commit()
    conn.close()
    print("done")


scriptName = readDesign()

createTables(scriptName)
