from uda_uml_parser import *
from uda_database import *
from uda_api import *

NAME="example2"
TARGET_DB_LANGUAGE_EXTENSION='sql'
TARGET_APY_LANGUAGE_EXTENSION='py'
DESIGN_FILE_NAME="..\\%s.plantuml"%(NAME)
DDL_FILE_NAME="..\\out\ddl\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
API_FILE_NAME="..\\out\\api\%s.%s"%("api",TARGET_APY_LANGUAGE_EXTENSION)
MAIN_TEMPLATE_FILE_NAME="..\\templates\\api-main.py"
ROUTE_TEMPLATE_FILE_NAME="..\\templates\\api-route.py"

#print sql script
outputTables=readDesign(DESIGN_FILE_NAME,DDL_FILE_NAME)

#run the database script
createTables(DDL_FILE_NAME)

#create API
createApi(outputTables,API_FILE_NAME,MAIN_TEMPLATE_FILE_NAME,ROUTE_TEMPLATE_FILE_NAME)
