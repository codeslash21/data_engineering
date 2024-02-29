import cassandra #python wrapper/driver to execute apache cassandra queries

# This connect to our local instance of apache cassandra. This connection will reach out to database and insure that we have correct 
# privilages to connect to this database. Once we get back our cluster object, we need to connect and that will create our session that we will
# use to execute queries
from cassandra.cluster import Cluster
try: 
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
except Exception as e:
    print(e)

# To create keyspace/database. On a one node local instance replcationn strategy will be 'SimpleStrategy' factor will be '1'
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS testdb
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)

except Exception as e:
    print(e)

# Connect to keyspace/database
try:
    session.set_keyspace('testdb')
except Exception as e:
    print(e)

# Creating table, we cant create data model or table without having information about what type of query we are going to perform on it. 
# Based on the query type we have to choose primary key and clustering column, generally the columns in the WHERE clause will be the PK
query = "CREATE TABLE IF NOT EXISTS test "
query = query + "(song_title text, artist_name text, year int, album_name text, single boolean, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

# Add data to table
query = "insert into test (song_title, artist_name, year, album_name, single)" 
query = query + " VALUES (%s, %s, %s, %s, %s)"
try:
    session.execute(query, ("Let It Be", "The Beatles", 1970, "Across The Universe", False))
except Exception as e:
    print(e)

# To get the data 
query = 'SELECT * FROM test'
try:
    rows = session.execute(query)
except Exception as e:
    print(e)  
for row in rows:
    print (row.year, row.album_name, row.artist_name)

# To execute query
query = "select * from test where year=1970 and artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.year, row.album_name, row.artist_name)

# close cursor and session
session.shutdown()
cluster.shutdown()
