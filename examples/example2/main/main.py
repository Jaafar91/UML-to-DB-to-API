import os
from dotenv import load_dotenv
from uda_uml_parser import *
from uda_database import *
from uda_api import *
from shutil import copyfile

load_dotenv()

NAME=os.getenv('PLANTUML_NAME')
DATABASE_TYPE=os.getenv('DATABASE_TYPE')
CONNECTION_STRING=os.getenv('CONNECTION_STRING')
TARGET_DB_LANGUAGE_EXTENSION='sql'
TARGET_APY_LANGUAGE_EXTENSION='py'
DESIGN_FILE_NAME="..\\%s.plantuml"%(NAME)
DDL_FILE_NAME="..\\out\ddl\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
API_FILE_NAME="..\\out\\api\%s.%s"%("api",TARGET_APY_LANGUAGE_EXTENSION)
DB_API_PATH="..\\out\\api\\api_database_connection.py"
MAIN_TEMPLATE_FILE_NAME="..\\templates\\api-main.py"
ROUTE_TEMPLATE_FILE_NAME="..\\templates\\api-route.py"
DB_TEMPLATE_FILE_NAME="..\\templates\\api_database_connection.py"

#print sql script
outputTables=readDesign(DESIGN_FILE_NAME,DDL_FILE_NAME)

#run the database script
createTables(DDL_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)

#copy database connection file
copyfile(DB_TEMPLATE_FILE_NAME, DB_API_PATH)

#create API
createApi(outputTables,API_FILE_NAME,MAIN_TEMPLATE_FILE_NAME,ROUTE_TEMPLATE_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)
