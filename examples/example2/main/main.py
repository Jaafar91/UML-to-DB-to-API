from uda_uml_parser import *
from uda_database import *
from uda_api import *
from shutil import copyfile

NAME="example2"
#DATABASE_TYPE="SQL SERVER"
#CONNECTION_STRING='Driver={SQL Server};''Server=localhost,1475;''Database=uda;''UID=SA;''PWD=Abc@1234;''Trusted_Connection=no;'
DATABASE_TYPE="POSTGRES"
CONNECTION_STRING='DRIVER={PostgreSQL ODBC Driver(UNICODE)};''SERVER=localhost;''PORT=5433;''DATABASE=uda;''UID=postgres;''PWD=root;'
TARGET_DB_LANGUAGE_EXTENSION='sql'
TARGET_APY_LANGUAGE_EXTENSION='py'
DESIGN_FILE_NAME="..\\%s.plantuml"%(NAME)
DDL_FILE_NAME="..\\out\ddl\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
API_FILE_NAME="..\\out\\api\%s.%s"%("api",TARGET_APY_LANGUAGE_EXTENSION)
DB_API_PATH="..\\out\\api\\api_database_connection.py"
MAIN_TEMPLATE_FILE_NAME="..\\templates\\api-main.py"
ROUTE_TEMPLATE_FILE_NAME="..\\templates\\api-route.py"
DB_TEMPLATE_FILE_NAME="..\\templates\\api_database_connection.py"

print(pyodbc.drivers())
#print sql script
outputTables=readDesign(DESIGN_FILE_NAME,DDL_FILE_NAME)

#run the database script
createTables(DDL_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)

#copy database connection file
copyfile(DB_TEMPLATE_FILE_NAME, DB_API_PATH)

#create API
createApi(outputTables,API_FILE_NAME,MAIN_TEMPLATE_FILE_NAME,ROUTE_TEMPLATE_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)
