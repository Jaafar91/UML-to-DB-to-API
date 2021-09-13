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
TARGET_API_LANGUAGE_EXTENSION=os.getenv('TARGET_API_LANGUAGE_EXTENSION')
DESIGN_FILE_NAME="..\\%s.plantuml"%(NAME)
DDL_FILE_NAME="..\\out\ddl\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
API_FILE_NAME="..\\out\\api\%s.%s"%("api",TARGET_API_LANGUAGE_EXTENSION)
DB_API_PATH="..\\out\\api\\api_database_connection.py"
MAIN_TEMPLATE_FILE_NAME="..\\templates\\%s\\api-main.py"%(TARGET_API_LANGUAGE_EXTENSION)
ROUTE_TEMPLATE_FILE_NAME="..\\templates\\\%s\api-route.py"%(TARGET_API_LANGUAGE_EXTENSION)
DB_TEMPLATE_FILE_NAME="..\\templates\\%s\\api_database_connection.py"%(TARGET_API_LANGUAGE_EXTENSION)

#print sql script
outputTables=readDesign(DESIGN_FILE_NAME,DDL_FILE_NAME)

#run the database script
createTables(DDL_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)

#copy database connection file
copyfile(DB_TEMPLATE_FILE_NAME, DB_API_PATH)

#create API
createApi(outputTables,API_FILE_NAME,MAIN_TEMPLATE_FILE_NAME,ROUTE_TEMPLATE_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)
