UML

- Each table should start with word "enitity"
- The format of each column is "column_name: data type"
- The primary key column name starts with *
- The primary key column should be the first line and followed by "--" line
- example
entity user{
  *id : int
  --
  first_name :   varchar(100)
  last_name :    varchar(100)
  date_of_birth: date
}

- Database Connection
- pyodbc library
- Run "pip install pyodbc"

- To run the api.py
- Navigate to python path or add the python path to the environment variables and run this command
python "...\DDAA\examples\example1\out\api\api.py"