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
        if line.find("${SINGLE_ROUTE_NAME_CAPITALIZE}") > -1:
            line = line.replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize())
        if line.find("${SINGLE_ROUTE_NAME}") > -1:
            line = line.replace("${SINGLE_ROUTE_NAME}",table["table"])
        if line.find("${ROUTE_NAME_CAPITALIZE}") > -1:
            line = line.replace("${ROUTE_NAME_CAPITALIZE}",table["table"].capitalize())
        if line.find("${PACKAGE}") > -1:
            line = line.replace("${PACKAGE}",os.getenv('PACKAGE'))
        if line.find("${ARTIFACT_NAME}") > -1:
            line=line.replace("${ARTIFACT_NAME}",os.getenv('ARTIFACT_NAME'))
        if line.find("${ENTITY_ID}") > -1:
            line=line.replace("${ENTITY_ID}","private int %s;"%(table["key"]))
        if line.find("${ENTITY_OTHER_COLUMNS}") > -1:
            entityLines=[]
            for col in table['cols']:
                if col["name"] != table["key"]:
                    entityLines.append("private %s %s;"%(convertDatabaseDataTypeToJaveDateType(col["dataType"]),col["name"]))
            
            line=line.replace("${ENTITY_OTHER_COLUMNS}","\n\n\t".join(entityLines))    
        if line.find("${MODEL_COLUMNS}") > -1:
            modelLines=[]
            for col in table['cols']:
                modelLines.append("private %s %s;"%(convertDatabaseDataTypeToJaveDateType(col["dataType"]),col["name"]))
            
            line=line.replace("${MODEL_COLUMNS}","\n\n\t".join(modelLines))    
        if line.find("${MAPPER_BODY}") > -1:
            mapperLines=[]
            for col in table['cols']:
                mapperLines.append(".%s(%sEntity.get%s())"%(col["name"],table["table"],col["name"].capitalize()))
            
            line=line.replace("${MAPPER_BODY}","\n\t\t\t\t".join(mapperLines))    
            
        destLines.append(line)
    f = open(path, "w")
    f.write("\n".join(destLines))
    f.close()

def convertDatabaseDataTypeToJaveDateType(dataType):
    if dataType.upper().startswith("VARCHAR"):
        return "String"
    elif dataType.upper().startswith("DATE"):
        return "Date"
    elif dataType.upper() == ("INT"):
        return "int"

def prepareJavaAPI(
    config,
    tables):

    if not os.path.exists(config["package"]+"//controller"):
        os.makedirs(config["package"]+"//controller")
    if not os.path.exists(config["package"]+"//config"):
        os.makedirs(config["package"]+"//config")
    if not os.path.exists(config["package"]+"//model"):
        os.makedirs(config["package"]+"//model")    
    if not os.path.exists(config["package"]+"//mapper"):
        os.makedirs(config["package"]+"//mapper")
    if not os.path.exists(config["package"]+"//entity"):
        os.makedirs(config["package"]+"//entity")
    if not os.path.exists(config["package"]+"//repository"):
        os.makedirs(config["package"]+"//repository")    
    if not os.path.exists(config["package"]+"//service"):
        os.makedirs(config["package"]+"//service")
    if not os.path.exists(config["package"]+"//config"):
        os.makedirs(config["package"]+"//config")    

    copyfile(config["pom"]["template"], config["pom"]["target"])
    copyfile(config["application"]["template"], config["application"]["target"])
    
    replaceJava(config["pom"]["target"],{})
    replaceJava(config["application"]["target"],{})

    for table in tables:
        copyfile(config["controller"]["template"], config["controller"]["target"].replace("${ROUTE_NAME}",table["table"].capitalize()))
        replaceJava(config["controller"]["target"].replace("${ROUTE_NAME}",table["table"].capitalize()),table)
        
        copyfile(config["service"]["template"], config["service"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()))
        replaceJava(config["service"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()),table)
        
        copyfile(config["model"]["template"], config["model"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()))
        replaceJava(config["model"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()),table)

        copyfile(config["entity"]["template"], config["entity"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()))
        replaceJava(config["entity"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()),table)

        copyfile(config["repository"]["template"], config["repository"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()))
        replaceJava(config["repository"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()),table)

        copyfile(config["mapper"]["template"], config["mapper"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()))
        replaceJava(config["mapper"]["target"].replace("${SINGLE_ROUTE_NAME_CAPITALIZE}",table["table"].capitalize()),table)

        copyfile(config["config"]["template"], config["config"]["target"].replace("${ROUTE_NAME}",table["table"].capitalize()))
        replaceJava(config["config"]["target"].replace("${ROUTE_NAME}",table["table"].capitalize()),table)
    