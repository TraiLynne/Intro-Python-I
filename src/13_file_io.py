"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
file = open('foo.txt')

for line in file:
	print(line.rstrip())

file.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newfile = open("bar.txt", "w")
newfile.write("Hello\n")
newfile.write("My name is Trai Lynne Compton\n")
newfile.write("I am a full stack web developer\n")
newfile.close()
