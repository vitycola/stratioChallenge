##### Stratio Challenge #####

This challenge have been developed by Victor Valero to Stratio company.

Its divided in two applications:

    1 randomData.py: this script generates formatted data according to the phone logs "00:05:00,400-234-090" recieving
                       the number of lines to generate. The script takes in account the probability of the duration of
                       the call since calls are more likely to be around 5 minutes so that it generate duration calls
                       with poisson distribution.

                       Command to execute script: python randomData.py 100000 > data/calls.log

    2 phoneBill.py: this script calculates the bill of each call according to call's duration. It use spark framework
                    to support large volume of data. The script its prepared to execute in local mode althought its
                    better to execute in a Big Data cluster using Yarn or Mesos.

                    Command to execute script local mode: python phoneBill.py
                    Command to execute script cluster mode: spark-submit --master yarn --deploy-mode cluster \
                                                            --num-executors 5 --executor-memory 1G --executor-cores 2 \
                                                            --driver-memory 1G phoneBill.py
