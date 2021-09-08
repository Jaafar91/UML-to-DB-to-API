import re

def getApiTemplate(templateFileName,tableName,methods):
    lines = open(templateFileName).read().split('\n')
    destLines=[]
    for line in lines:
        if line.find("${ROUTE_NAME}") > -1:
            line = line.replace("${ROUTE_NAME}",tableName)
        if line.find("${ROUTE_METHODS}") > -1:
            line=line.replace("${ROUTE_METHODS}",methods)
        destLines.append(line)
    return destLines
