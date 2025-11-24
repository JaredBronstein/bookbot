def charcount(filepath):
	with open(filepath) as f:
		words = f.read()
		words = words.lower()
		count = {}
		for char in words:
			if char in count:
				count[char] += 1
			else:
				count[char] = 1
		print(f"{count}: {count[char]}")

def wordcount(filepath):
	with open(filepath) as f:
		words = f.read()
		num = len(words.split())
		print(f"Found {num} total words")

def charlist(filepath):
	with open(filepath) as f:
		words = f.read().lower()
		num = len(words.split())
		count = {}
		for char in words:
			if char in count:
				count[char] += 1
			else:
				count[char] = 1
		new_count = sorted(count.items())
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {filepath}...")
		print("----------- Word Count ----------")
		print(f"Found {num} total words")
		print("--------- Character Count -------")
		for char in count:
			if(char.isalpha()):
				line = f"{char}: {count[char]}"
				print(line.replace("'", ''))
		print("============= END ===============") 
