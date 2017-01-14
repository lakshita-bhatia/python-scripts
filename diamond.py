print 'Hello, welcome to diamond world'
while 1:
	n=raw_input('Enter the value of n:')
	n=int(n)
	if n%2==0:
		print 'Error! give some odd number : '
	else:
		break
l=n/2
for i in range(0,n+1,2):
	print ' '*(l-(i/2)),'*'*(i+1)
l=1
for i in range(n-1,0,-2):
	print ' '*l,'*'*(i-1)
	l+=1

	
