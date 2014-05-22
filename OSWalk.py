#python code

import os, sys

# Open a file
initpath = str(sys.argv[1])
dirs = os.listdir( initpath )

print "all files in the directory" + initpath
print "*" * 20
maxwords = []
maxlength = 0
for root, dirs, files in os.walk(initpath):
	for filename in files:
		if filename.endswith(".m") or filename.endswith(".h"):
			f = open(os.path.join(root, filename),'r')
			string = f.read()
			words = string.split()
			for word in words:
				if len(word) > maxlength:
					maxlength = len(word)
					maxwords = [ word ]
				elif len(word) == maxlength:
					maxwords.append(word)
				print word
			f.close()
		print maxwords






''' steps to make this work:
	
	1. Enter in a directory in terminal through an argument
		- probably like: cschlyer$ python testing.py -/directory/subdirectory/someDirectory
	2. Iterate through all files, looking for a .h or .m file
		-  this could get complicated... recursive function?

	3. Once a file is found, all text is copied into a buffer (?) that the script can read
	4. All lines are read, looking for the longest variable / method name
		- probably look for continuous string... no whitespace or special characters
	5. When serching, store the whole string as a variable
		- add each new, non-special character to the variable
	6. Compare new word to length of the longest name
		- if two are the same, should store in an array
		- if new one is bigger, it becomes the longest string
		- if smaller, ignore and move on '''