#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):

    with open(fileName, "r") as f:
        return f.read()


def longestLine(fileName):
    longest = ""
    with open(fileName, "r") as f:
        for line in f:
            clean_line = line.strip("\n")
            if len(clean_line) > len(longest):
                longest = clean_line
    return longest


def toBinary(fileName):
    with open(fileName, "r") as f:
        content = f.read().strip()  # Get all bits as one string

    bytes_list = []
    for i in range(0, len(content), 8):
        chunk = content[i: i + 8]
        bytes_list.append(chunk)

    return bytes_list

