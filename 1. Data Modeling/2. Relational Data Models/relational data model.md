# Relational Data Modeling
- [OLAP VS OLTP](#olap-vs-oltp)
- [Normalisation and Denormalisation](#normalisation-and-denormalisation)
- [Fact and Dimension table](#fact-and-dimension-table)
- [Star Schema](#star-schema)
- [Snowflake Schema](#snowflake-schema)
- [Data Definition and Constraints](#data-definition-and-constraints)


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

#### Objectives of Normalisation:
1. To free the database from unwanted insertions, updates, & deletion dependencies
2. To reduce the need for refactoring the database as new types of data are introduced
3. To make the relational model more informative to users
4. To make the database neutral to the query statistics

## Fact and Dimension table
Fact table consists of the measurements, metrics or facts of a business process. Dimension table is a structure that categorizes facts and measures in order to enable users to answer business questions. Dimensions are people, prodcuts, place, time etc. 

![image](https://github.com/codeslash21/data_engineering/assets/32652085/3a26aa37-4a2c-4cc7-b7d2-70e047c1a006)

## Star Schema
Star Schema is the simplest style of data mart schema. The star schema consists of one or more fact tables referencing any number of dimension tables. 
- Gets its name from the physical model resembling a star shape
- A fact table is at its center
- Dimension table surrounds the fact table representing the star’s points.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/1cfbcfd2-88be-48d9-9078-df35232e0085)

### Benefits
- You can denormalize your table
- Simplifies queries with simple joins
- Fast aggregations. Aggregations perform calculations and clustering of our data so that we do not have to do that work in our application. Examples : COUNT, GROUP BY etc

### Drawbacks
- Issues come up with denormalisation
- Data integrity. As because of denormalisation there will be lots of duplicate data.
- Decrease query flexibility. Because of denormalisation you will not be able to do as many ad-hoc queries on your table.
- Many to many relationship is hard to support, it has been simplified.

## Snowflake Schema
Its a logical arrangement of table in multidimensional database represented by centralized fact tables with are connected to multiple dimension tables. A complex snowflake shape emerges when the dimensions of snowflake schema are elaborated, having multiple levels of relationship, child tables ahaving multiple parent.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/57a1f85e-1b31-4460-b34c-d09e4301ae79)

### Star VS Snowflake Schema
- Star Schema is a special, simplified case of the snowflake schema.
- Star schema does not allow for many to many relationships while the snowflake schema does.
- Snowflake schema is more normalized than Star schema but only in 1NF or 2NF

## Data Definition and Constraints
#### NOT NULL
The NOT NULL constraint indicates that the column cannot contain a null value. You can add NOT NULL constraints to more than one column. Usually this occurs when you have a COMPOSITE KEY.
```
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL, 
    store_id int NOT NULL, 
    spent numeric
);
```
#### UNIQUE
The UNIQUE constraint is used to specify that the data across all the rows in one column are unique within the table. The UNIQUE constraint can also be used for multiple columns, so that the combination of the values across those columns will be unique within the table. In this latter case, the values within 1 column do not need to be unique.
```
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL UNIQUE, 
    store_id int NOT NULL UNIQUE, 
    spent numeric 
);
```
```
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL, 
    store_id int NOT NULL, 
    spent numeric,
    UNIQUE (customer_id, store_id, spent)
);
```
#### PRIMARY KEY
The PRIMARY KEY constraint is defined on a single column, and every table should contain a primary key. The values in this column uniquely identify the rows in the table. If a group of columns are defined as a primary key, they are called a composite key. That means the combination of values in these columns will uniquely identify the rows in the table. By default, the PRIMARY KEY constraint has the unique and not null constraint built into it.
```
CREATE TABLE IF NOT EXISTS store (
    store_id int PRIMARY KEY, 
    store_location_city text,
    store_location_state text
);
```
```
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int, 
    store_id int, 
    spent numeric,
    PRIMARY KEY (customer_id, store_id)
);
```
#### Upsert
In RDBMS language, the term upsert refers to the idea of inserting a new row in an existing table, or updating the row if it already exists in the table. The action of updating or inserting has been described as "upsert". The way this is handled in PostgreSQL is by using the INSERT statement in combination with the ON CONFLICT clause. 
```
INSERT INTO customer_address (
VALUES (432, '758 Main Street', 'Chicago', 'IL')
);
```
```
INSERT INTO customer_address (customer_id, customer_street)
VALUES
    (
    432, '923 Knox Street, Suite 1' 
) 
ON CONFLICT (customer_id) 
DO UPDATE
    SET customer_street  = EXCLUDED.customer_street;
```

## NOTE
- Two of most popular(because of their simplicity) data mart schema for data warehouses are: Star schema and Snowflake schema
