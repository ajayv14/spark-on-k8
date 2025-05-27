# Dockerfile
FROM apache/spark:latest 

# Copy Spark application script into the image
COPY simple_word_count.py /opt/spark/work-dir/simple_word_count.py