# Cloud Data Warehouse
![image](https://github.com/codeslash21/data_engineering/assets/32652085/68e4f63f-dde6-41ce-a4a8-57745b9d7ddf)

![image](https://github.com/codeslash21/data_engineering/assets/32652085/a466f5e5-66f4-488c-a0d9-9bda935bfe6c)

![image](https://github.com/codeslash21/data_engineering/assets/32652085/5f97a32c-d3a9-413d-9ad0-c4c4b1b9db72)

A data warehouse is a copy of transaction data specifically structured for query and analysis. A data warehouse is a system that retrieves and consolidates data periodically from the source systems into a dimensional or normalized data store. It usually keeps years of history and is queried for business intelligence or other analytical activities. It is typically updated in batches, not every time a transaction happens in the source system. 

![image](https://github.com/codeslash21/data_engineering/assets/32652085/f1fc0843-ef4a-449e-bc94-df94e38b322f)

- **Dimensional data model** is a type of data model that is specifically designed for data warehousing and analytics purposes. It organizes data in a way that makes it easy for business users and data analytics applications to work with the data and optimize analytical query performance. In a dimensional data model, data is organized into two main types of tables: `fact tables` and `dimension tables`.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/1fc1f279-48d3-44b5-92a1-3326d63cb216)

![image](https://github.com/codeslash21/data_engineering/assets/32652085/f6b6b60b-f5cd-469c-99f4-53ba7f100367)

## Dimension Modeling
We know that 3NF databases are actually optimizedfor consistency and deduplication and hard to explain to business users. If we try to use 3NF databases for analytical queries in a data warehouse, we would incur lots of expensive joins. Instead we will ETL data into a dimensional model for a data warehouse using star schemas. Star schema consists of fact and dimension tables.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/96d8c3b6-b9a8-469c-a986-7ac4b0e1fbb0)

### `Goals of the Star Schema`
- Easy to understand
- Fast analytical query performance

### `Fact Tables`
- Fact table is always going to be numeric and additive in 99% of the cases.
- Record business events, like an order, a phone call, a book review
- Fact tables columns record events recorded in quantifiable metrics like quantity of an item, duration of a call, a book rating

### `Dimension Tables`
- Record the context of the business events, e.g. who, what, where, why, etc..
- Dimension tables columns contain attributes like the store at which an item is purchased or the customer who made the call, etc.
