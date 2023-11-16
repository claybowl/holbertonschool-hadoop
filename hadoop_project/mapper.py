#!/usr/bin/python2.7
import sys

def parse_input(file):
    for line in file:
        yield line.strip()

def mapper():
    for line in parse_input(sys.stdin):
        # Split the line into columns
        columns = line.split(',')

        # Check if the line has the right number of columns
        if len(columns) >= 3:
            id, company, total_compensation = columns[0], columns[1], columns[2]
            # Print the desired output format: id, company, and total yearly compensation
            print(f"{id}\t{company},{total_compensation}")

if __name__ == "__main__":
    mapper()
