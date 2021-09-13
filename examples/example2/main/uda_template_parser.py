import re
import os
from shutil import copyfile

def getApiTemplate(table,routeTemplateFileName):
    lines = open(routeTemplateFileName).read().split('\n')
    destLines=[]
    for line in lines:
        if line.find("${ROUTE_NAME}") > -1:
            line = line.replace("${ROUTE_NAME}",table["table"])
        if line.find("${ROUTE_UNIQUE}") > -1:
            line=line.replace("${ROUTE_UNIQUE}",table['key'])
        destLines.append(line)
    return destLines

def getMainApiTemplate(tables,mainTemplateFileName,routeTemplateFileName,dbType,connectionString):
    lines = open(mainTemplateFileName).read().split('\n')
    apis=[]
    for table in tables:
        apis.append("\n".join(getApiTemplate(table,routeTemplateFileName)))
    destLines=[]
    for line in lines:
        if line.find("${API_ROUTES}") > -1:
            line = line.replace("${API_ROUTES}","\n".join(apis))
        if line.find("${DB_TYPE}") > -1:
            line=line.replace("${DB_TYPE}",dbType)
        if line.find("${CONNECTION_STRING}") > -1:
            line=line.replace("${CONNECTION_STRING}",connectionString)
        destLines.append(line)
    return "\n".join(destLines)

def replaceJava(path,table):
    lines = open(path).read().split('\n')
    destLines=[]
    for line in lines:
        if line.find("${ROUTE_NAME}") > -1:
            line = line.replace("${ROUTE_NAME}",table["table"])
        if line.find("${ROUTE_NAME_CAPITALIZE}") > -1:
            line = line.replace("${ROUTE_NAME_CAPITALIZE}",table["table"].capitalize())
        if line.find("${PACKAGE}") > -1:
            line = line.replace("${PACKAGE}",os.getenv('PACKAGE'))
        if line.find("${ARTIFACT_NAME}") > -1:
            line=line.replace("${ARTIFACT_NAME}",os.getenv('ARTIFACT_NAME'))
        destLines.append(line)
    f = open(path, "w")
    f.write("\n".join(destLines))
    f.close()

def prepareJavaAPI(
    PACKAGE_DIRECTORY,
    POM_TEMPLATE_FILE_PATH,
    POM_API_FILE_PATH,
    MAIN_TEMPLATE_FILE_NAME,
    MAIN_API_FILE_NAME,
    ROUTE_TEMPLATE_FILE_NAME,
    ROUTE_API_FILE_NAME,
    tables):

    if not os.path.exists(PACKAGE_DIRECTORY):
        os.makedirs(PACKAGE_DIRECTORY)

    copyfile(POM_TEMPLATE_FILE_PATH, POM_API_FILE_PATH)
    copyfile(MAIN_TEMPLATE_FILE_NAME, MAIN_API_FILE_NAME)
    
    replaceJava(POM_API_FILE_PATH,{})
    replaceJava(MAIN_API_FILE_NAME,{})

    for table in tables:
        copyfile(ROUTE_TEMPLATE_FILE_NAME, ROUTE_API_FILE_NAME.replace("${ROUTE_NAME}",table["table"].capitalize()))
        replaceJava(ROUTE_API_FILE_NAME.replace("${ROUTE_NAME}",table["table"].capitalize()),table)
    