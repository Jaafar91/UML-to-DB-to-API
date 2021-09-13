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
- It parses UML file, generates sql script, run the generated script, and create API using Flask
- The inputs:
    - Valid SQL Server Database connection
    - Running Database
    - Valid plantuml that has one or more table
    - UDA Scripts
- The output:
    - Sql script
    - API code that can be run and consumed by any API client, e.g Postman

# Useful Paths
- The connection string can be changed from the .env file `examples/example2/main/.env`
- The docker folder has ready image to run SQL Server that matches the connection string

# UML file
- Each table should start with word `enitity`
- The format of each column is `column_name: data type`
- The primary key column name starts with `*`
- The primary key column should be the first line and followed by `--` line
- example
```
 entity user{
  *id : int
  --
  first_name :   varchar(100)
  last_name :    varchar(100)
  date_of_birth: date
}
```

# Python Libraries
- pyodbc library 

    > pip install pyodbc

    > pip install python-dotenv

# Run the API
- Navigate to python path or add the python path to the environment variables and run this command  
    
    > python "..\examples\example1\out\api\api.py"

# Run MSSQL Docker
- NAvigate to MSSQL folder from your command line `..\docker\MSSQL`
- Run docker-compose build

    > docker-compose build
    
    > docker-compose up

- Somtimes it does not work with the above commands and will require to do it start it manually by executing this command:

    > docker exec -it <containerName> "bash"

- Then run the commands inside the `..\docker\MSSQL\config\setup.sh`