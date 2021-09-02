import sys
import pathlib
def main():
    if len(sys.argv) < 2:
        print("Please enter a proper file path")
        return
    fp = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(fp), 'r') as f:
        text_in = f.read()
    print(text_in)
    tokens = text_in.split(',')
    for x in tokens:
        print(x)

if __name__ == '__main__':
    main();
