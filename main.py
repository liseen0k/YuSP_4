with open("input.txt") as textFile:
    lines = [line.split() for line in textFile]
    textFile.close()
print(lines.__str__())
