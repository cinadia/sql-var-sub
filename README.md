# SQL Variable Substitution Script

## Description
Takes a .sql file, replaces variables specified, and executes file against the database given via the engine URL. 

The following strings are replaceable if included in the .sql file:
- $DB_NAME' by the given database name
- '$ROLE' by the given role
- '$PASSWORD' by the given password

## Running (Windows)
cd into `src` directory

`py replace_and_parse.py var-replace --filename=provided_filename.sql --ENGINE_URL=provided_url --DB_NAME=provided_name --ROLE=provided_role --PASSWORD=provided_password`

## Docs
`filename`: required; the name of the file

`ENGINE_URL`: required; the URL of the database to connect to 

`DB_NAME`: not required; the database name to replace in the file; default: DB

`ROLE`: not required; the role to replace in the file; default: postgres

`PASSWORD`: not required; the password to replace in the file
 
 ## Robustness
 Currently checks/accounts for:
 - empty files
 - comments
 - failed connections to the database (which could arise from failed queries)
 
 ## Future Tests to Implement
 - valid filename and parameters
 - correct SQL syntax, to distinguish failed query executions between failed queries or failed connections to the database
 - multiple SQL statements in the same line (ie without \n)
