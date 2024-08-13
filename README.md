# twitter_datapipeline_using_airflow

This project implements a data pipeline that fetches tweets using the Tweepy API, processes the data using Python, and loads it into AWS S3. The pipeline is managed and orchestrated using Apache Airflow.

## Features

- **Data Extraction**: Fetches tweets from Twitter using Tweepy API.
- **Data Transformation**: Processes and formats the tweet data.
- **Data Storage**: Uploads the processed data to AWS S3.
- **Orchestration**: Uses Apache Airflow for scheduling and managing workflows.

## Requirements

- Python 3.8+
- Apache Airflow
- Tweepy
- boto3 (for AWS S3 interaction)
- pandas (for data manipulation)
- AWS credentials (configured via environment variables or AWS CLI)

## Pre-requisites

1. **Clone the repository:**
   - create a new folder on to your desktop
   - open command prompt
   ```bash
   cd desktop\folder_name
   git clone https://github.com/bevaranikhil/twitter_datapipeline_using_airflow.git

2. **Install all the libraries:**
   - open Command Prompt.
   - Copy and install all libraries from [twitter_commands.sh](https://github.com/bevaranikhil/twitter_datapipeline_using_airflow/blob/main/twitter_comands.sh).

### Execution

- deploy [Twitter_dag](https://github.com/bevaranikhil/twitter_datapipeline_using_airflow/blob/main/twitter_dag.py) and [Twitter_etl](https://github.com/bevaranikhil/twitter_datapipeline_using_airflow/blob/main/twitter_etl.py) on to EC2 machine.

### Instructions:
1. **Replace placeholder values** with your specific credentials and repository information.
2. **Ensure that** the Airflow DAG file (`twitter_data_pipeline.py`) is properly set up in your repository with the required tasks for data extraction, transformation, and loading.



## Acknowledgments

- [Tweepy](https://github.com/tweepy/tweepy) for the Twitter API interaction.
- [Apache Airflow](https://airflow.apache.org/) for workflow orchestration.
- [AWS S3](https://aws.amazon.com/s3/) for cloud storage.
