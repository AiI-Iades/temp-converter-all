# Entry point for CLI tool
import converter
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('temp', type=float)
parser.add_argument('--from', required=True, choices=['C', 'F', 'K', 'R', 'N'])
parser.add_argument('--to', required=True, choices=['C', 'F', 'K', 'R', 'N'])
args = parser.parse_args()
result = converter.convert(args.temp, args.from, args.to)
print(f"{args.temp} {args.from} = {result} {args.to}")