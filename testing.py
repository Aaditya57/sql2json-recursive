import mysql.connector
import logging
import warnings
import pandas as pd 

# Replace these values with your actual database connection details
server_name = '192.168.88.71:3307'
database_name = 'db_ad'
username = 'root'
password = 'a@no1Knows'


host = '192.168.88.71'
database = 'db_ad'
user = 'root'
password = 'a@no1Knows'
port = 3307

def log( string ): 
    log = getLogger() 
    log.debug( string )  

def getLogger():
    log_level = 'INFO'
    # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % log_level)

    
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s    - %(message)s')
    logger = logging.getLogger()
    
    # file_handler = logging.FileHandler(log_file)
    # file_handler.setFormatter(logging.Formatter(log_format))
    # logger.addHandler(file_handler)    
    
    return logger 


def getMySQLConnection():
    # Connect mySQL Datbase 
    log = getLogger() 
    warnings.filterwarnings("ignore")
    try:
        mysqlconnection = mysql.connector.connect( 
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        testcnt = pd.read_sql( "select CURRENT_TIMESTAMP() " , mysqlconnection ) 
        log.debug( testcnt.shape) 
    except mysql.connector.Error as error:
        log.error("Error while connecting to MySQL:", error)
        log.error( error )
        exit(0)

    return mysqlconnection 


# try:
#     # Attempt to establish a connection
#     # connection = mysql.connector.connect(
#     #     host=host,
#     #     database=database,
#     #     user=user,
#     #     password=password,
#     #     port=port
#     # )
#     connection = getMySQLConnection() 
#     # If successful, print a success message
#     if connection.is_connected():
#         print("Connection to the database successful!")

#         # Example: Execute a basic query
#         cursor = connection.cursor()
#         cursor.execute("SELECT version()")
#         row = cursor.fetchone()
#         print(f"Database version: {row[0]}")

#         # Close the cursor and connection
#         cursor.close()
#         connection.close()

# except mysql.connector.Error as err:
#     # If there is an error, print the details
#     print(f"Error: {err}")