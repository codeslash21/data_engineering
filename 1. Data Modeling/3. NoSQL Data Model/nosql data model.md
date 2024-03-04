# NoSQL Data Modeling
- [When to Use NoSQL](#when-to-use-nosql)
- [Eventual Consistency](#eventual-consistency)
- [CAP Theorem](#cap-theorem)
- [CQL](#cql)
- [Primary Key](#primary-key)
- [Clustering Columns](#clustering-columns)
- [WHERE clause](#where-clause)
  
## When to Use NoSQL:
- Need high Availability in the data: Indicates the system is always up and there is no downtime
- Have Large Amounts of Data
- Need Linear Scalability: The need to add more nodes to the system so performance will increase linearly
- Low Latency: Shorter delay before the data is transferred once the instruction for the transfer has been received.
- Need fast reads and write

## Eventual Consistency
Its related to distributed database system. Over time (if no new changes are made) each copy of the data will be the same, but if there are new changes, the data may be different in different locations. The data may be inconsistent for only milliseconds. There are workarounds in place to prevent getting stale data.

## CAP Theorem
![image](https://github.com/codeslash21/data_engineering/assets/32652085/1a2ef323-7c3f-4a59-bfc8-053c7ec6cedf)

- **Consistency:** Every read from the database gets the latest (and correct) piece of data or an error
- **Availability:** Every request is received and a response is given -- without a guarantee that the data is the latest update
- **Partition Tolerance:** The system continues to work regardless of losing network connectivity between nodes

<br></br>

- Consistency in the ACID principle refers to the requirement that only transactions that abide by constraints and database rules are written into the database, otherwise the database keeps previous state. In other words, the data should be correct across all rows and tables. However, consistency in the CAP theorem refers to every read from the database getting the latest piece of data or an error.
- The CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability. So there is no such thing as Consistency and Availability in a distributed database since it must always tolerate network issues. You can only have Consistency and Partition Tolerance (CP) or Availability and Partition Tolerance (AP). Remember, relational and non-relational databases do different things, and that's why most companies have both types of database systems.
- According to the CAP theorem, a database can actually only guarantee two out of the three in CAP. So supporting Availability and Partition Tolerance makes sense, since Availability and Partition Tolerance are the biggest requirements.
- If I am trying to do analysis, such as determining a trend over time, e.g., how many friends does John have on Twitter, and if you have one less person counted because of "eventual consistency" (the data may not be up-to-date in all locations), that's OK. In theory, that can be an issue but only if you are not constantly updating. If the pipeline pulls data from one node and it has not been updated, then you won't get it. Remember, in Apache Cassandra it is about Eventual Consistency.

## CQL
Cassandra query language is the way to interact with the database and is very similar to SQL. The following are not supported by CQL
- JOINS
- GROUP BY
- Subqueries

## Primary Key
- Must be unique
- Hashing of this value results in placement on a particular node in the system.
- The PRIMARY KEY is made up of either just the PARTITION KEY or may also include additional CLUSTERING COLUMNS
- A Simple PRIMARY KEY is just one column that is also the PARTITION KEY. A Composite PRIMARY KEY is made up of more than one column and will assist in creating a unique value and in your retrieval queries. For composite primary key the first column will be the partition key and the remaining columnns are clustering columns.
- The PARTITION KEY will determine the distribution of data across the system, so we need to choose the partition key properly for data to be evenly distributed.

## Clustering Columns
- The clustering column will sort the data in ascending order within the partition.
- More than one clustering column can be added (or none!)
- From there the clustering columns will sort in order of how they were added to the primary key
- You cannot use the clustering columns out of order in the SELECT statement. You may choose to omit using a clustering column in your SELECT statement.
```
query = "CREATE TABLE IF NOT EXISTS music_library "
query += """
(year int, artist_name text, album_name text, city text, 
 PRIMARY KEY (artist_name, album_name, city))
WITH CLUSTERING ORDER BY (album_name DESC, city DESC);
"""
```

## WHERE clause
- Data Modeling in Apache Cassandra is query focused, and that focus needs to be on the WHERE clause.
- Partition key must be included in your query and clustering columns can be used in order they appear in parimary key.
- Failure to include a WHERE clause will result in an error. But its possible to execute query without using where clause if you add a configuration `ALLOW FILTERING` to your query.


## NOTE
- In Apache Cassandra every node is connected to every node -- it's peer to peer database architecture.
- In Apache Cassandra no duplicate is allowed. If we try to insert a new data with same PK which is already there then that data will be overwritten, no error will be thrown.
- If we dont have unique primary key, then for a query cassandra returns all the rows.
