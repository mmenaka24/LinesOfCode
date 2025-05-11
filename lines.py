import sys

def count_lines_of_code(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    line_count = 0

    for line in lines:
        stripped_line = line.strip()
        if not (stripped_line == '' or stripped_line.startswith('#')):
            line_count += 1
    
    return line_count

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file")

    try:
        print(count_lines_of_code(filename))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
    