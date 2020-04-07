import sys
try:
    v = True
    if len(sys.argv) > 1:
        ret = 0
        for i in range(1, len(sys.argv)):
            if v:
                ret += int(sys.argv[i])
            else:
                ret -= int(sys.argv[i])
            v = not v
        print(ret)
    else:
        print('NO PARAMS')
except ValueError:
    print('ValueError')