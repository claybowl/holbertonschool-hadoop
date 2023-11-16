#!/usr/bin/python2.7
"""function which takes list of directory paths
and creates those directories in HDFS using
Snakebite"""
from snakebite.client import Client


def createdir(directory_list):
    """takes list of directory paths and creates directories"""
    client = Client("localhost", 9000)

    try:
        for x in client.mkdir(directory_list):
            print(x)
    except Exception as e:
        print("Error: {}".format(e))
