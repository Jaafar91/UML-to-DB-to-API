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
DDL_FILE_NAME="..\\out\\ddl\\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
API_FILE_NAME="..\\out\\api\\%s\\%s.%s"%(TARGET_API_LANGUAGE_EXTENSION,"api",TARGET_API_LANGUAGE_EXTENSION)

#print sql script
outputTables=readDesign(DESIGN_FILE_NAME,DDL_FILE_NAME)

#run the database script
createTables(DDL_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)

#PYTHON
if TARGET_API_LANGUAGE_EXTENSION == "py":
    DB_API_PATH="..\\out\\api\\%s\\api_database_connection.py"%(TARGET_API_LANGUAGE_EXTENSION)
    MAIN_TEMPLATE_FILE_NAME="..\\templates\\%s\\api-main.py"%(TARGET_API_LANGUAGE_EXTENSION)
    ROUTE_TEMPLATE_FILE_NAME="..\\templates\\%s\\api-route.py"%(TARGET_API_LANGUAGE_EXTENSION)
    DB_TEMPLATE_FILE_NAME="..\\templates\\%s\\api_database_connection.py"%(TARGET_API_LANGUAGE_EXTENSION)

    #copy database connection file
    copyfile(DB_TEMPLATE_FILE_NAME, DB_API_PATH)

    #create API
    createApi(outputTables,API_FILE_NAME,MAIN_TEMPLATE_FILE_NAME,ROUTE_TEMPLATE_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)

elif TARGET_API_LANGUAGE_EXTENSION == "java":
    PACKAGE_NAME=os.getenv('PACKAGE').replace('.','\\')
    POM_TEMPLATE_FILE_PATH="..\\templates\\%s\\pom.xml"%(TARGET_API_LANGUAGE_EXTENSION)
    POM_API_FILE_PATH="..\\out\\api\\%s\\pom.xml"%(TARGET_API_LANGUAGE_EXTENSION)

    PACKAGE_DIRECTORY="..\\out\\api\\%s\\src\\main\\java\\%s"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)
    
    MAIN_TEMPLATE_FILE_NAME="..\\templates\\%s\\Application.java"%(TARGET_API_LANGUAGE_EXTENSION)
    MAIN_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\Application.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)
    
    ROUTE_TEMPLATE_FILE_NAME="..\\templates\\%s\\HelloController.java"%(TARGET_API_LANGUAGE_EXTENSION)
    ROUTE_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\HelloController.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    if not os.path.exists(PACKAGE_DIRECTORY):
        os.makedirs(PACKAGE_DIRECTORY)
    
    copyfile(POM_TEMPLATE_FILE_PATH, POM_API_FILE_PATH)
    copyfile(MAIN_TEMPLATE_FILE_NAME, MAIN_API_FILE_NAME)
    copyfile(ROUTE_TEMPLATE_FILE_NAME, ROUTE_API_FILE_NAME)
    replaceJava(POM_API_FILE_PATH,{})
    replaceJava(MAIN_API_FILE_NAME,{})
    replaceJava(ROUTE_API_FILE_NAME,outputTables[0])

