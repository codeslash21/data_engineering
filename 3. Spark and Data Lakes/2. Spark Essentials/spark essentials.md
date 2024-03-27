
## Spark DAG
Apache Spark distributes data processing tasks over a cluster of distributed computing resources. How does it accomplish this? In distributed system, your program should not rely on resources created by previous execution. An `idempotent` program can run multiple times without any effect on the result. Some programs depend on prior state in order to execute properly. This is not considered idempotent, because they depend on that state existing before starting. One goal of idempotent code is that data can be processed in parallel, or simultaneously. This is done by calling the same code repeatedly in different threads, and on different nodes or servers for each chunk or block of data. If each program has no reliance on prior execution, there should be no problem splitting up processing. 

When writing Spark code, it is very important to avoid reading data into regular lists or arrays, because the amount of data your code deals with can be very large. Instead, you will use special datasets called Resilient Distributed Datasets (RDDs) and DataFrames. Much like an SQL query cursor, they don't actually hold all of the data in memory. These datasets give your Spark job access to the shared resources of the cluster in a very controlled way, that is managed outside of your Spark job.
```
## Instead of doing something like this 
textFile = open("invoices.txt", "r")
## invoiceList could occupy Gigabytes of Memory
invoiceList = textFile.readlines()
print(invoiceList)

## Do something like this instead
invoiceDataFrame = spark.read.text("invoices.txt")
## Leverage Spark DataFrames to handle large datasets
invoiceDataFrame.show(n=10)
```

## Directed Acyclic Graph (DAG)
Every Spark program makes a copy of its input data and never changes the original parent data. Because Spark doesn't change or mutate the input data, it's known as immutable. But what happens when you have lots of function calls in your program?
- In Spark, you do this by chaining together multiple function calls that each accomplish a small chunk of the work.
- It may appear in your code that every step will run sequentially
- However, they may be run more efficiently if Spark finds a more optimal execution plan

Spark uses a programming concept called lazy evaluation. Before Spark does anything with the data in your program, it first builds step-by-step directions of what functions and data it will need. In Spark, and in other similar computational processes, this is called a Directed Acyclic Graph (DAG). The reference is made to the fact that no explicit repetition is inherent in the process. For example, if a specific file is read more than once in your code, Spark will only read it one time. Spark builds the DAG from your code, and checks if it can procrastinate, waiting until the last possible moment to get the data.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/3e2ea34e-27a3-4e42-be5c-0a1fcc917de4)

## RDD
![image](https://github.com/codeslash21/data_engineering/assets/32652085/6b8606bd-293a-44f6-b356-c983ec2d96a1)

We can wrangle the data using python and SQL. To wrangle the data the code you write at higher level API first goes through a query optimizer to turn it into an actual execution plan before it can be run. Spark optimizer is called `catalyst`, under the hood catalyst will translate your code into same DAG. The code generated based on execution plan operates on a lower level data abstraction called RDD. RDDs are a low-level abstraction of the data. In the first version of Spark, you had to work directly with RDDs. You can think of RDDs as long lists distributed across various machines. You can still use RDDs as part of your Spark code although working with DataFrames and SQL is easier. In some cases we need more flexibilty than what higher level API can provide, so we need to directly interact with RDD. Using RDD gives us lots of flexibility but the code is harder to write and read and we also loose access to catalyst since this flexibility makes it much more difficult to optimize the code under the hood. 

## PySpark and SparkSession
### PySpark
Python is one of many languages you can use to write Spark Jobs. If you choose to use Python, then you will use the PySpark library. `PySpark` gives you access to all the important Spark data constructs like:
- RDDs
- DataFrames
- Spark SQL
  
That means you can write Spark code that runs in either a Spark Cluster, in a Jupyter Notebook, or on your laptop. When you write code on your Jupyter Notebook or a laptop, Spark creates a temporary Spark node that runs locally. Because Spark uses Java, it is necessary to install the JDK on a computer used to run PySpark code.

### SparkSession
- The first component of each Spark Program is the `SparkContext`. The `SparkContext` is the main entry point for Spark functionality and connects the cluster with the application.
- To create a `SparkContext`, we first need a `SparkConf` object to specify some information about the application such as its name and the master's nodes' IP address. If we run Spark in local mode, we can just put the string `local` as master.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/d856c1dd-9eed-4e78-a004-f3d6997b30a6)

- To read data frames, we need to use Spark SQL equivalent, the `SparkSession`. Similarity to the `SparkConf`, we can specify some parameters to create a SparkSession. `getOrCreate()` for example, means that if you already have a `SparkSession` running, instead of creating a new one, the old one will be returned and its parameters will be modified to the new configurations.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/b1947dfe-a9a3-4683-a9fb-924a6603dccf)
