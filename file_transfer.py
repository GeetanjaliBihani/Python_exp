#An interactive file transfer function

#Creating a function to enable file transfer
def file_transfer(arg1, arg2):
	open(arg1, 'a').write(open(arg2).read())
	print "Viola! File transfer from %r to %r done!" % (arg1, arg2)

#Creating a function to give file details
def file_details(arg1):
	length = int(len(open(arg1).read()))
	print "Uhm...Your file is only %d bytes long." %length
	
#A fun prompt?
response = str(raw_input("Are you ready for some fun? Y / N ?"))


if response=='Y':
	print "Let's start with transferring a file's contents from one end to another!"
	print("Write the name of your input file.")
	input = raw_input(">")
	print "Write the name of your output file"
	output = raw_input(">")
	file_transfer(output, input)
	print "File transfer done!"
	print "Now, let's find the length of our files."
	print "Which file's size do you want to calculate?"
	chosen_one = raw_input(">")
	file_details(chosen_one)

elif response=='N':
	print "You are no fun..."

print "~FIN~"
	
	
	
	
	

