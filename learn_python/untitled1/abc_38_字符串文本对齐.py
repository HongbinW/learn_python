poem = ["登鹳雀楼",
		"王之涣",
		"白日依山尽",
		"黄河入海流",
		"欲求千里目",
		"更上一层楼"]

for poem_str in poem:
	# print("|%s|" %poem_str.center(10,"　"))	#默认使用英文空格填充，使用全半角输入时，可以使其对齐
	print("|%s|" % poem_str.rjust(10, "　"))