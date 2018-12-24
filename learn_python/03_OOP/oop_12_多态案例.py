class Dog:

	def __init__(self,name):
		self.name = name

	def game(self):
		print("%s 蹦蹦跳跳地玩耍"%self.name)

class XiaoTianDog(Dog):
	def game(self):
		print("%s can fly"%self.name)

class Person:

	def __init__(self,name):
		self.name = name

	def game_with_dog(self,dog):
		print("%s 和 %s 愉快的玩耍"%(self.name,dog.name))

		#让狗玩耍
		dog.game()
xtq = XiaoTianDog("哮天犬")
xiaoming = Person("小明")
xiaoming.game_with_dog(xtq)