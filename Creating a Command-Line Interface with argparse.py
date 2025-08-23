import argparse

parser = argparse.ArgumentParser(description='A simple greeting script.')
parser.add_argument('--name', required=True, help='Your name')
parser.add_argument('--age', type=int, help='Your age')

args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")

# Run from terminal: python script.py --name "Alice" --age 30
