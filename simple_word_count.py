# simple_word_count.py

from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Create a SparkSession
    # .appName sets a name for your application, useful for UI
    # .getOrCreate() will create a new SparkSession or return an existing one
    spark = SparkSession.builder \
        .appName("SimpleWordCount") \
        .getOrCreate()

    # Create a small RDD (Resilient Distributed Dataset) from a list of strings
    # This simulates having some data to process
    data = ["hello spark", "hello kubernetes", "spark on kubernetes", "test success"]
    rdd = spark.sparkContext.parallelize(data)

    # Perform the word count transformation
    # 1. flatMap(lambda line: line.split(" ")): Splits each line into words
    # 2. map(lambda word: (word, 1)): Creates (word, 1) pairs
    # 3. reduceByKey(lambda a, b: a + b): Sums up the counts for each word
    word_counts = rdd.flatMap(lambda line: line.split(" ")) \
                     .map(lambda word: (word, 1)) \
                     .reduceByKey(lambda a, b: a + b)

    # Collect the results and print them (an action)
    # .collect() brings all the results to the driver, so use with small results
    results = word_counts.collect()

    print("--- Word Count Results ---")
    for word, count in results:
        print(f"'{word}': {count}")
    print("------------------------")

    # Stop the SparkSession
    spark.stop()
    print("Spark job finished successfully.")