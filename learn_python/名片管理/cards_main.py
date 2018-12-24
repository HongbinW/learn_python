
import cars_tools

while True:

	# TODO 显示功能菜单
	cars_tools.show_menu()

	action_str = input("请选择要执行的操作：")
	print("您选择的操作是【%s】" % action_str)

	# 1,2,3针对名片的操作
	# 0退出新四通
	# 其他输入错误，并提示用户
	if action_str in ["1","2","3"]:
		if action_str =="1":
			cars_tools.new_card()
		elif action_str =="2":
			cars_tools.show_all()
		elif action_str =="3":
			cars_tools.search_card()
		# 若果在开发程序时，不希望立即编写分支内部的代码
		# 可以使用pass关键字，表示一个占位符，保证代码结构正确，程序运行时，pass不会执行任何操作
		# pass
	elif action_str == "0":
		print("欢迎再次使用【名片管理系统】")
		break
	else:
		print("选择错误，请重新选择")

