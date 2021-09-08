import re

def getApiTemplate(templateFileName,table,methods):
    lines = open(templateFileName).read().split('\n')
    destLines=[]
    for line in lines:
        if line.find("${ROUTE_NAME}") > -1:
            line = line.replace("${ROUTE_NAME}",table["table"])
        if line.find("${ROUTE_METHODS}") > -1:
            line=line.replace("${ROUTE_METHODS}",methods)
        destLines.append(line)
    return destLines
