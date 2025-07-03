import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw data from catalog
AmazonS3_node1751561021778 = glueContext.create_dynamic_frame.from_catalog(
    database="raw_sales_db",
    table_name="sample_sales_data_csv",
    transformation_ctx="AmazonS3_node1751561021778"
)

# Drop duplicate rows
DropDuplicates_node1751561076834 = DynamicFrame.fromDF(
    AmazonS3_node1751561021778.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1751561076834"
)

# Drop unwanted fields
DropFields_node1751561173579 = DropFields.apply(
    frame=DropDuplicates_node1751561076834,
    paths=["payment_method"],
    transformation_ctx="DropFields_node1751561173579"
)

# Evaluate Data Quality
EvaluateDataQualityMultiFrame_node1751563303731_ruleset = """
    Rules = [
        RowCount > avg(last(10)) * 0.6,
        ColumnCount >= max(last(1))
    ]
"""

EvaluateDataQualityMultiFrame_node1751563303731 = EvaluateDataQuality().process_rows(
    frame=DropFields_node1751561173579,
    ruleset=EvaluateDataQualityMultiFrame_node1751563303731_ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQuality_node1751561003796",
        "enableDataQualityResultsPublishing": True
    },
    additional_options={
        "performanceTuning.caching": "CACHE_NOTHING",
        "observations.scope": "NONE"
    }
)

# Select cleaned data (originalData output from DQ)
originalData_node1751563303732 = SelectFromCollection.apply(
    dfc=EvaluateDataQualityMultiFrame_node1751563303731,
    key="originalData",
    transformation_ctx="originalData_node1751563303732"
)

# Convert to DataFrame
final_df = originalData_node1751563303732.toDF()

# Write as a single CSV file to S3 (no partitions)
final_df.coalesce(1).write \
    .option("header", "true") \
    .mode("overwrite") \
    .csv("s3://aws-serverless-etl-project-processed-bucket/sales/")

job.commit()
