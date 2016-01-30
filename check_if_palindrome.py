seq = raw_input('>>>')
if seq == seq[::-1]:
	print "%r is a palindrome!" % (seq)
else:
	print "%r isn't a palindrome" % (seq)
