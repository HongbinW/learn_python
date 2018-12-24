def sum_numbers(*args):
	result = 0
	for i in args:
		result += i

	return result

r = sum_numbers(1,2,3,4,5)
print(r)
