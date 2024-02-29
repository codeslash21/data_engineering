import psycopg2 # import this as python wrapper/driver to execute postgreSQL commands in the jupyter notebook

# studentdb is the default database
try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)

# to get a cursor to the database
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)

# To set autocommit as True, so then we dont have to commit after each transaction autometically. If we dont commit the first transaction 
# then we cant execute the next transaction and the transaction will be aborted. At this point we will be blocked unitl we restart the 
# connection or commit the previous transaction and to do that we have to do `conn.commit()` after each transaction. We can do the following
# to do autocommit after each transaction.
conn.set_session(autocommit=True)

# To create database
try: 
    cur.execute("create database testdb")
except psycopg2.Error as e:
    print(e)

# To close connection to previous default database student and connect to newly created database
try: 
    conn.close()
except psycopg2.Error as e:
    print(e)
    
try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=testdb user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
    
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

# To create table to the currect database
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS songs (song_title varchar, artist_name varchar, year int, album_name varchar, single varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

# To insert data
try: 
    cur.execute("INSERT INTO songs (song_title, artist_name, year, album_name, single) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 ("Think For Yourself", "The Beatles", "1965", "Rubber Soul", "False"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

# To get all the row in a table
try: 
    cur.execute("SELECT * FROM songs;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

# To close cursor and connection
cur.close()
conn.close()

