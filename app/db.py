import mysql.connector
import os

config = {
    'user': os.getenv('USER' , 'root'),
    'password':  os.getenv('PASSWORD', 'pass'),
    'host':  os.getenv('HOST', 'localhost'),
    'port':  int(os.getenv('PORT', 3306))
}

def get_connection():
    try: 
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as e:
        print(e.msg)
        return None
    
    

def init_db():
    query = '''
    CREATE DATABASE IF NOT EXISTS `weapons` ;
    USE `weapons`;
    CREATE TABLE `weapon_arehouse` (
      `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      `weapon_id` varchar(50),
      `weapon_name` varchar(50),
      `weapon_type` varchar(50),
      `range_km` INT,
      `weight_kg` FLOAT,
      `manufacturer` varchar(50),  
      `origin_country` varchar(50), 
      `storage_location` varchar(50),
      `year_estimated` varchar(50), 
      `risk_level` varchar(50)
    )
        '''
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.close()
        conn.close()
    
