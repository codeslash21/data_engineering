
## CloudShell Command
- `aws s3 mb s3://soumya-dend/` to create a S3 bucket with the name `soumya-dend`
- `aws s3 cp s3://udacity-dend/data-pipelines/ ~/data-pipelines/ --recursive` to copy the data from the udacity bucket to the home cloudshell directory
- `aws s3 cp ~/data-pipelines/ s3://soumya-dend/data-pipelines/ --recursive` to copy the data from the home cloudshell directory to your own bucket
- `aws s3 ls s3://soumya-dend/data-pipelines/` to list the data to be sure it copied over.


## Configure Variables - S3 Path
![image](https://github.com/codeslash21/data_engineering/assets/32652085/60e5c5a5-a0e4-47d6-8d1f-d1a9f8940b9d)

## AWS Redshift
- Type the following command from AWS cloudshell to create redshift role
```
aws iam create-role --role-name my-redshift-service-role --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "redshift.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}'
```
- Command to give redshift role full access to S3
```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --role-name my-redshift-service-role
```

## Set Up Connections
### Connecting to AWS
The `MetastoreBackend` python class connects to the Airflow Metastore Backend to retrieve credentials and other data needed to connect to outside systems.
```
from airflow.decorators import dag
from airflow.secrets.metastore import MetastoreBackend

@dag(
    start_date=pendulum.now()
)
def load_data_to_redshift_dag():
    @task
    def copy_task():    
        metastoreBackend = MetastoreBackend()
        aws_connection=metastoreBackend.get_connection("aws_credentials")
        logging.info(vars(aws_connection))
```

### Connecting to Redshift
To connect to Redshift, you can use the PostgresHook and PostgresOperator classes provided by Airflow. 
#### PostgresHook
The `PostgresHook` class is a superclass of the Airflow `DbApiHook`. When you instantiate the class, it creates an object that contains all the connection details for the Postgres database. It retrieves the details from the Postgres connection you created earlier in the Airflow UI.
```
from airflow.hooks.postgres_hook import PostgresHook

def load_task():    
      redshift_hook = PostgresHook("redshift")
      redshift_hook.run("SELECT * FROM trips")
```

#### PostgresOperator
The PostgresOperator class executes sql, and accepts the following parameters:
- postgres_conn_id
- task_id
- sql statement
- optionally a dag
```
from airflow.operators.postgres_operator import PostgresOperator

location_traffic_task = PostgresOperator(
        task_id="calculate_location_traffic",
        postgres_conn_id="redshift",
        sql="SELECT * FROM trips"
)
```

## NOTE
- While creating IAM role we can attach existing policies where we can define what are the accesses granted for this role. After, creating IAM role, we have to create credentials using `create access key` so that we can access this IAM role from other services like Airflow. We have to download the credentials as csv for future use. To access this IAM role from Airflow we can add that connection by providing `Access Key Id` and `Secret Key`.
- `airflow connections get aws_credentials -o json ` to get details in JSON format about the `aws_credentials` connection that we have created using Airflow UI
