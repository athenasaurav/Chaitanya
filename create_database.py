import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine, types
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host="localhost" , user="root" , passwd="12345" ,db="mysql")#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE rasa_db")
        print("Database is created")
        # cursor.execute("CREATE TABLE rikjai(id VARCHAR(255),Outdoor_Indoor VARCHAR(255), Category VARCHAR(255), Title VARCHAR(255), Date VARCHAR(255), Timeslot VARCHAR(255), Duration VARCHAR(255), Destination VARCHAR(255), District VARCHAR(255), min_nos_people VARCHAR(255), max_nos_people VARCHAR(255), vacancy VARCHAR(255), Price_per_head VARCHAR(255), Tel VARCHAR(255), Website  VARCHAR(255))")
        # print("Table is created....")

except Error as e:
    print("Error while connecting to MySQL", e)

try:
    engine = create_engine('mysql://root:12345@localhost/rasa_db') # enter your password and database names here
    df = pd.read_csv("email_pass.csv",sep=',',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
    df.to_sql('login',con=engine,index=False,if_exists='append')
    print("Login Table is created")
except Error as e:
    print("Error while creating table to MySQL", e)


try:
    engine = create_engine('mysql://root:12345@localhost/rasa_db') # enter your password and database names here
    df = pd.read_csv("incident.csv",sep=',',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
    df.to_sql('incident',con=engine,index=False,if_exists='append')
    print("Incident Table is created")
except Error as e:
    print("Error while creating table to MySQL", e)