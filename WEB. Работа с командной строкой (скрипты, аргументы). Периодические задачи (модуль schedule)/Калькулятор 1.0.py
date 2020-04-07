import sys
s = 0
if len(sys.argv) > 2:
    for r in range(1, 3):
        t = True
        for i in sys.argv[r]:
            if i not in '1234567890':
                t = False
        if not t:
            break
    if t:
        s = int(sys.argv[1]) + int(sys.argv[2])
print(s)