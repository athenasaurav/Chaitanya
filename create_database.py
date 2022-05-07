import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine, types
import mysql.connector as mysql
from mysql.connector import Error
from actions import config
try:
    conn = mysql.connect(host=config.host , user=config.user , passwd=config.password ,db="mysql")#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE {}".format(config.database))
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    engine = create_engine('mysql://{}:{}@{}/{}'.format(config.user, config.password, config.host, config.database)) # enter your password and database names here
    df = pd.read_csv("email_pass.csv",sep=',',quotechar='\'',encoding='utf8') # Replace CSV_File_name with your excel sheet name
    df.to_sql('login',con=engine,index=False,if_exists='append')
    print("Login Table is created")
except Error as e:
    print("Error while creating table to MySQL", e)


try:
    engine = create_engine('mysql://{}:{}@{}/{}'.format(config.user, config.password, config.host, config.database)) # enter your password and database names here
    df = pd.read_csv("incident.csv",sep=',',quotechar='\'',encoding='utf8') # Replace CSV_File_name with your excel sheet name
    df.to_sql('incident',con=engine,index=False,if_exists='append')
    print("Incident Table is created")
except Error as e:
    print("Error while creating table to MySQL", e)