# Oliver Keen
# Learning Python, File Input/Output
# Utilizes command line input and exception handling
# 12/16/2020

# Usage: python3 fileio.py input_file [output_file] [--append (-a)]

import sys

# Receives number of arguments (n) and command line input (args)
# Returns file output mode (write/append) after verifying input
def verify(n, args):
    mode = 'w'   # Defaults to write

    if n >= 5:   # More than 4 args provided
        print("Too many arguments!")
        n = 5
        help(n)
    elif n == 1: # Only first arg (script) provided
        print("Too few arguments!")
        help(n)
    elif n == 4: # File output mode provided
        if args[n - 1] == "--append" or args[n - 1] == "-a":
            mode = 'a'
        else:
            print("Invalid file output mode \"" + args[n - 1] + "\"!")
            print("Avoid overwriting existing data with \"--append\" or \"-a\"")
            help(n)

    return mode

# Prints usage and exits with provided error code
# 1. Too few arguments
# 2. Unable to open input file
# 3. Unable to open output file
# 4. Invalid file output mode
# 5. Too many arguments
def help(code):
    print("Usage: fileio.py input_file [output_file] [--append (-a)]")
    print("Exiting (" + str(code) + ")")

    sys.exit(code)

# Prints contents of provided file to terminal
def cat(inputFile):
    try:
        file = open(inputFile, 'r')
    except OSError:
        print("Unable to open file \"" + inputFile + "\"!")
        help(2)
    with file:
        print(file.read(), end = '')

        file.close()

# Copies contents of input file to output file
def catFile(inputFile, outputFile, mode):
    try:
        fin = open(inputFile, 'r')
    except OSError:
        print("Unable to open file \"" + inputFile + "\"!")
        help(2)
    with fin:
        try:
            fout = open(outputFile, mode)
        except OSError:
            fin.close()

            print("Unable to open file \"" + outputFile + "\"!")
            help(3)
        with fout:
            fout.write(fin.read())

            fin.close()
            fout.close()

# Main body
mode = verify(len(sys.argv), sys.argv)

if len(sys.argv) == 2:
    cat(sys.argv[1])
else:
    catFile(sys.argv[1], sys.argv[2], mode)

sys.exit(0)
