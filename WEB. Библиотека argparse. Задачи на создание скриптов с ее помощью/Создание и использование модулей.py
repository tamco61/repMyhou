import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', nargs='?', type=str)
arg = parser.parse_args()
p = arg.file
def count_lines(p):
    try:
        file = open(p).readlines()
        return len(file)
    except BaseException:
        return 0
if __name__ == '__main__':
    print(count_lines(p))