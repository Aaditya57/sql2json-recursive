import yaml
import json
from datetime import datetime
from decimal import Decimal
import re
import db_Connection1 as dbconn

log = dbconn.getLogger() 
class CustomJSONEncoder(json.JSONEncoder):
    """ Custom JSON Encoder that converts datetime objects to strings. """
    def default(self, obj):
        if isinstance(obj, datetime):
            # Format datetime object as a string in ISO format
            return obj.isoformat()
        elif isinstance(obj, set):
            return list(obj)  # Convert set to list
        elif isinstance(obj , Decimal):
            return int(obj)
        return json.JSONEncoder.default(self, obj)


def row_to_dict(row, cursor_description):
    """ Convert a pyodbc.Row object to a dictionary. """
    return {cursor_description[i][0]: value for i, value in enumerate(row)}


def row_to_name_value_pairs(row, cursor_description):
    """ Convert a row to a list of name-value pairs. """
    row_dict = row_to_dict(row, cursor_description)
    return [{key: value} for key, value in row_dict.items()]


def get_json_from_query( query , connection ):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print( rows ) 
        cursor_description = cursor.description
        print( cursor_description )
        results = [row_to_name_value_pairs(row, cursor_description) for row in rows]
        print( results )
        return results     

def getString(results, row, col_name):
    try:
        return results[row][col_name]
    except (IndexError, KeyError):
        return None  # Or handle the error as you prefer

def executeQuery( sql_query ): 
    # Execute the query and store results in a list of dictionaries
    dbconn.log(f'executing : {sql_query}')
    connection = dbconn.getMySQLConnection()
    cursor = connection.cursor() 
    cursor.execute(sql_query)
    columns = [col[0] for col in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor = None
    return results 


# Function to replace variables in the query
def replace_variables(text, var_dict):
    # Replace each variable with its value
    if var_dict == None:
        return text 
    for var, value in var_dict.items():
        value = str( value ) 
        text = re.sub(r'\$' + var, value, text)
    return text


json1 = {} 

    
def list_to_dict(lst):
    result = {}
    for item in lst:
        if 'name' in item and 'text' in item:
            result[item['name']] = item['text']
        elif 'query' in item:
            result.update(list_to_dict(item['query']))
    return result   
       


def execute_sql(sql):
    # Here, you would execute your SQL query using a database connection.
    # For demonstration, we'll just return a string
    return { 'col': 'value'}



def process_queries(queries, results=None, row=None):
    if results is None:
        results = {}


    main_json = []
    for query in queries:
        if 'name' in query and 'text' in query:
            # Execute the SQL query and store the result
            name = query['name']
            sql_query = query['text'] 
            sql_query = replace_variables ( query['text'] , row ) 
            sql_results = executeQuery(sql_query)
            for sql_result in sql_results:
                json_local = {} 
                if name == 'item':
                    json_local =  sql_result 
                else:
                    json_local[name] =  sql_result 
                if 'query' in query:
                    json_local['info'] = process_queries( query['query'], results , sql_result ) 

                main_json.append(json_local)
    
    return main_json 



# Connect to the database

# Read YAML
with open('queries.yml', 'r') as file:
    log.info("Opening file queries.yml")
    data = yaml.safe_load(file)


# print( process_recurrsive(data) ) 
data = process_queries(data['query']) 


with open('data.json', 'w') as file:
    # Dump the JSON data into the file
    log.info("writing to file data.json")
    json.dump(data, file, indent=4, cls=CustomJSONEncoder )


