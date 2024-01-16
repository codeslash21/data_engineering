# Introduction to data modeling
A database is a structured repository or collection of data that is stored and retrieved electronically for use in applications. Data can be stored, updated, or deleted from a database. And the software used to access the database by the user and application is the database management system (DBMS).

## Data Model
Data model is an abstraction that organise the elements of data and how they will relate to each other. Data modeling is the process of creating data models for an information system. Data modeling starts from conceptual data modeling

![image](https://github.com/codeslash21/data_engineering/assets/32652085/09b4f573-b327-49a3-bf43-186e32ace137)

## Why Data Modeling Important
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


## NOTE:
- Relational databases include a schema of tables that are linked to each other.
- 
