import psycopg2
import csv
from urllib.parse import urlparse, uses_netloc
import configparser

#######################################################################
# IMPORTANT:  You must set your config.ini values!
#######################################################################
# The connection string is provided by elephantsql.  Log into your account and copy it into the
# config.ini file.  It should look something like this:
# postgres://vhepsma:Kdcads89DSFlkj23&*dsdc-32njkDSFS@foo.db.elephantsql.com:7812/vhepsma
# Make sure you copy the entire thing, exactly as displayed in your account page!
#######################################################################
config = configparser.ConfigParser()
config.read('config.ini')
connection_string = config['database']['postgres_connection']

#  You may use this in seed_database.  The function reads the CSV files
#  and returns a list of lists.  The first list is a list of classes,
#  the secode list is a list of ships.
def load_seed_data():
    classes = list()
    with open('classes.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            classes.append(row)

    ships = list()
    with open('ships.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            ships.append(row)
    #print(ships)
    #return [classes, ships]
    return ships


def seed_database():
    # you must create the necessary tables, if they do not already exist.
    # BE SURE to setup the necessary foreign key constraints such that deleting
    # a class results in all ships of that class being removed automatically.

    # after ensuring the tables are present, count how many classes there are.
    # if there are none, then call load_data to get the data found in config.json.
    # Insert the data returned from load_data.  Hint - it returns a tuple, with the first being a list
    # of tuples representing classes, and the second being the list of ships.  Carefully
    # examine the code or print the returned data to understand exactly how the data is structuredoo
    # i.e. column orders, etc.

    # If there is already data, there is no need to do anything at all...
    # Open a cursor to perform database operations
    #1) First, construct a CREATE TABLE statement.
    #2)Next, connect to the PostgreSQL database by calling the connect() function. The connect() function returns a connection object.
    #3)Then, create a cursor object by ca
    # After that, execute the CREATE TABLE by calling the execute() method of the cursor object.
    #Finally, close the communication with the PostgreSQL database server by calling the close() methods of the cursor and connection objects.


    cur = conn.cursor()
    cur.execute("CREATE TABLE Ships(Name  varchar[20], Class  varchar[20],  Launched date);")
    #load_seed_data()
    print (ships)
    cur.execute("INSERT INTO Ships(Name  , Class  ,  Launched ) VALUES (%s, %s,%s)",
    (California,Tennessee,1921))
      #   (ships[0],ships[1],ships[2]))
    cur.close()
    conn.close() 


#A foreign key is a field or group of fields in a table that uniquely identifies a row in 
# another table. In other words, a foreign key is defined in a table that references to the
#  primary key of the other tabl
#A foreign key constraint indicates that values in a column or a group of columns in the child table 
#match with the values in a column or a group of columns of the parent table. We say that a foreign key
#  constraint maintains referential integrity between child and parent tables.


         


# Return list of all classes.  Important, to receive full credit you
# should use a Python generator to yield each item out of the cursor.
# Column order should be class, type, country, guns, bore, displacement
##def get_classes():

# Return list of all ships, joined with class.  Important, to receive full credit you
# should use a Python generator to yield each item out of the cursor.
# Column order should be ship.class, name, launched, class.class, type, country, guns, bore, displacement
# If class_name is not None, only return ships with the given class_name.  Otherwise, return all ships
#def get_ships(class_name):


# Data will be a list ordered with class, type, country, guns, bore, displacement.
#def add_class(data):


# Data will be a list ordered with class, name, launched.
# def add_ship(data):

# Delete class with given class name.  Note while there should only be one
# SQL execution, all ships associated with the class should also be deleted.
#def delete_class(class_name):


# Delets the ship with the given class and ship name.
#def delete_ship(ship_name, class_name):



# This is called at the bottom of this file.  You can re-use this important function in any python program
# that uses psychopg2.  The connection string parameter comes from the config.ini file in this
# particular example.  You do not need to edit this code.

def connect_to_db(conn_str):
        uses_netloc.append("postgres")
        url = urlparse(conn_str)

        conn = psycopg2.connect(database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port)

        return conn

# This establishes the connection, conn will be used across the lifetime of the program.
conn = connect_to_db(connection_string)
# import ipdb; ipdb.set_trace()
print ("************************")
print ("conn = {}".format(conn))
print ("************************")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Ships (Name  varchar(20), Class varchar(20),  Launched smallint);")
#cur.execute("CREATE TABLE IF NOT EXISTS Ships (Name  varchar[20], Class  varchar[20],  Launched date);")
#load_seed_data()
#  print (ships)
#cur.execute("INSERT INTO Ships(Name  , Class  ,  Launched ) VALUES (%s, %s,%s)",
#
# ("California","Tennessee",1921))
   #            "INSERT INTO test (num, data) VALUES (%s, %s)",
#      (100, "abc'def")
           
#conn.commit()

shipsret=load_seed_data()
# print (shipsret)
# cur.execute("INSERT INTO (Name  , Class  ,  Launched ) VALUES (%s, %s,%s)",
#     (shipsret))
#cur.execute("INSERT INTO ships (Name  , Class  ,  Launched ) VALUES (%s, %s,%s)",
#('test','test2', 1560))

for ship in shipsret:
#     print (ship[0] + ',' + ship[1] + ',' +ship[2])
#     print (ship)
#print(shipsret)
   # cur.execute("INSERT INTO (Name  , Class  ,  Launched ) VALUES (%s, %s,%s)",
    #(ship)ships[0],ships[1],ships[2])
   # cur.execute("INSERT INTO (Name  , Class  ,  Launched ) VALUES (%s, %s,%s)",
    #(ship[0],ship[1],ship[2]))
    cur.execute("INSERT INTO ships (Name  , Class  ,  Launched ) VALUES (%s, %s,%s)",
    (ship))
           
           
conn.commit()

    #(ships[0],ships[1],ships   [2]))
cur.close()
conn.close() 

#seed_database() 
