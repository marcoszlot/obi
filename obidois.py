N = input("Enter: ")
yey = raw_input("Enter: ")
alfa = yey.split(' ')
A = int(alfa[0])
L = int(alfa[1])
P = int(alfa[2])
if N <= A and N <= L and N <= P:
	print "S"
else:
	print "N"
