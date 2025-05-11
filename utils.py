import sys

def check_command_line_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def check_file_is_python_file(filename):
    if not filename.endswith(".py"):
        sys.exit("Not a python file")