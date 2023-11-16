#!/usr/bin/python2.7
"""retrieves from the HDFS files listed in l and store
them in the home /tmp folder of the user
"""
from snakebite.client import Client


def download(l):
    client = Client('localhost', 9000)


    for file in client.copyToLocal(l, '/tmp'):
        print(file)
