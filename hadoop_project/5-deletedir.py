#!/usr/bin/python2.7
"""task 4"""
from snakebite.client import Client
import os


def download():
    client = Client('localhost', 5000)

    results = []
    for file_path in l:
        local_path = '/tmp/' + os.path.basename(file_path)
        result_dict = {'path': local_path, 'result': False, 'error': '', 'source_path': file_path}


        try:
            for _ in client.copyToLocal([file_path], '/tmp'):
                pass
            result_dict['result'] = True
        except Exception as e:
            result_dict['error'] = str(e)

        results.append(result_dict)

    return results



if __name__ == "__main__":
    l = ["/holbies/input/lao.txt"]
    result = download(l)
    for r in result:
        print(r)


    with open('/tmp/lao.txt', 'r') as file:
        print(file.read())
