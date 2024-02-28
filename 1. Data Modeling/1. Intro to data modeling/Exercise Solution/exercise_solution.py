import psycopg2 # import this as python wrapper to execute postgreSQL commands in the jupyter notebook

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

# To set autocommit as True, so then we dont have to commit after each transaction autometically. If we dont commit the first transaction then we cant execute the next transaction and 
conn.set_session(autocommit=True)
