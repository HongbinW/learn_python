xiaoming_dict = {"name":"小明",
				 "age" : 18}

#1.统计键值数量
print(len(xiaoming_dict))

#2.合并字典
temp_dict = {"height":1.75,
			 "age" : 20}	#update，如果被合并的字典中包含已经存在的键值对，会覆盖原有的
xiaoming_dict.update(temp_dict)
#3.请空字典
xiaoming_dict.clear()
print(xiaoming_dict)