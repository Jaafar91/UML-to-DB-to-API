import pyodbc

def getConnection(dbType,connectionString):
    if dbType == "SQL SERVER":
        return pyodbc.connect(connectionString)
    else:
        return 0
