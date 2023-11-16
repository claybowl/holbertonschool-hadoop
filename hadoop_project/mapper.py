#!/usr/bin/python2.7
import sys


parser = sys.stdin

for line in parser:
    line = line.split(',')
    print("{}\t{},{}".format(line[0], line[1], line[3]))
# def mapper():
#     for line in parse_input(sys.stdin):
        # Split the line into columns
#         columns = line.split(',')
# 
        # Check if the line has the right number of columns
#         if len(columns) >= 3:
#             id, company, total_compensation = columns[0], columns[1], columns[2]
#             # Print desired output frmt: id, company, and total compensation
#             print("{}\t{},{}".format(line[0], line[1], line[3]))

# if __name__ == "__main__":
#     mapper()
