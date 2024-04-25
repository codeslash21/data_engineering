
## CloudShell Command
- `aws s3 mb s3://soumya-dend/` to create a S3 bucket with the name `soumya-dend`
- `aws s3 cp s3://udacity-dend/data-pipelines/ ~/data-pipelines/ --recursive` to copy the data from the udacity bucket to the home cloudshell directory
- `aws s3 cp ~/data-pipelines/ s3://soumya-dend/data-pipelines/ --recursive` to copy the data from the home cloudshell directory to your own bucket
- `aws s3 ls s3://soumya-dend/data-pipelines/` to list the data to be sure it copied over.


## Configure Variables - S3 Path
![image](https://github.com/codeslash21/data_engineering/assets/32652085/60e5c5a5-a0e4-47d6-8d1f-d1a9f8940b9d)

## NOTE
- While creating IAM role we can attach existing policies where we can define what are the accesses granted for this role. After, creating IAM role, we have to create credentials using `create access key` so that we can access this IAM role from other services like Airflow. We have to download the credentials as csv for future use. To access this IAM role from Airflow we can add that connection by providing `Access Key Id` and `Secret Key`.
- `airflow connections get aws_credentials -o json ` to get details in JSON format about the `aws_credentials` connection that we have created using Airflow UI
