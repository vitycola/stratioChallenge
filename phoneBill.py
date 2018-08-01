from pyspark.sql import SparkSession
import os
import re

os.environ['PYSPARK_PYTHON'] = '/Users/victor/anaconda3/envs/ds34/bin/python'

# Example in local

app_name = "example-logs"
master = "local[*]"
spark = (SparkSession.builder
         .master(master)
         .config("spark.driver.cores", 2)
         .appName("phoneBill")
         .getOrCreate())

secBillingType = 300
priceSecond = 3
priceMinute = 150

sc = spark.sparkContext
logs = sc.textFile("./data/calls.log")

def calcSeconds(hours,minutes,seconds):

    return hours*360 + minutes*60 + seconds


def calculateBill(time):

    hours,minutes,seconds = map(int,time.split(":"))
    totalSec = calcSeconds(hours, minutes, seconds)

    if (totalSec < secBillingType):
        bill = totalSec * priceSecond
    else:
        bill = (hours * 60 + minutes + int(bool(seconds))) * priceMinute # Calculate the price per minute

    return bill

pattern = "\d{2}:\d{2}:\d{2},\d{3}-\d{3}-\d{3}"

#Filter those lines that doesnt match the pattern and calculate the bill

result = logs.filter(lambda line: re.match(pattern,line))\
                 .map(lambda line: line.split(sep=","))\
                .map(lambda x: (x[1], x[0], calculateBill(x[0])))

print(result.take(5))