# Function to convert decimal number
# to binary using recursion

from time import time

def DecimalToBinary(num):
	b = num
	count = 0
  
    # Count the number of iterations to
    # reach x = 0.
	while (b!=0):
		b = (b & (b << 1))
		print(b)
		count=count+1
	return count


# Driver Code
if __name__ == '__main__':
	
	# decimal value
	dec_val = 7
	
	st=time()

	# Calling function
	print(DecimalToBinary(dec_val))

	et=time()

	tt=et-st

	print('Total exec time ',tt)
