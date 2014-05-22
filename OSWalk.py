#python code

import os, sys, string, re

# Open a file
initpath = str(sys.argv[1])
dirs = os.listdir( initpath )

print "all files in the directory" + initpath
print "*" * 20
maxword = ""
maxlength = 0
for root, dirs, files in os.walk(initpath):
	for filename in files:
		if filename.endswith(".m") or filename.endswith(".h"):
			f = open(os.path.join(root, filename),'r')
			stringToRead = f.read()
			new_string = re.sub('[^a-zA-Z0-9\n]', ' ', stringToRead)
			words = new_string.split()
			#words = ''.join(c for c in stringToRead if c.isalnum() or c.isspace()).split()
			for word in words:
				if len(word) > maxlength:
					maxlength = len(word)
					maxword = word
				#print word
			f.close()
print maxword
