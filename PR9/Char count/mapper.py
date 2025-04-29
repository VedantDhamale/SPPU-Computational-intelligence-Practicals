import sys
# Mapper for character counting
for line in sys.stdin:
    line = line.strip().replace(" ", "")  # remove spaces
    for char in line:
        print(f"{char}\t1")