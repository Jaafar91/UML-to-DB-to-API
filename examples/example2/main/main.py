import os
from dotenv import load_dotenv
from uda_uml_parser import *
from uda_database import *
from uda_api import *
from uda_postman_parser import *
from shutil import copyfile
import settings

load_dotenv()
settings.init()

NAME=os.getenv('PLANTUML_NAME')
OUTPUT_FOLDER=os.getenv('OUTPUT_FOLDER')
DATABASE_TYPE=os.getenv('DATABASE_TYPE')
CONNECTION_STRING=os.getenv('CONNECTION_STRING')
TARGET_DB_LANGUAGE_EXTENSION='sql'
TARGET_API_LANGUAGE_EXTENSION=os.getenv('TARGET_API_LANGUAGE_EXTENSION')
DESIGN_FILE_NAME="..\\%s.plantuml"%(NAME)
DDL_FILE_NAME="..\\out\\ddl\\%s.%s"%(NAME,TARGET_DB_LANGUAGE_EXTENSION)
API_FILE_NAME="..\\out\\api\\%s\\%s\\%s.%s"%(TARGET_API_LANGUAGE_EXTENSION,OUTPUT_FOLDER,"api",TARGET_API_LANGUAGE_EXTENSION)
BASE_TEMPLATE="..\\templates\\%s\\"%(TARGET_API_LANGUAGE_EXTENSION)
POSTMAN_TEMPLATE="..\\templates\\postman\\postman_collection.json"
OUT_POSTMAN_TEMPLATE="..\\out\\postman\\"

#print sql script
outputTables=readDesign(DESIGN_FILE_NAME,DDL_FILE_NAME)

#run the database script
createTables(DDL_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)

#PYTHON
if TARGET_API_LANGUAGE_EXTENSION == "py":
    BASE_OUTPUT="..\\out\\api\\%s\\%s"%(TARGET_API_LANGUAGE_EXTENSION,OUTPUT_FOLDER)
    DB_API_PATH=BASE_OUTPUT+"\\api_database_connection.py"
    MAIN_TEMPLATE_FILE_NAME="..\\templates\\%s\\api-main.py"%(TARGET_API_LANGUAGE_EXTENSION)
    ROUTE_TEMPLATE_FILE_NAME="..\\templates\\%s\\api-route.py"%(TARGET_API_LANGUAGE_EXTENSION)
    DB_TEMPLATE_FILE_NAME="..\\templates\\%s\\api_database_connection.py"%(TARGET_API_LANGUAGE_EXTENSION)

    if not os.path.exists(BASE_OUTPUT):
        os.makedirs(BASE_OUTPUT)

    #copy database connection file
    copyfile(DB_TEMPLATE_FILE_NAME, DB_API_PATH)

    #create API
    createApi(outputTables,API_FILE_NAME,MAIN_TEMPLATE_FILE_NAME,ROUTE_TEMPLATE_FILE_NAME,DATABASE_TYPE,CONNECTION_STRING)

elif TARGET_API_LANGUAGE_EXTENSION == "java":
    PACKAGE_NAME=os.getenv('PACKAGE').replace('.','\\')
    #BASE_API="..\\out\\api\\%s\\%s\\src\\main\\"%(TARGET_API_LANGUAGE_EXTENSION,OUTPUT_FOLDER)
    BASE_API="..\\out\\api\\%s\\%s\\"%(TARGET_API_LANGUAGE_EXTENSION,OUTPUT_FOLDER)
    
    POM_TEMPLATE_FILE_PATH=BASE_TEMPLATE+"pom.xml"
    POM_API_FILE_PATH=BASE_API+"pom.xml"

    PACKAGE_DIRECTORY=BASE_API+"src\\main\\java\\%s"%(PACKAGE_NAME)
    RESOURCE_DIRECTORY=BASE_API+"src\\main\\resources"

    YAML_TEMPLATE_FILE_PATH=BASE_TEMPLATE+"application.yaml"
    YAML_API_FILE_PATH=RESOURCE_DIRECTORY+"\\application.yaml"
    
    MAIN_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Application.java"
    MAIN_API_FILE_NAME=PACKAGE_DIRECTORY+"\\Application.java"
    
    CONFIG_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"DBConfig.java"
    CONFIG_API_FILE_NAME=PACKAGE_DIRECTORY+"\\config\\DBConfig.java"
    
    ROUTE_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"RouteController.java"
    ROUTE_API_FILE_NAME=PACKAGE_DIRECTORY+"\\controller\\${ROUTE_NAME}Controller.java"

    SERVICE_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Service.java"
    SERVICE_API_FILE_NAME=PACKAGE_DIRECTORY+"\\service\\${SINGLE_ROUTE_NAME_CAPITALIZE}Service.java"

    ENITITY_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Entity.java"
    ENITITY_API_FILE_NAME=PACKAGE_DIRECTORY+"\\entity\\${SINGLE_ROUTE_NAME_CAPITALIZE}Entity.java"

    MAPPER_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Mapper.java"
    MAPPER_API_FILE_NAME=PACKAGE_DIRECTORY+"\\mapper\\${SINGLE_ROUTE_NAME_CAPITALIZE}Mapper.java"
    
    MODEL_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Model.java"
    MODEL_API_FILE_NAME=PACKAGE_DIRECTORY+"\\model\\${SINGLE_ROUTE_NAME_CAPITALIZE}.java"

    REPO_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Repository.java"
    REPO_API_FILE_NAME=PACKAGE_DIRECTORY+"\\repository\\${SINGLE_ROUTE_NAME_CAPITALIZE}Repository.java"

    META_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Meta.java"
    META_API_FILE_NAME=PACKAGE_DIRECTORY+"\\model\\Meta.java"

    DATA_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"Data.java"
    DATA_API_FILE_NAME=PACKAGE_DIRECTORY+"\\model\\${SINGLE_ROUTE_NAME_CAPITALIZE}Data.java"

    GEN_RESPONSE_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"GenericResponse.java"
    GEN_RESPONSE_API_FILE_NAME=PACKAGE_DIRECTORY+"\\model\\GenericResponse.java"

    RESPONSE_MAPPER_TEMPLATE_FILE_NAME=BASE_TEMPLATE+"GenericResponseMapper.java"
    RESPONSE_MAPPER_API_FILE_NAME=PACKAGE_DIRECTORY+"\\mapper\\GenericResponseMapper.java"
    
    obj = {
    "pom":{"template":POM_TEMPLATE_FILE_PATH,"target":POM_API_FILE_PATH},
    "yaml":{"template":YAML_TEMPLATE_FILE_PATH,"target":YAML_API_FILE_PATH},
    "package": PACKAGE_DIRECTORY,
    "resources": RESOURCE_DIRECTORY,
    "application": {"template":MAIN_TEMPLATE_FILE_NAME,"target":MAIN_API_FILE_NAME},
    "config": {"template":CONFIG_TEMPLATE_FILE_NAME,"target":CONFIG_API_FILE_NAME},
    "controller":{"template":ROUTE_TEMPLATE_FILE_NAME,"target":ROUTE_API_FILE_NAME},
    "service": {"template":SERVICE_TEMPLATE_FILE_NAME,"target":SERVICE_API_FILE_NAME},
    "entity": {"template":ENITITY_TEMPLATE_FILE_NAME,"target":ENITITY_API_FILE_NAME},
    "model": {"template":MODEL_TEMPLATE_FILE_NAME,"target":MODEL_API_FILE_NAME},
    "mapper": {"template":MAPPER_TEMPLATE_FILE_NAME,"target":MAPPER_API_FILE_NAME},
    "repository": {"template":REPO_TEMPLATE_FILE_NAME,"target":REPO_API_FILE_NAME},
    "meta": {"template":META_TEMPLATE_FILE_NAME,"target":META_API_FILE_NAME},
    "data": {"template":DATA_TEMPLATE_FILE_NAME,"target":DATA_API_FILE_NAME},
    "genericResponse": {"template":GEN_RESPONSE_TEMPLATE_FILE_NAME,"target":GEN_RESPONSE_API_FILE_NAME},
    "responseMapper": {"template":RESPONSE_MAPPER_TEMPLATE_FILE_NAME,"target":RESPONSE_MAPPER_API_FILE_NAME}
    }
    prepareJavaAPI(obj,outputTables)

#Create Postman
for table in outputTables:
    copyfile(POSTMAN_TEMPLATE, OUT_POSTMAN_TEMPLATE+table["table"]+".json")
    replaceJava(OUT_POSTMAN_TEMPLATE+table["table"]+".json",table)