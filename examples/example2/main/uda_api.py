from uda_template_parser import *

def createApi(tables,apiFileName,mainTemplateFileName,routeTemplateFileName,dbType,connectionString):
    api = getMainApiTemplate(tables,mainTemplateFileName,routeTemplateFileName,dbType,connectionString)
    f = open(apiFileName, "w")
    f.write(api)
    f.close()