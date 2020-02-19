from asmdoc.exceptions import ParseException
from asmdoc.container import Function

def skipWhitespace(line):
    while len(line) > 0 and any(line[0] == c for c in " \t\r\n"):
        line = line[1:]

    return line

def readToWhitespace(line):
    s = ""

    while len(line) > 0 and not any(line[0] == c for c in " \t\r\n"):
        s += line[0]
        line = line[1:]

    return s, line

def getCommand(line):
    cmd, line = readToWhitespace(line)      # Till 1st whitespace cmd
    line = skipWhitespace(line)
    arg1, line = readToWhitespace(line)     # Till 2nd whitepace arg1
    arg2 = skipWhitespace(line)

    arg2 = arg2.replace('\n', '').replace('\r', '')
    return cmd, arg1, arg2

def parseFile(fileHandle, fileName):

    functions = []
    function = None
    module = None
    for line in fileHandle:
        if len(line) == 0 or line[0] != '@':
            continue

        line = skipWhitespace(line[1:])
        if len(line) == 0:
            continue

        cmd, arg1, arg2 = getCommand(line)

        if cmd == "\\module":
            # Module was defined before
            if module != None:
                raise ParseException("Module was defined before")
            module = arg1

        elif cmd == "\\func":
            # Function defined before
            if function != None:
                functions.append( function )
            function = Function(fileName, arg1, arg2)

        elif cmd == "\\param":
            # No function defined before
            if function == None:
                raise ParseException("No function defined before \\param")
            function.addParameter(arg1, arg2)

        elif cmd == "\\returns":
            # No function defined before
            if function == None:
                raise ParseException("No function defined before \\return")
            function.setReturns(arg1 + " " + arg2)

    # End of file

    # If function defined
    if function != None:
        functions.append( function )

    return module, functions