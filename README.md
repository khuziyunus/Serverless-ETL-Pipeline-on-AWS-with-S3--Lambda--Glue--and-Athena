# Serverless ETL Pipeline on AWS with S3, Lambda, Glue, and Athena
Here I have built a serverless ETL pipeline that:  Extracts raw CSV data uploaded to an S3 bucket,  Transforms the data using AWS Glue (or a Lambda function for light cases),  Stores the processed data in another S3 bucket (in Parquet format),  Queries the data using Athena.
