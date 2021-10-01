import re

CREATE_TABLE="DROP TABLE IF EXISTS %s;\nCREATE TABLE %s (\n%s\n);\n"
TABLES_NAMES=[]

def readDesign(designFileName,ddlFileName):
    lines = open(designFileName).read().split('\n')
    #print("\n\nlines:"+"\n".join(lines))
    result =removeUnused(lines)
    #print("\n\nresult:"+"\n".join(result))
    indexes=countTables(result)
    allTables=parseTables(result,indexes)
    #print(allTables)
    finalResult="\n".join(generateDDL(allTables))
    #print(finalResult)
    f = open(ddlFileName, "w")
    f.write(finalResult)
    f.close()
    return TABLES_NAMES

def removeUnused(uml):
    lines = []
    for line in uml:
        if isValid(line.strip()):
            lines.append(line.strip())
    return lines

def isValid(line):
    if(line.startswith('@')):
       return False
    elif(line.startswith('--')):
        return False
    elif(len(line) == 0):
        return False
    return True

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

def generateDDL(allTables):
    ddls = []
    for table in allTables:    
        rows = []
        cols=[]
        
        key = ''
        for line in table:
            col={}
            row = ""
            if line.startswith("entity"):
                tableName=getTableName(line)
            elif line.startswith("*") and line.startswith("**") == False:
                row = replaceIndexes(line)
                rows.append(row+" NOT NULL PRIMARY KEY")
                col["name"]=row.split(' ')[0]
                col["dataType"]= row.split(' ')[len(row.split(' '))-1]
                cols.append(col)
                key=col["name"]
            elif line.startswith("}") == False:
                row = replaceIndexes(line)
                rows.append(row)
                col["name"]=row.split(' ')[0]
                col["dataType"]= row.split(' ')[len(row.split(' '))-1]
                if line.startswith("**"):
                    col["FK"]= True 
                else: 
                    col["FK"]= False 
                cols.append(col)

        
        ddls.append(CREATE_TABLE %(tableName,tableName,",\n".join(rows)))
        TABLES_NAMES.append({'table':tableName,'cols':cols,'key':key})
    
    fk=[]
    for table in TABLES_NAMES:
        for col in table["cols"]:
            if "FK" in col and col["FK"] == True:
                stmt="ALTER TABLE %s ADD CONSTRAINT fk_%s_%s FOREIGN KEY(%s) REFERENCES %s(%s);"%(table["table"],table["table"],col["name"],col["name"],getParentTableName(col["name"]),getParentTableNameColumn(col["name"]))
                fk.append(stmt)
    ddls.append("\n".join(fk))
    return ddls

def getParentTableName(fk):
    for table in TABLES_NAMES:
        if fk.startswith(table["table"]):
            return fk[:len(table["table"])]

def getParentTableNameColumn(fk):
    for table in TABLES_NAMES:
        if fk.startswith(table["table"]):
            for col in table["cols"]:
                if col["name"] == fk[len(table["table"])+1:]:
                    return fk[len(table["table"])+1:]

def getTableName(line):
    tableName=line.replace("{","").replace("entity","").strip()
    return tableName

def replaceIndexes(line):
    return re.sub(r'\[.*?\]|[\*]|[:]', ' ', line).strip()
