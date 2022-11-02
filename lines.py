import sys

def main():
    check_argv()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count_lines = 0
    for line in lines:
        if check_comment_or_emptyline(line) == False:
            count_lines += 1
    print(count_lines)

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if sys.argv[1].endswith(".py") == False:
        sys.exit("Not a python file")

def check_comment_or_emptyline(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()