#!/usr/bin/python2.7
from snakebite.client import Client
import os

def download(l):
    # Replace 'localhost' and 9000 with your HDFS NameNode address and port
    client = Client('localhost', 9000)

    results = []
    for file_path in l:
        # Form the path where the file will be saved locally
        local_path = '/tmp/' + os.path.basename(file_path)
        result_dict = {'path': local_path, 'result': False, 'error': '', 'source_path': file_path}

        try:
            # Using Snakebite client to copy the file from HDFS to local directory
            for _ in client.copyToLocal([file_path], '/tmp'):
                pass
            result_dict['result'] = True
        except Exception as e:
            result_dict['error'] = str(e)

        results.append(result_dict)

    return results

# Example usage
if __name__ == "__main__":
    download = __import__('6-download').download
    l = ["/holbies/input/lao.txt"]
    result = download(l)
    for r in result:
        print(r)

    # Reading the downloaded file
    with open('/tmp/lao.txt', 'r') as file:
        print(file.read())
