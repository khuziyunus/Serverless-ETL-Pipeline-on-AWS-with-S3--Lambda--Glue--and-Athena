# 🛠️ AWS Serverless ETL Pipeline with S3, Glue & Athena

This project demonstrates how to build a fully serverless ETL (Extract, Transform, Load) data pipeline on AWS using S3, Glue, and Athena. It extracts raw CSV data uploaded to S3, transforms it using AWS Glue (written in PySpark), and queries the cleaned data with Athena.

---

## 📌 Table of Contents

- [🎯 Objective](#-objective)
- [🧰 Tools & Services Used](#-tools--services-used)
- [📁 Project Structure](#-project-structure)
- [🚀 How It Works](#-how-it-works)
- [🧪 Sample Dataset](#-sample-dataset)
- [📸 Screenshots](#-screenshots)
- [📊 Athena Query Result](#-athena-query-result)
- [📝 How to Run](#-how-to-run)
- [📈 Future Improvements](#-future-improvements)

---

## 🎯 Objective

To build a cost-efficient, scalable, and serverless data pipeline on AWS that:

- Accepts CSV files via Amazon S3.
- Cleans and transforms the data using AWS Glue with PySpark.
- Stores the transformed data in S3 as a single CSV.
- Enables querying and analysis using Amazon Athena.

---

## 🧰 Tools & Services Used

| Service         | Purpose                          |
|----------------|----------------------------------|
| **Amazon S3**   | Store raw and transformed data   |
| **AWS Glue**    | ETL pipeline using PySpark       |
| **AWS Athena**  | Query data using SQL             |
| **IAM**         | Access and permission control    |
| **CloudWatch**  | Logs and job monitoring          |
| **Python**      | Generate sample dataset          |

---

## 📁 Project Structure

