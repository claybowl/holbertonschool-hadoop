#!/usr/bin/python2.7
"""task 4"""
from snakebite.client import Client


def deletedir(directory_list):
    # Initialize Snakebite client
    client = Client("localhost", 9000)

    # sort directory list in reverse order
    directory_list.sort(reverse=True)
    try:
        for x in client.rmdir(directory_list):
            print(x)
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    directory_list = ["/Betty", "/Betty/Holberton"]
    deletedir(directory_list)
