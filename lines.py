import sys


def count_lines_of_code(filename):
    line_count = 0

    with open(filename) as f:
        for line in f:
            stripped_line = line.strip()
            if not (stripped_line == "" or stripped_line.startswith("#")):
                line_count += 1

    return line_count

def check_command_line_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def check_file_is_python_file(filename):
    if not filename.endswith(".py"):
        sys.exit("Not a python file")


def main():

    check_command_line_args()

    filename = sys.argv[1]

    check_file_is_python_file(filename)

    try:
        print(count_lines_of_code(filename))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
