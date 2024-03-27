import re

def parse_line(s):
    pattern = r'(\d+),(\d+),(\d+),(.+)'  # 4 groups: 3 numbers and 1 string
    match = re.fullmatch(pattern, s.strip())  # Use strip() to remove newline characters
    return (int(match.group(1)), int(match.group(2)), int(match.group(3)), match.group(4)) if match else None

def parse_file(path):
    results = {}  # Dictionary to hold the results
    non_matching_lines = 0  # Counter for non-matching lines
    with open(path, 'r') as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                year, count, _, name = parsed
                key = (name, year)
                if key in results:
                    results[key] += count
                else:
                    results[key] = count
            else:
                non_matching_lines += 1
                print(f"Non-matching line: {line.strip()}")  # Print non-matching lines
    if non_matching_lines > 0:
        print(f"Total non-matching lines: {non_matching_lines}")
    return results

def name_frequency(d):
    result = {}
    for (name, _), count in d.items():
        if name in result:
            result[name] += count
        else:
            result[name] = count
    return result


def popular_name(fname, n):
    # Parse the file to get name counts per year
    results = parse_file(fname)

    # Aggregate name counts across years
    name_totals = name_frequency(results)

    # Sort names by total count, in descending order
    sorted_names = sorted(name_totals.items(), key=lambda x: x[1], reverse=True)

    # Print the top n names
    for name, total in sorted_names[:n]:
        print(f"{name} {total}")


# Example usage:
fname = 'prenoms.txt'  # Make sure to use the correct path to your file
n = 5
popular_name(fname, n)

# Example usage
#path = 'prenoms.txt'  # Ensure this is the correct path to your file
#results = parse_file(path)  # Now 'results' is defined here before being used

# Use the function with the results from `parse_file`
#name_totals = name_frequency(results)

# Printing the total counts for each name
#for name, total in name_totals.items():
#    print(f"{name}: {total}")
