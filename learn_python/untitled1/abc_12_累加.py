"""
i = 0
sum1 = 0
while i<=100:
	sum1 += i
	i+= 1
print("0-100之间的数字求和结果 = %d"%sum1)
"""

i = 0
sum1 = 0
while i<=100:
	if i % 2 ==0:
		sum1 += i
	i+= 1
print("0-100之间的偶数数字求和结果 = %d"%sum1)
