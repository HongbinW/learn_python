has_ticket = True
knife_length= 15
if has_ticket:
	print("有票，准备安检")
	if knife_length >= 20:
		print("不允许上车")
	else:
		print("安检通过")
else:
	print("无票，禁止入内")