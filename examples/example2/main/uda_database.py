import pyodbc

def createTables(scriptName):
    lines = open(scriptName).read()
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(lines)
    conn.commit()
    conn.close()

def getConnection():
    return pyodbc.connect('Driver={SQL Server};''Server=localhost,1475;''Database=uda;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;')
