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

    YAML_TEMPLATE_FILE_PATH="..\\templates\\%s\\application.yaml"%(TARGET_API_LANGUAGE_EXTENSION)
    YAML_API_FILE_PATH="..\\out\\api\\%s\\src\\main\\resources\\application.yaml"%(TARGET_API_LANGUAGE_EXTENSION)

    PACKAGE_DIRECTORY="..\\out\\api\\%s\\src\\main\\java\\%s"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)
    RESOURCE_DIRECTORY="..\\out\\api\\%s\\src\\main\\resources"%(TARGET_API_LANGUAGE_EXTENSION)
    
    MAIN_TEMPLATE_FILE_NAME="..\\templates\\%s\\Application.java"%(TARGET_API_LANGUAGE_EXTENSION)
    MAIN_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\Application.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)
    
    CONFIG_TEMPLATE_FILE_NAME="..\\templates\\%s\\DBConfig.java"%(TARGET_API_LANGUAGE_EXTENSION)
    CONFIG_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\config\\DBConfig.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)
    
    ROUTE_TEMPLATE_FILE_NAME="..\\templates\\%s\\RouteController.java"%(TARGET_API_LANGUAGE_EXTENSION)
    ROUTE_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\controller\\${ROUTE_NAME}Controller.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    SERVICE_TEMPLATE_FILE_NAME="..\\templates\\%s\\Service.java"%(TARGET_API_LANGUAGE_EXTENSION)
    SERVICE_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\service\\${SINGLE_ROUTE_NAME_CAPITALIZE}Service.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    ENITITY_TEMPLATE_FILE_NAME="..\\templates\\%s\\Entity.java"%(TARGET_API_LANGUAGE_EXTENSION)
    ENITITY_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\entity\\${SINGLE_ROUTE_NAME_CAPITALIZE}Entity.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    MAPPER_TEMPLATE_FILE_NAME="..\\templates\\%s\\Mapper.java"%(TARGET_API_LANGUAGE_EXTENSION)
    MAPPER_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\mapper\\${SINGLE_ROUTE_NAME_CAPITALIZE}Mapper.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)
    
    MODEL_TEMPLATE_FILE_NAME="..\\templates\\%s\\Model.java"%(TARGET_API_LANGUAGE_EXTENSION)
    MODEL_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\model\\${SINGLE_ROUTE_NAME_CAPITALIZE}.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    REPO_TEMPLATE_FILE_NAME="..\\templates\\%s\\Repository.java"%(TARGET_API_LANGUAGE_EXTENSION)
    REPO_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\repository\\${SINGLE_ROUTE_NAME_CAPITALIZE}Repository.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    META_TEMPLATE_FILE_NAME="..\\templates\\%s\\Meta.java"%(TARGET_API_LANGUAGE_EXTENSION)
    META_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\model\\Meta.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    DATA_TEMPLATE_FILE_NAME="..\\templates\\%s\\Data.java"%(TARGET_API_LANGUAGE_EXTENSION)
    DATA_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\model\\${SINGLE_ROUTE_NAME_CAPITALIZE}Data.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    GEN_RESPONSE_TEMPLATE_FILE_NAME="..\\templates\\%s\\GenericResponse.java"%(TARGET_API_LANGUAGE_EXTENSION)
    GEN_RESPONSE_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\model\\GenericResponse.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)

    RESPONSE_MAPPER_TEMPLATE_FILE_NAME="..\\templates\\%s\\GenericResponseMapper.java"%(TARGET_API_LANGUAGE_EXTENSION)
    RESPONSE_MAPPER_API_FILE_NAME="..\\out\\api\\%s\\src\\main\\java\\%s\\mapper\\GenericResponseMapper.java"%(TARGET_API_LANGUAGE_EXTENSION,PACKAGE_NAME)
    
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
    prepareJavaAPI(
        obj,
        outputTables,
    )
