# UDA
UML Database API

# Purpose
The purpose of this project is to create an automation way for users to create APIs from UML.

# POC
In initital phase, my target is running a python script that creates a running application from UML design, and this application connects to API & DB

# Phase 1
- Create UML
- Generate DDL Script from UML in MSSQL
- Create API from a DB using python (FLASK)

 # Phase 2
 - Enhance the UML functionalities
 - Add more Database Management System
 - Create API for more programming languages 

 # How it works
    * It parses UML file, generates sql script, run the generated script, and create API using Flask
    * The inputs:
        * Valid SQL Server Database connection
        * Running Database
        * Valid plantuml that has one or more table
        * UDA Scripts
    The output:
        * Sql script
        * API code that can be run and consumed by any API client, e.g Postman

# Useful Paths
- The connection string can be changed from the main file 'examples/example2/main/main.py'
- The docker folder has ready image to run SQL Server that matches the connection string

