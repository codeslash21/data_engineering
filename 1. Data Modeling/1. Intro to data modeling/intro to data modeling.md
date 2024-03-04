# Introduction to data modeling
- [Data Model](#data-model)
- [Relational Model](#relational-model)
- [ACID Transactions](#acid-transactions)
- [NoSQL Database](#nosql-database)
- [Apache Cassandra](#apache-cassandra)


A database is a structured repository or collection of data that is stored and retrieved electronically for use in applications. Data can be stored, updated, or deleted from a database. And the software used to access the database by the user and application is the database management system (DBMS).

## Data Model
Data model is an abstraction that organise the elements of data and how they will relate to each other. Data modeling is the process of creating data models for an information system. Data modeling starts from conceptual data modeling

![image](https://github.com/codeslash21/data_engineering/assets/32652085/09b4f573-b327-49a3-bf43-186e32ace137)

### Why Data Modeling Important
The organization of the data for your applications is extremely important and makes everyone's life easier. Having a well thought out and organized data model is critical to how that data can later be used. Queries that could have been straightforward and simple might become complicated queries if data modeling isn't well thought out. Data modeling is not a fixed process. It is iterative as new requirements and data are introduced. Having flexibility will help as new information becomes available.

## Relational Model

![image](https://github.com/codeslash21/data_engineering/assets/32652085/b3219a8b-41be-43fa-8fd1-d7ded3b07457)

Relational database is a digital database based on the relational model of data and a software system is used to maintain relational databases is a relational database management system (RDBMS). 
![image](https://github.com/codeslash21/data_engineering/assets/32652085/a8cbcb89-5757-41d8-8681-8ac18d7a7227)

## ACID Transactions
Properties of database transactions intended to guarantee validity even in the event of errors or power failures.
- **Atomicity:** The whole transaction is processed or nothing is processed. A commonly cited example of an atomic transaction is money transactions between two bank accounts. The transaction of transferring money from one account to the other is made up of two operations. First, you have to withdraw money in one account, and second you have to save the withdrawn money to the second account. An atomic transaction, i.e., when either all operations occur or nothing occurs, keeps the database in a consistent state. This ensures that if either of those two operations (withdrawing money from the 1st account or saving the money to the 2nd account) fail, the money is neither lost nor created. 
- **Consistency:** Only transactions that abide by constraints and rules are written into the database, otherwise the database keeps the previous state. The data should be correct across all rows and tables.
- **Isolation:** Transactions are processed independently and securely, order does not matter. A low level of isolation enables many users to access the data simultaneously, however this also increases the possibilities of concurrency effects (e.g., dirty reads or lost updates). On the other hand, a high level of isolation reduces these chances of concurrency effects, but also uses more system resources and transactions blocking each other.
- **Durability:** Completed transactions are saved to database even in cases of system failure. A commonly cited example includes tracking flight seat bookings. So once the flight booking records a confirmed seat booking, the seat remains booked even if a system failure occurs. 

![image](https://github.com/codeslash21/data_engineering/assets/32652085/5c99fe1c-7b72-4af2-bd8e-89dd4bee4080)

## NoSQL Database
NoSQL databases were created due to some of the issues faced with relational databases. NoSQL databases have been around since the 1970s, but they became more popular since the 2000s as data sizes increased and outages/downtime decreased in acceptability. Following are some example of NoSQL database
- **Apache Cassandra** (Partition Row store)
- **MongoDB** (Document store)
- **DynamoDB** (Key-Value store)
- **Apache HBase** (Wide Column Store)
- **Neo4J** (Graph Database)

![image](https://github.com/codeslash21/data_engineering/assets/32652085/ea4113f7-b36e-4203-90eb-9de080d4627d)

![image](https://github.com/codeslash21/data_engineering/assets/32652085/0e3f094d-d2d9-491c-b3d3-6d955615d44c)

There are some NoSQL databases that offer some form of ACID transaction. As of v4.0, MongoDB added multi-document ACID transactions within a single replica set. With their later version, v4.2, they have added multi-document ACID transactions in a sharded/partitioned deployment.

## Apache Cassandra
Apache Cassandra provides scalability and high availablity without compromising performance. Linear scalability and proven fault-tolerance on commodity hardware and cloud infrastructure make it perfect platform for mission-critical data. Apache cassandra uses it own query language CQL. Apache Cassandra requires data modeling based on the query you want. There are no duplicates in Apache cassnadra. Some use cases are
1. Transaction logging (retail, health care)
2. Internet of Things (IoT)
3. Time series data
4. Any workload that is heavy on writes to the database (since Apache Cassandra is optimized for writes).

### Terminology
![image](https://github.com/codeslash21/data_engineering/assets/32652085/34d2b50c-59ae-424e-affc-72cf8ae691da)

- **Keyspace:** Collections of table
- **Table:** Group of partition
- **Row:** A single item
- **Partition:** Fundamental unit of access. Collection of rows. How data is distributed.
- **Primary Key:** Primary key is made up of a partition key and clustering columns
- **Columns:** Clustering and data. Labeled element


## NOTE:
- Relational databases include a schema of tables that are linked to each other.
- PostgreSQL is an open-source object-relational database system. PostgreSQL uses and builds upon SQL database language by providing various features that reliably store and scale complicated data workloads. PostgreSQL SQL syntax is different than other relational databases SQL syntax.
- PostgreSQL allows duplicate
- `!echo "alter user student createdb;" | sudo -u postgres psql` `|` is pipe operator in unix It takes the output from the command on the left and passes it as input to the command on the right. `alter user student createdb;` this means This SQL statement alters the properties of the PostgreSQL user `student` to grant it the ability to create databases createdb. `sudo -u postgres psql` This part of the command is essentially executing `psql` as the `postgres`. `postgres`, which is typically the default administrative user for PostgreSQL. `psql` this is the PostgreSQL interactive terminal. It allows you to interact with PostgreSQL databases using SQL commands. In summary, the entire command is using `sudo` to execute the `psql` command as the `postgres` user, and then it's passing the SQL statement `alter user student createdb;` to `psql`, which alters the `student` user in PostgreSQL to grant it the ability to create databases.
- `studentdb` is the default database for postgreSQL
