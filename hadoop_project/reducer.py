#!/usr/bin/python2.7
import sys
import heapq

def parse_input(file):
    for line in file:
        yield line.strip()

def reducer():
    min_heap = []

    for line in parse_input(sys.stdin):
        parts = line.split('\t')
        if len(parts) == 2:
            _, value = parts
            company, salary = value.rsplit(',', 1)
            try:
                salary = float(salary)
                # Add to the heap and maintain the size of 10
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (salary, line))
                else:
                    heapq.heappushpop(min_heap, (salary, line))
            except ValueError:
                pass  # Ignore lines where salary is not a number

    # Extract the top ten salaries
    top_salaries = heapq.nlargest(10, min_heap)
    
    # Print the results
    print("id\tSalary\tcompany")
    for salary, line in sorted(top_salaries, reverse=True):
        print(line)

if __name__ == "__main__":
    reducer()
