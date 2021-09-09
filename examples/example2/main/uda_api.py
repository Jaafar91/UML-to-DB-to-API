from uda_template_parser import *

def createApi(tables,apiFileName,mainTemplateFileName,routeTemplateFileName):
    api = defineFlask(tables,mainTemplateFileName,routeTemplateFileName);
    f = open(apiFileName, "w")
    f.write(api)
    f.close()

def defineFlask(tables,mainTemplateFileName,routeTemplateFileName):
    return getMainApiTemplate(tables,mainTemplateFileName,routeTemplateFileName)
