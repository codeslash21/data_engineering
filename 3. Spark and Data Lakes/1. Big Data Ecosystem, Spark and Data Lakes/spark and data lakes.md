# Big Data Ecosystem
- [Hadoop](#hadoop)
- [Spark](#spark)
- [MapReduce](#mapreduce)
- [Spark Cluster](#spark-cluster)
- [Spark's Limitations](#sparks-limitations)
- [Data Lakes](#data-lakes)
- [Lakehouse Architecture](#lakehouse-architecture)


![image](https://github.com/codeslash21/data_engineering/assets/32652085/d2b3e918-0b3a-4938-8ec0-e85232613912)

Early efforts at processing large amounts of structured, semi-structured, and unstructured data led to the development of Hadoop. Hadoop incorporates two key components:
- The **Hadoop Distributed File System** (or HDFS) provides distributed storage with high-throughput access to data.
- **MapReduce** provides a way to conduct massive parallel processing for large amounts of data.

The next step in the evolution was Apache Spark. Spark built on the ideas of Hadoop and provided multiple programming APIs for processing data as well as providing an interactive interface for iteratively developing data engineering and data science solutions. Hadoop and Spark have led to the development and popularity of data lakes to process large amounts of both structured and unstructured data. Finally, the latest step in the evolution of big data ecosystems is the lake house architecture. Lake house seeks to combine the strengths of both data lakes and data warehouses.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/37cb4f56-65e3-4d48-a0c3-3d0886f8969f)

Data warehouses are based on specific and explicit data structures that allow for highly performant business intelligence and analytics but they do not perform well with unstructured data. Data lakes are capable of ingesting massive amounts of both structured and unstructured data with Hadoop and Spark providing processing on top of these datasets. Data lakes have several shortcomings that grew out of their flexibility. They are unable to support transactions and perform poorly with changing datasets. Data governance became difficult due to the unstructured nature of these systems. Modern lakehouse architectures seek to combine the strengths of data warehouses and data lakes into a single, powerful architecture.

## Hadoop 
Haddop is an ecosystem of tools for big data storage and data analysis. Hadoop is an older system than Spark but is still used by many companies. The major difference between Spark and Hadoop is how they use memory. Hadoop writes intermediate results to disk whereas Spark tries to keep data in memory whenever possible. This makes Spark faster for many use cases. Oftentimes when someone is talking about Hadoop in general terms, they are actually talking about Hadoop MapReduce.
- **Hadoop MapReduce** - a system for processing and analyzing large data sets in parallel.
- **Hadoop YARN** - a resource manager that schedules jobs across a cluster. The manager keeps track of what computer resources are available and then assigns those resources to specific tasks.
- **Hadoop Distributed File System (HDFS)** - a big data storage system that splits data into chunks and stores the chunks across a cluster of computers.
- **Apache Pig** - a SQL-like language that runs on top of Hadoop MapReduce
- **Apache Hive** - another SQL-like interface that runs on top of Hadoop MapReduce

## Spark
Spark contains libraries for data analysis, machine learning, graph analysis, and streaming live data. Spark is generally faster than Hadoop. This is because Hadoop writes intermediate results to disk whereas Spark tries to keep intermediate results in memory whenever possible. The Hadoop ecosystem includes a distributed file storage system called HDFS (Hadoop Distributed File System). Spark, on the other hand, does not include a file storage system. You can use Spark on top of HDFS but you do not have to. Spark can read in data from other sources as well. 

Data streaming is a specialized topic in big data. The use case is when you want to store and analyze data in real-time such as Facebook posts or Twitter tweets. Spark has a streaming library called Spark Streaming. Other popular distributed streaming processing projects include Storm and Flink. Flink is much faster than Spark Streaming library. 

## MapReduce
MapReduce is a programming technique for manipulating large data sets. "Hadoop MapReduce" is a specific implementation of this programming technique. The technique works by first dividing up a large dataset and distributing the data across a cluster. In the map step, each data is analyzed and converted into a (key, value) pair. Then these key-value pairs are shuffled across the cluster so that all keys are on the same machine. In the reduce step, the values with the same keys are combined together. While Spark doesn't implement MapReduce, you can write Spark programs that behave in a similar way to the map-reduce paradigm.

## Spark Cluster
Most computational frameworks are organized into a master-worker hierarchy:
- The master node is responsible for orchestrating the tasks across the cluster
- Workers are performing the actual computations

There are four different modes to setup Spark:
- Local mode: In this case, everything happens on a single machine. So, while we use spark's APIs, we don't really do any distributed computing. The local mode can be useful to learn syntax and to prototype your project.
- The other three modes are distributed and declare a cluster manager. The cluster manager is a separate process that monitors available resources and makes sure that all machines are responsive during the job. There are three different options of cluster managers:
  - Spark's own Standalone Cluster Manager
  - YARN from the Hadoop project
  - Another open-source manager from UC Berkeley's AMPLab Coordinators.

## Spark's Limitations
- Spark Streaming’s latency is at least 500 milliseconds since it operates on micro-batches of records, instead of processing one record at a time. Native streaming tools such as Storm, Apex, or Flink can push down this latency value and might be more suitable for low-latency applications. Flink and Apex can be used for batch computation as well.
- Another limitation of Spark is its selection of machine learning algorithms. Currently, Spark only supports algorithms that scale linearly with the input data size. In general, deep learning is not available either, though there are many projects that integrate Spark with Tensorflow and other deep learning tools.

## Data Lakes
### Key Features
- Lower costs associated with using big data tools for ETL / ELT operations.
- Data lakes provide schema-on-read rather than schema-on-write which lowers the cost and work of ingesting large amounts of data.
- Data lakes provide support for structured, semi-structured, and unstructured data. Whereas data warehouse only support highly structered data.

### Schema-On-Read and Schema-On-Write
Schema-on-read and schema-on-write are two different approaches to handling data in the context of data lakes. Schema-on-write refers to the traditional approach where data is structured and organized before it is written into the storage system. In this approach, a predefined schema is applied to the data, and it is validated and transformed to fit the schema before being loaded into the storage system. This ensures that the data is in a consistent and structured format from the beginning. Examples of systems that use schema-on-write include traditional relational databases and data warehouses.

On the other hand, schema-on-read is an alternative approach used in data lakes. In schema-on-read, the data is stored in its raw and unprocessed form, without any predefined schema. The schema is applied or interpreted at the time of reading or querying the data. This means that the data can be ingested into the data lake without any upfront transformation or validation. The schema is flexible and can be defined or modified as needed during the data exploration or analysis phase. This approach allows for more agility and flexibility in handling diverse and evolving data sources.

Schema-on-read provides several advantages. It allows for the storage of raw and unprocessed data, which can be valuable for data exploration, ad-hoc analysis, and data science use cases. It also reduces the upfront cost and complexity of data transformation, as the data can be loaded into the data lake without strict schema requirements. Additionally, schema-on-read enables the integration of both structured and unstructured data sources, providing a more comprehensive view of the data.

However, it's important to note that schema-on-read also introduces some challenges. Since the schema is applied at the time of reading, it requires additional processing and potentially impacts query performance. It also puts the responsibility on the data consumer to interpret and handle the data appropriately.

### Drawbacks of Datalakes
- No atomicity, means that the failed production jobs left the data in a corrupted state.
- No quality enforcement, which left us with inconsistent and therefore unusable data.
- No consistency/isolation, its impossible to stream and batch process data while ingesting.

## Lakehouse Architecture
The key innovation of the lakehouse architecture is the creation of a metadata and data governance layer on top of the data lake.
- This creates a pool of raw data as well as a curated set of data.
- This provides the flexibility and benefits we previously saw with data lakes, and it also provides solutions to the weaknesses in data lakes.
- One of the important features of a lakehouse architecture is the ability to quickly ingest large amounts of data and then incrementally improve the quality of the data.
- The key difference between data lakes and data lakehouse architectures is the inclusion of the metadata and governance layer. This is the crucial ingredient that provides atomicity, data quality, and consistency for the underlying data lake.

