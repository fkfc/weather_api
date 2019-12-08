from threading import Lock
import sqlite3

# Provides an abstraction layer for the database with an atomic thread-safe method for sql commands
class Database:
    _mutex = Lock()
    _con = None
    _database_file = "weather.db"

    @staticmethod
    def execute(sql, *params):
        Database._mutex.acquire()
        cursor = Database._get_cursor()
        response = Database._execute(cursor, sql, *params)
        Database._mutex.release()
        return response

    @staticmethod
    def _get_cursor():     
        if Database._con == None: Database._connect()
        return Database._con.cursor()

    @staticmethod
    def _connect():
        Database._con = sqlite3.connect(Database._database_file, check_same_thread = False)
        Database._create_database(Database._get_cursor())
    
    @staticmethod
    def _execute(cur, sql, *params):
        result = cur.execute(sql, *params).fetchall()
        Database._con.commit()
        return result

    @staticmethod
    def _create_database(cur):
        sql = "\
            CREATE TABLE IF NOT EXISTS cities(\
                id INTEGER PRIMARY KEY,\
                name TEXT,\
                state CHAR(50)\
            )"
        Database._execute(cur, sql)
        
        sql = "\
            CREATE TABLE IF NOT EXISTS forecasts(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                city INTEGER,\
                date CHAR(10),\
                rain_probability REAL,\
                rain_precipitation REAL,\
                temperature_min REAL,\
                temperature_max REAL\
            )"
        Database._execute(cur, sql)
