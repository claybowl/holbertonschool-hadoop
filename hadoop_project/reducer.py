#!/usr/bin/env python3
"""Reducer script to find the top ten salaries."""

import sys
import re

def parse_line(line):
    """Parse line and extract id, company, and salary."""
    parts = re.split('\t|,', line.strip())
    if len(parts) == 3:
        try:
            return int(parts[0]), parts[1], float(parts[2])
        except ValueError:
            return None
    return None

def main():
    top_salaries = []

    for line in sys.stdin:
        parsed_line = parse_line(line)
        if parsed_line:
            id, company, salary = parsed_line

            # Add to top_salaries and maintain its size to 10
            if len(top_salaries) < 10:
                top_salaries.append((id, company, salary))
            elif salary > top_salaries[-1][2]:
                top_salaries[-1] = (id, company, salary)
            
            top_salaries.sort(key=lambda x: x[2], reverse=True)

    print("id\tSalary\tcompany")
    for id, company, salary in top_salaries:
        print(f"{id}\t{salary}\t{company}")

if __name__ == "__main__":
    main()
