import sys

# Mapper for word counting
for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(f"{word}\t1")