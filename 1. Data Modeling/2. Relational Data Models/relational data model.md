# Relational Data Modeling
Database is a set of related data and the way it is organized. Database Management System is a computer software that allows users to interact with the database and provides access to all of the data.
![image](https://github.com/codeslash21/data_engineering/assets/32652085/c5ca3a55-adff-4779-9ce0-32b05ee15b08)

## OLAP VS OLTP
- **Online Analytical Processing (OLAP):**
Databases optimized for these workloads allow for complex analytical and ad hoc queries, including aggregations. These type of databases are optimized for reads.

- **Online Transactional Processing (OLTP):**
Databases optimized for these workloads allow for less complex queries in large volume. The types of queries for these databases are read, insert, update, and delete.

The key to remember the difference between OLAP and OLTP is analytics (A) vs transactions (T). If you want to get the price of a shoe then you are using OLTP (this has very little or no aggregations). If you want to know the total stock of shoes a particular store sold, then this requires using OLAP (since this will require aggregations). OLTP queries will have little aggregations really, if any, while OLAP will heavily focus on aggregations.

## Normalisation and Denormalisation
Normalisation to reduce data redundancy and increase data integrity, whereas denormalisation must be done in read heavy workloads to increase. Denormalisation is the process of trying to improve the read performance of a database at the expense of losing some write performance by adding redundant copies of data. JOINS on the database allow for outstanding flexibility but are extremely slow. If you are dealing with heavy reads on your database, you may want to think about denormalizing your tables. You get your data into normalized form, and then you proceed with denormalization. So, denormalization comes after normalization. Denormalization is part of the data modeling process to make data more easily queried.

- **Objectives of Normalisation:**
1. To free the database from unwanted insertions, updates, & deletion dependencies
2. To reduce the need for refactoring the database as new types of data are introduced
3. To make the relational model more informative to users
4. To make the database neutral to the query statistics

## Fact and Dimension table
Fact table consists of the measurements, metrics or facts of a business process. Dimension table is a structure that categorizes facts and measures in order to enable users to answer business questions. Dimensions are people, prodcuts, place, time etc. 

![image](https://github.com/codeslash21/data_engineering/assets/32652085/3a26aa37-4a2c-4cc7-b7d2-70e047c1a006)


## NOTE
- Two of most popular(because of their simplicity) data mart schema for data warehouses are: Star schema and Snowflake schema
