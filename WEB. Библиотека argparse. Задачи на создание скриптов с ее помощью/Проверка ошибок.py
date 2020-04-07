import argparse
def print_error(text):
    print(f'ERROR: {text}!!')
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('string')
    arg = parser.parse_args()
    print('Welcome to my program')
    print_error(arg.string)