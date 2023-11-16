#!/usr/bin/python2.7
"""function which takes list of directory paths
and creates those directories in HDFS using
Snakebite"""
from snakebite.client import Client


def createdir():
    """takes list of directory paths and creates directories"""
    client = Client('localhost', 9000) # replace with hadoop NameNode host info
    for dir in l:
        result = client.mkdir([dir]), create_parent=True)
        for r in result:
            print({'path': r['path'], 'result': r['result']}]

if __name__ == "__main__":
    # usage
    dir_list = ["/Betty", "/Betty/Holberton"]
    createdir(dir_list)
