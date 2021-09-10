import pyodbc

def createTables(scriptName,dbType,connectionString):
    lines = open(scriptName).read()
    conn = getConnection(dbType,connectionString)
    cursor = conn.cursor()
    cursor.execute(lines)
    conn.commit()
    conn.close()

def getConnection(dbType,connectionString):
    if dbType == "SQL SERVER":
        return pyodbc.connect(connectionString)
    else:
        return 0