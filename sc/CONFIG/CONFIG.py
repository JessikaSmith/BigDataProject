APP_NAME = 'Twitter Stat'
# Standalone version:
SPARK_ADDRESS = "local[*]"
RAW_DATA_PATH = '../data/raw_data.csv'
TMP_DIR_PATH = '../data/'
OUTPUT_PATH = '../data/USER_SENT_TOPIC.parquet'

# Multi-node version:
# SPARK_ADDRESS = "spark://192.168.13.133:7077"
# HDFS_ADDRESS = "hdfs://192.168.13.133:8020/"
# os.environ["HADOOP_CONF_DIR"] = "/usr/local/hadoop/conf"