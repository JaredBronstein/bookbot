import sys

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) > 1:
		charlist(sys.argv[1])
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print(sys.argv)
from stats import wordcount, charcount, charlist

main()
