import pyodbc

def getConnection(dbType,connectionString):
    if dbType == "SQL SERVER" or dbType == "POSTGRES":
        return pyodbc.connect(connectionString)
    else:
        return 0
