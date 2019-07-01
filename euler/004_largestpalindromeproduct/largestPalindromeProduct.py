def isPalindrome(number):
	numberString = str(number)

	return True if numberString == numberString[::-1] else False

# TODO: Add functionality where function
# receives # of digits and returns largest
def largestPalindromeProduct(digits):
	largestPalindromeProduct = 0

	for x in range(100, 1000):
		for y in range(x, 1000):
			product = x * y
			if isPalindrome(product) and largestPalindromeProduct < (product):
				largestPalindromeProduct = product

	print(largestPalindromeProduct)


largestPalindromeProduct(3)
