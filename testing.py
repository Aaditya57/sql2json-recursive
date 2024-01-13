import mysql.connector
import logging
import warnings
import pandas as pd 
from configparser import ConfigParser
from mysql.connector import MySQLConnection


def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}  
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db 

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
        db_config = read_db_config()
        mysqlconnection = MySQLConnection(**read_db_config())
        testcnt = pd.read_sql( "select CURRENT_TIMESTAMP() " , mysqlconnection ) 
        log.debug( testcnt.shape) 
    except mysql.connector.Error as error:
        log.error("Error while connecting to MySQL:", error)
        log.error( error )
        exit(0)

    return mysqlconnection 