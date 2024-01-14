
import logging
import warnings
import pandas as pd 
from configparser import ConfigParser
from dotenv import load_dotenv
import os
import pyodbc


load_dotenv()

host = os.getenv("host")
database = os.getenv("database")
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")

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
    
    return logger 


def getMySQLConnection():
    # Connect mySQL Datbase 
    log = getLogger() 
    warnings.filterwarnings("ignore")
    try:
        str = f"DRIVER={'ODBC Driver 17 for SQL Server'};SERVER={host};DATABASE={database};UID={user};PWD={password};PORT={port}"
        mysqlconnection = pyodbc.connect(str)
        testcnt = pd.read_sql( "select CURRENT_TIMESTAMP() " , mysqlconnection ) 
        log.debug( testcnt.shape) 
    except pyodbc.Error as error:
        log.error("Error while connecting to MySQL:", error)
        log.error( error )
        exit(0)

    return mysqlconnection 