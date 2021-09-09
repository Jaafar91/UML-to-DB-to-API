import re

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

def getMainApiTemplate(tables,mainTemplateFileName,routeTemplateFileName):
    lines = open(mainTemplateFileName).read().split('\n')
    apis=[]
    for table in tables:
        apis.append("\n".join(getApiTemplate(table,routeTemplateFileName)))
    destLines=[]
    for line in lines:
        if line.find("${API_ROUTES}") > -1:
            line = line.replace("${API_ROUTES}","\n".join(apis))
        destLines.append(line)
    return "\n".join(destLines)